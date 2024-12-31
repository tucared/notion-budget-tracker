# Streamlit App

## Setup

1. Install [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) if not done already

2. Setup virtual env

    ```shell
    uv sync
    ```

## Running

1. Start server
   - In python environment: `uv run streamlit run app.py`
   - In dockerised environment: `docker-compose up --build`

2. Go to <http://localhost:8501/>
   - Username: `rbriggs`
   - Password: `abc` (hashed in `config.yaml`)

## Editing

- Check linting and type errors

    ```shell
    uv run ruff check
    uv run mypy app.py
    ```

- Run formatter and fix linting errors

    ```shell
    uv run ruff format
    uv run ruff check --fix
    ```

- Add/remove dependency
  
    ```shell
    uv add pandas
    uv remove pandas

    uv add ruff --dev
    uv remove ruff --dev

    # After changes, you need to sync to `uv.lock` file
    uv sync
    ```
