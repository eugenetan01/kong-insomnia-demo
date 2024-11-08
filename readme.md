# Setup
1. Create a project on Insomnia and git clone this project in Insomnia

    - navigate to the collection tab and change the env vars (cmd-e) to use the `OpenAPI env localhost:3000` env

3. start the services:

    ```bash
    docker-compose -f ./docker/docker-compose-bankong-combined_local_portchange.yaml up -d
    ```

4. check the services are running:
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

10. To showcase API-Ops, make an empty commit and push to dev branch to run the github action

    ```bash
    git commit --allow-empty -m "Trigger CI/CD pipeline"
    git push origin dev
    ```

    - Show the `.github/workflows/inso-deck.yaml` that it runs on push to dev branch and PR to master
    - Show the steps in the github action:
          - running the insomnia unit tests defined
          - converting my openapi specs to kong gateway config via decK
          - validating the decK file 
          - pushing it as gateway config to my control plane
    - verify by going to your control plane to see the APIs in the spec onboarded to the gateway
      
# References:

1. See the `./demo-scenes/resources/insomnia-env-var.json` for env vars if needed

2. See the `./demo-scenes/wrong-format-spec.yaml` file for a spec that violates spectral linting errors

