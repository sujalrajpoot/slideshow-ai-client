from typing import Optional, Dict, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass
import requests
import json

class SlideShowAIError(Exception):
    """Custom exception for SlideShowAI-related errors."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.details = details


class APIClient(ABC):
    """
    Abstract base class for API clients.
    Defines the interface that concrete API clients must implement.
    """

    @abstractmethod
    def send_request(self, endpoint: str, payload: Dict[str, Any]) -> Any:
        """Send a request to the given API endpoint with the specified payload."""
        pass


@dataclass
class SlideShowAIClient(APIClient):
    """
    SlideShowAI client implementation for interacting with the SlideShow API.
    
    Attributes:
        api_url (str): The base URL of the SlideShow API.
    """
    api_url: str

    def send_request(self, endpoint: str, payload: Dict[str, Any]) -> Any:
        """
        Sends a POST request to the specified API endpoint with the given payload.

        Args:
            endpoint (str): The API endpoint to send the request to.
            payload (Dict[str, Any]): The payload for the request.

        Returns:
            Any: The response content from the API.

        Raises:
            SlideShowAIError: If the request fails or the response code indicates an error.
        """
        try:
            response = requests.post(endpoint, json=payload, stream=True)
            if response.status_code != 200:
                raise SlideShowAIError(
                    f"Error: Received response code {response.status_code}",
                    details={"response_content": response.text}
                )
            return response
        except requests.RequestException as e:
            raise SlideShowAIError(f"Request failed: {e}")


class SlideShowAI:
    """
    SlideShowAI encapsulates the logic for interacting with the SlideShow AI API.

    Attributes:
        client (SlideShowAIClient): An instance of the SlideShowAIClient for API interactions.
    """
    API_URL = "https://slideshow-5.onrender.com/process_message"

    def __init__(self) -> None:
        self.client = SlideShowAIClient(self.API_URL)

    def chat(self, user_query: str, prints: bool = True) -> str:
        """
        Initiates a conversation with the SlideShow AI by sending a user query.

        Args:
            user_query (str): The user's query to send to the SlideShow AI.
            prints (bool, optional): Flag to indicate whether to print the response in real-time. Defaults to True.

        Returns:
            str: The complete response content from the SlideShow AI.

        Raises:
            SlideShowAIError: If the response contains errors or fails to decode.
        """
        payload = {"message": user_query}
        complete_response = ""

        try:
            response = self.client.send_request(self.API_URL, payload)
            for line in response.iter_lines(decode_unicode=True, chunk_size=1):
                if line:
                    try:
                        json_data = json.loads(line)
                        content = json_data.get('response', '')
                        if prints:
                            print(content, end='', flush=True)
                        complete_response += content
                    except:continue
        except SlideShowAIError as e:
            return f"Error: {e}"

        return complete_response.strip().replace('\n', '')

# Example usage
if __name__ == "__main__":
    slideshow_ai = SlideShowAI()
    try:
        response_text = slideshow_ai.chat("What is artificial intelligence?")
        print("\nSlideShowAI:", response_text)
    except SlideShowAIError as e:
        print(f"An error occurred: {e}")
