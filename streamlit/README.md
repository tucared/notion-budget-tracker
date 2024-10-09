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

### Publish image to Artifact Registry

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

3. Build and tag local image (arch linux)

    ```shell
    export REPOSITORY=streamlit
    export IMAGE=streamlit_app
    export IMAGE_URL=$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE

    docker build -f Dockerfile -t $IMAGE . --platform linux/amd64
    docker tag $IMAGE $IMAGE_URL
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
    docker push $IMAGE_URL
    ```

6. Check image is pushed

    ```shell
    gcloud artifacts docker images list $IMAGE_URL
    ```

### Deploy Cloud Run app

1. Create service account

    ```shell
    # Set variables
    export PROJECT_ID=XXX
    export SERVICE_ACCOUNT_NAME="cloud-run-sa"
    export DATASET_ID="notion_cloud_function"
    export DATASET_LOCATION="US"

    # Create service account
    gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME \
        --project=$PROJECT_ID \
        --display-name="Cloud Run Service Account"

    # Add Data Viewer role to the service account for the specific dataset
    bq show \
        --format=prettyjson \
        $PROJECT_ID:$DATASET_ID > bq_policy.json


    gcloud projects add-iam-policy-binding $PROJECT_ID \
        --member="serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/bigquery.dataViewer" \
        --condition="resource.type=bigquery.googleapis.com/Dataset AND resource.name=//bigquery.googleapis.com/projects/$PROJECT_ID/datasets/monthly-finance.notion_cloud_function AND resource.location=$DATASET_LOCATION"

    # Delete service account
    gcloud iam service-accounts delete "$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
        --project=$PROJECT_ID \
        --quiet
    ```

2. Create Cloud Run instance

    ```shell
    export REGION=europe-west9
    export SERVICE_NAME=streamlit-app
    gcloud run deploy $SERVICE_NAME --image $IMAGE_URL --region $REGION

    gcloud run services list
    ```

## Cleanup

Delete Cloud Run service

```shell
gcloud run services delete $SERVICE_NAME --region $REGION
```

Delete image from Container registry

```shell
gcloud artifacts docker images delete $IMAGE_URL --delete-tags
```
