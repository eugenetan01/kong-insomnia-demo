import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables
API_BASE_URL = os.getenv("KONNECT_API_BASE_URL")
CONTROL_PLANE_ID = os.getenv("CONTROL_PLANE_ID")  # The ID of the control plane
AUTH_TOKEN = os.getenv("KONNECT_AUTH_TOKEN")

# HTTP headers
HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "accept": "*/*"
}

def delete_resources(resource_type: str) -> int:
    """
    Delete all resources of a given type (services or routes) from Konnect.
    """
    try:
        with httpx.Client() as client:
            # Fetch all resources
            endpoint = f"{API_BASE_URL}/v2/control-planes/{CONTROL_PLANE_ID}/core-entities/{resource_type}"
            response = client.get(endpoint, headers=HEADERS)
            if response.status_code != 200:
                print(f"Failed to fetch {resource_type}: {response.text}")
                return 0

            resources = response.json().get("data", [])
            deleted_count = 0

            # Delete each resource
            for resource in resources:
                resource_id = resource["id"]
                delete_response = client.delete(f"{endpoint}/{resource_id}", headers=HEADERS)
                if delete_response.status_code == 204:
                    print(f"Deleted {resource_type[:-1]} ID {resource_id}")
                    deleted_count += 1
                else:
                    print(f"Failed to delete {resource_type[:-1]} ID {resource_id}: {delete_response.text}")

            return deleted_count
    except Exception as e:
        print(f"Error during {resource_type} deletion: {e}")
        return 0

def main():
    """
    Main function to delete all services and routes.
    """
    if not API_BASE_URL or not CONTROL_PLANE_ID or not AUTH_TOKEN:
        print("Error: Missing API_BASE_URL, CONTROL_PLANE_ID, or AUTH_TOKEN in the environment.")
        return

    print("Starting cleanup process...")

    # Delete all routes
    routes_deleted = delete_resources("routes")
    print(f"Deleted {routes_deleted} routes.")

    # Delete all services
    services_deleted = delete_resources("services")
    print(f"Deleted {services_deleted} services.")

    print("Cleanup process completed.")

if __name__ == "__main__":
    main()
