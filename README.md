# SlideShowAI Client

A Python-based client to interact with the SlideShow AI API. This client enables real-time communication with the SlideShow AI server, streaming responses to user queries in a clean and efficient manner.

---

## 🚨 Important Disclaimer

**EDUCATIONAL PURPOSE ONLY**

This project is intended solely for educational purposes and is not affiliated with or endorsed by the SlideShow AI organization. It is designed to demonstrate API interaction techniques in Python and is not meant to harm, misuse, or overload the API or its associated organization. Please use this responsibly and in accordance with the API's terms of service.

---

## Features

- **Streamed API Responses**: Real-time streaming of API responses for a seamless experience.
- **Custom Error Handling**: Provides detailed error messages with contextual information.
- **Extensible Architecture**: Uses advanced OOP concepts such as abstract base classes and custom exceptions.
- **Ease of Use**: Simple and intuitive interface for interacting with the SlideShow AI.

---

## Requirements

- Python 3.7 or higher
- Internet connection (for API interaction)

---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/sujalrajpoot/slideshow-ai-client.git
    cd slideshow-ai-client
    ```

2. Install dependencies:

    ```bash
    pip install requests
    ```

---

## Usage

### Example Interaction

Here’s how to use the `SlideShowAI` client in your Python code:

```python
if __name__ == "__main__":
    slideshow_ai = SlideShowAI()
    try:
        response_text = slideshow_ai.chat("What is artificial intelligence?")
        print("\nSlideShowAI:", response_text)
    except SlideShowAIError as e:
        print(f"An error occurred: {e}")
```

## Key Components
1. `SlideShowAI`:
- Provides the main interface for interacting with the API.
- Streams responses in real-time and processes them into a complete message.

2. `SlideShowAIClient`:

- Handles HTTP communication with the API.
- Implements the APIClient abstract base class for extensibility.

3. `SlideShowAIError`:

- Custom exception for handling API-related errors with additional context.

---

## Extensibility
This client is designed with flexibility in mind. You can extend its functionality by:

- Adding new API endpoints to the SlideShowAIClient.
- Overriding methods in the APIClient base class.

---

## API Endpoint
The client communicates with the SlideShow AI server at:

```bash
https://slideshow-5.onrender.com/process_message
```

## Payload Example
```json
{
    "message": "What is artificial intelligence?"
}
```

## Response Format
The server returns streamed JSON responses with the following structure:

```json
{
    "response": "Artificial Intelligence (AI) refers to..."
}
```

## Error Handling
Errors are captured as instances of `SlideShowAIError` and include:

- Error messages
- Contextual details (e.g., response content or exception info)

---

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact
For questions or support, please open an issue or reach out to the maintainer.

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the project repository.
