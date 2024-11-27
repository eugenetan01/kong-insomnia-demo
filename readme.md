# Setup
1. Create a project on Insomnia and git clone this project in Insomnia

    - navigate to the collection tab and change the env vars (cmd-e) to use the `OpenAPI env localhost:3000` env

3. Start the services:

    ```bash
    docker-compose -f ./docker/docker-compose-bankong-combined_local_portchange.yaml up -d
    ```

4. Check the services are running:
    - frontend: http://localhost:29080/
    - backend: http://localhost:3000/transactions

# Execution:

1. Go to spec tab of the cloned collection and show how you can edit the openapi specs

2. Show the linting errors by deleting the `contacts` section and how you can edit and see the preview tabs update

3. Add back the contacts section and see it updated in the current preview tab and spec

4. Show how you can define your own linting errors with the spectral file
    - Only allow camelCase for `operationId` field
    - Change `operationId` for `getTransaction` to `get-transaction` instead in Insomnia design tab
    - Highlight the linting error
    - Change back to camelCase

5. Paste in the openapi.yaml below and see the contact section updated in the preview tab

6. Click generate collection in the settings and go to the collection tab to start testing APIs

7. Go to cmd e and add the env vars into the collection

8. Start testing your API:
    - Create new transaction - if it fails, change the id in request body to a diff value
    - Get all transactions

9. Go to tests, create a new suite and run a test for List all transactions to return status = 200 OK

10. To showcase API-Ops, make an empty commit and push to dev branch to run the github action
    - Show the `.github/workflows/inso-deck.yaml` that it runs on push to dev branch and PR to master
    - Show the steps in the github action: <br/> 
          - Running the insomnia unit tests defined <br/>
          - Converting my openapi specs to kong gateway config via decK <br/>
          - Validating the decK file <br/>
          - Pushing it as gateway config to my control plane <br/>
    - Verify by going to your control plane to see the APIs in the spec onboarded to the gateway
    - Run below commands to trigger

        ```bash
        git commit --allow-empty -m "Trigger CI/CD pipeline"
        git push origin dev
        ```
# Cleanup

1. Navigate to `./cleanup/konnect` folder and create a venv for the python project

    ```python
    python3 -m venv myenv
    source myenv/bin/activate
    ```

2. Install the requirements.txt for the venv

    `pip3 install -r requirements.txt`

3. Create a .env file with the following vars:

    ```python
    KONNECT_API_BASE_URL="https://global.api.konghq.com"
    KONNECT_AUTH_TOKEN="<your-konnect-PAT>"
    CONTROL_PLANE_ID="<your-control-plane-id>"
    ```

4. Run the `python3 cleanup-konnect.py` to remove the gateway services and routes

# References:

1. See the `./demo-scenes/resources/insomnia-env-var.json` for env vars if needed

2. See the `./demo-scenes/wrong-format-spec.yaml` file for a spec that violates spectral linting errors
