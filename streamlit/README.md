# Streamlit App

## Local dev

### Setup

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

### Run the app locally

In python environment: `streamlit run app.py`

In dockerised environment: `docker-compose up --build`

## Publish to Cloud Run

1. Set variables

    ```shell
    export PROJECT_ID=XXX
    gcloud config set project $PROJECT_ID
    ```

2. Authenticate to Google Artifact Registry with gcloud CLI

    ```shell
    export LOCATION=europe-west9
    gcloud auth configure-docker $LOCATION-docker.pkg.dev
    ```

3. Build and tag local image

    ```shell
    export REPOSITORY=streamlit
    export IMAGE=streamlit_app

    docker build -f Dockerfile -t $IMAGE .
    docker tag $IMAGE $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
    ```

4. Create repository on Google Artifact Registry

    ```shell
      gcloud artifacts repositories create $REPOSITORY \
        --repository-format=docker \
        --location=$LOCATION \
        --description="Used to store data app image"

    gcloud artifacts repositories describe $REPOSITORY \
        --location=$LOCATION
    ```

5. Push image to Google Artifact Registry

    ```shell
    docker push $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
    ```

6. Check image is pushed

    ```shell
    gcloud artifacts docker images list \
        $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
    ```

## Cleanup

1. Delete image from Container registry

    ```shell
    gcloud artifacts docker images delete $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE --delete-tags
    ```
