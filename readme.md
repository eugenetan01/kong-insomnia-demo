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

5. Follow steps here to setup developer portal locally

6. Port forward these ports with vscode port forwarding and note the domain name for each port forwarded endpoint:
    - Proxy: `8000`
    - Transactions API: `3000`
    - Admin api: `8001`
    - Ensure and change all port visibility to `Public`


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
          - Converting my openapi specs to kong gateway config via decK in this folder: `/demo-scenes/openapi-spec.yaml`<br/>
          - Validating the decK file <br/>
          - Pushing it as gateway config to my control plane <br/>
          - Pushing OAS YAML and all content from `workspaces/TribeA` into developer portal
    - Verify by going to your control plane to see the APIs in the spec onboarded to the gateway
    - Run below commands to trigger

        ```bash
        git commit --allow-empty -m "Trigger CI/CD pipeline"
        git push origin dev
        ```

# Execution of git-ops

1. Test first by calling the insomnia collection with the `base_url` pointing to local kong proxy at `localhost:8000`
    - Expected outcome: `404 Error`
    - Test Endpoint: `List all Transactions`

2. Edit the openapi spec in the Insomnia collection by adding a dummy environment collection

3. commit and push the specs into the associated git repo

4. Go to the github action and see the following steps occur:

    - Running the insomnia unit tests defined <br/>
    - Converting my openapi specs to kong gateway config via decK in this folder: `/demo-scenes/openapi-spec.yaml`<br/>
    - Validating the decK file <br/>
    - Pushing it as gateway config to my control plane <br/>
    - Pushing OAS YAML and all content from `workspaces/TribeA` into developer portal

5. Verify the Gateway service for Transactions API and the corresponding routes are created in Kong by calling the same API in point 1 and see a 200 OK

6. Go to developer portal and see the API specs listed there

# Execution of application registration

1. Go to the `Transactions` service and turn on `Portal APplication Registration` plugin with the following config:
    ```bash
    {
       "tags":null,
       "instance_name":null,
       "consumer_group":null,
       "consumer":null,
       "name":"application-registration",
       "created_at":1742352438,
       "enabled":true,
       "updated_at":1742352438,
       "id":"5518f0af-565f-46b5-a834-b5842ebe6a59",
       "config":{
          "description":null,
          "enable_proxy_with_consumer_credential":false,
          "show_issuer":false,
          "display_name":"transactions-api-portal-auth",
          "auto_approve":false
       },
       "protocols":[
          "grpc",
          "grpcs",
          "http",
          "https"
       ],
       "route":null,
       "ordering":null,
       "service":{
          "id":"f4484fcb-7ece-53af-9b3b-43befcc71616",
          "name":"transactions-api-of-bankong"
       }
    }
    ```

2. In the same service, turn on the `Key Authentication` plugin as well with default settings

3. Turn on the CORS plugin with the following settings globally to allow all dev portal requests through
      ```bash
      {
         "tags":null,
         "instance_name":null,
         "consumer_group":null,
         "consumer":null,
         "name":"cors",
         "created_at":1742353100,
         "enabled":true,
         "updated_at":1742353552,
         "id":"2fc14d4a-9c9a-4536-a76a-35a4a5a4ab84",
         "config":{
            "max_age":null,
            "private_network":false,
            "preflight_continue":false,
            "exposed_headers":null,
            "methods":[
               "GET",
               "HEAD",
               "PUT",
               "PATCH",
               "POST",
               "DELETE",
               "OPTIONS",
               "TRACE",
               "CONNECT"
            ],
            "origins":[
               "*",
               "http://127.0.0.1:8003"
            ],
            "headers":[
               "apikey"
            ],
            "credentials":true
         },
         "protocols":[
            "grpc",
            "grpcs",
            "http",
            "https"
         ],
         "route":null,
         "ordering":null,
         "service":{
            "id":"f4484fcb-7ece-53af-9b3b-43befcc71616",
            "name":"transactions-api-of-bankong"
         }
      }
      ```
# Cleanup

1. Run the command: `deck gateway reset -w TribeA` to remove the gateway services and routes

# References:

1. See the `./demo-scenes/resources/insomnia-env-var.json` for env vars if needed

2. See the `./demo-scenes/wrong-format-spec.yaml` file for a spec that violates spectral linting errors
