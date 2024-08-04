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
    ```

3. Freeze dependencies (needs some manual cleaning afterwards)

    ```shell
    pip freeze > requirements.txt
    ```

## Run the app locally

`streamlit run app.py`
