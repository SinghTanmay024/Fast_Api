# FastAPI Project

This is a FastAPI project that provides APIs for various functionalities. It uses `uvicorn` as the ASGI server.

## Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies from `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI application using `uvicorn`:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
- `main` refers to the filename (`main.py`) where the FastAPI app instance is defined.
- `app` is the FastAPI instance inside `main.py`.
- `--reload` enables auto-reloading on code changes (useful for development).

## API Documentation

FastAPI provides interactive API documentation automatically:
- Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Open ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the MIT License.

