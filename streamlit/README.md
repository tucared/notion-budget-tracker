# Local dev

## Setup

1. Create virtual environment

    ```shell
    pyenv install 3.12.4
    pyenv virtualenv 3.12.4 nbt-streamlit
    pyenv local nbt-streamlit
    ```

2. Install dependencies

    ```shell
    pip install -r requirements.txt
    pip install -r requirements.dev.txt
    ```

3. Check linting and type errors

    ```shell
    ruff check
    mypy app.py
    ```

4. Run formatter and fix linting errors

    ```shell
    ruff format
    ruff check --fix
    ```

5. Freeze dependencies (needs some manual cleaning afterwards)

    ```shell
    pip freeze > requirements.txt
    ```

## Run the app locally

`streamlit run app.py`
