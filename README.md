# Simple Social Frontend

A Streamlit frontend application offering a unified platform for sharing images and videos. This is the UI client for the Simple Social application, featuring user authentication, media upload via ImageKit, and a dynamic social feed.

## Features

-   **User Authentication**: JWT-based signup and login flows communicating with a remote backend.
-   **Media Upload**: Support for image and video uploads directly integrated via the backend.
-   **Social Feed**: Real-time feed displaying posts from all users with timestamps and captions.
-   **Interactive UI**: A responsive, clean interface built entirely with Streamlit.

## Tech Stack

-   **Frontend**: Streamlit
-   **Http Client / API Integration**: Requests (Python)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Start the Streamlit application:
```bash
streamlit run frontend.py
```
The application will open in your default browser (usually at `http://localhost:8501`).

## License
MIT
