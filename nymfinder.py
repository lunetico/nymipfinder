import requests

# Fetch data from the API
url = "https://explorer.nymtech.net/api/v1/tmp/unstable/nym-nodes"
response = requests.get(url)
nodes = response.json()

# Extract hostname and IP address
filtered = []
for node in nodes:
    description = node.get("description")
    if description and "host_information" in description:
        host_info = description["host_information"]
        hostname = host_info.get("hostname")
        ip_address = host_info.get("ip_address")
        filtered.append({
            "hostname": hostname,
            "ip_address": ip_address
        })

# Print header
print(f"{'Hostname':<30} {'IP Address(es)'}")
print("-" * 60)

# Print each entry in columns
for entry in filtered:
    hostname = entry["hostname"] or "None"
    ip_list = ", ".join(entry["ip_address"]) if entry["ip_address"] else "None"
    print(f"{hostname:<30} {ip_list}")
