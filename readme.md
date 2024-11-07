# Setup
1. git clone this url on your insomnia client after creating a new project:

    ```bash
    git clone https://github.com/eugenetan01/kong-edu-insomnia.git
    ```

    - navigate to the collection tab and change the env vars (cmd-e) to use the `OpenAPI env localhost:3000` env

2. start the services:

    ```bash
    docker-compose -f ./bankong/docker/docker-compose-bankong-combined_local_portchange.yaml up -d
    ```

3. check the services are running:
    1. frontend: http://localhost:29080/
    2. backend: http://localhost:3000/transactions
