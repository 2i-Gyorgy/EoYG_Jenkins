import requests

def make_api_request(url):
    response = requests.get(url)
    return response

# Environment Agency Tide Gauge API - Station E70824 Leith
api_url = "https://environment.data.gov.uk/flood-monitoring/id/stations/E704534824/measures"

# Make API request
api_response = make_api_request(api_url)

# Check if the response is valid (you can customize this based on your API)
if api_response.status_code == 200:
    print("API request successful")
    # Add additional validation here if needed
else:
    print(f"API request failed with status code {api_response.status_code}")
    # Handle the failure accordingly

# print response
print(api_response)
