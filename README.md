# FastAPI Python Bundle

This repository contains a FastAPI Python bundle. Follow the instructions below to set it up and run it on your local machine.

## Prerequisites

- Python 3.7 or higher installed on your machine.
- pip package manager installed.
- Git installed (optional, if you want to clone this repository).

## Setting Up Environment

1. Clone this repository (if you haven't already):

  *>> bash or CMD:*
  
  ~~~
   git clone <repository-url>
  ~~~

2. Navigate into the cloned repository:

  ~~~
   cd <repository-name>
  ~~~

3. Create a virtual environment:

  ~~~
   python -m venv .venv
  ~~~
  
4. Activate the virtual environment:

  *>> on windows:*

  ~~~
   venv\Scripts\activate
  ~~~

  *>> on macOS and linux:*

  ~~~
   source venv/bin/activate
  ~~~

5. Install the required dependencies using pip:

  ~~~
   pip install -r requirements.txt
  ~~~

6. Set you local .env file with your URIs and so.

7. After installing the dependencies, you can start the FastAPI application:

  ~~~
   uvicorn main:app --reload
  ~~~

8. Once the server starts, visit http://localhost:8000/docs in your browser to access the interactive API documentation provided by FastAPI.


## Additional Notes

If you're deploying this application for production, make sure to change the --reload flag when running uvicorn as it's meant for development purposes only.
Customize the FastAPI application according to your project requirements by modifying the files in the repository.
Refer to the FastAPI documentation for more advanced usage and features: FastAPI Documentation


2:49