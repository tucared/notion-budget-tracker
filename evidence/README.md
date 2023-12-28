1. Create service account with BigQuery User role

    ```shell
    gcloud ... # TODO
    ```

2. Download its service key

    ```shell
    gcloud iam service-accounts keys create gcp_key.json \
        --iam-account=... # TODO
    ```

3. Set connection options to use this service key

    ```shell
    npm run dev
    # Settings > Connections
    ```

4. Check it works locally

    ```shell
    npm run sources
    ```

5. Create app

    ```shell
    gcloud app create --project=$PROJECT_ID
    # Please enter your numeric choice:  14
    ```

6. Deploy app

    ```shell
    cd evidence
    gcloud app deploy --project=$PROJECT_ID
    # Do you want to continue (Y/n)?  y
    ```

7. Disable your app ([doc](https://cloud.google.com/appengine/docs/standard/python3/building-app/cleaning-up#disabling_your_application))