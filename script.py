import requests
from concurrent.futures import ThreadPoolExecutor

# List of server instances
server_instances = ['http://localhost:81', 'http://localhost:82', 'http://localhost:83']

# Number of requests to send to each server instance
num_requests = 100

# Function to send requests to a server instance
def send_requests(server_url):
    hits = 0
    for _ in range(num_requests):
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                hits += 1
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to {server_url}: {e}")
    return server_url, hits

if __name__ == "__main__":
    hit_counts = {}

    with ThreadPoolExecutor(max_workers=len(server_instances)) as executor:
        results = executor.map(send_requests, server_instances)

    for server_url, hits in results:
        hit_counts[server_url] = hits

    print("Hits per server instance:")
    for server_url, hits in hit_counts.items():
        print(f"{server_url}: {hits} hits")
