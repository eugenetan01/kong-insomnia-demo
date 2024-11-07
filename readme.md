# Setup
1. git clone this repo

    - navigate to the collection tab and change the env vars (cmd-e) to use the `OpenAPI env localhost:3000` env

2. start the services:

    ```bash
    docker-compose -f ./docker/docker-compose-bankong-combined_local_portchange.yaml up -d
    ```

3. check the services are running:
    - frontend: http://localhost:29080/
    - backend: http://localhost:3000/transactions

# Execution:

1. go to spec tab of the cloned collection and show how you can edit the openapi specs

2. show the linting errors by deleting the `contacts` section and how you can edit and see the preview tabs update

3. add back the contacts section and see it updated in the current preview tab and spec

4. show how you can define your own linting errors with the spectral file
    - only allow camelCase for `operationId` field
    - change `operationId` for `getTransaction` to `get-transaction` instead in Insomnia design tab
    - highlight the linting error
    - change back to camelCase

5. paste in the openapi.yaml below and see the contact section updated in the preview tab

6. click generate collection in the settings and go to the collection tab to start testing APIs

7. go to cmd e and add the env vars into the collection

8. start testing your API:
    - Create new transaction - if it fails, change the id in request body to a diff value
    - Get all transactions

9. go to tests, create a new suite and run a test for List all transactions to return status = 200 OK

# References:

1. See the `./demo-scenes/resources/insomnia-env-var.json` for env vars if needed

2. See the `./demo-scenes/wrong-format-spec.yaml` file for a spec that violates spectral linting errors

