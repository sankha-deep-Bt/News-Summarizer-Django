# New Summarizer Project

This project is a text summarization tool built with Django. Below are the steps to set up the project, install dependencies, and run the server.

## Prerequisites
- Ensure you have Python installed on your system. You can download it from python.org.

## Setting Up the Virtual Environment

### 1. Create a Virtual Environment

1. Open your terminal or command prompt.
2. Navigate to your project directory.
3. Run the following command to create a virtual environment:

    ```bash
    python -m venv .venv
    ```

    This will create a directory named `.venv` in your project folder.

### 2. Activate the Virtual Environment

- **Windows:**

    ```bash
    .\.venv\Scripts\activate
    ```

- **macOS/Linux:**

    ```bash
    source .venv/bin/activate
    ```

    After activation, you should see `(.venv)` at the beginning of your terminal prompt.

## Installing Dependencies

### 3. Install Packages from `requirements.txt`

1. Ensure you have a `requirements.txt` file in your project directory.
2. Run the following command to install the packages listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### 4. Deactivate the Virtual Environment

- When you're done working in the virtual environment, you can deactivate it by running:

    ```bash
    deactivate
    ```

## Running the Server

### 1. Navigate to the `new_summarizer` Folder:

   ```bash
   cd news_summarizer
  ```

### 2. Run the following Command:

  ```bash
    python manage.py runserver
  ```


## THE ERRORS ARE THERE BECAUSE MIGRATIONS HAVE NOT BEEN DONE THEY CAN BE IGNORED

## To get ruid of the error run the following commands one by one:

  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
