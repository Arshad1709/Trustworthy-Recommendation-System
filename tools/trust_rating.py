import requests
from bs4 import BeautifulSoup
import re

def search_api_documentation(api_name):
    search_url = f"https://github.com/Yesware/pubnub-javascript"
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all links pointing to markdown files
        markdown_links = soup.find_all('a', href=re.compile(r'\.md$'))
        for link in markdown_links:
            # Get the URL of the markdown file
            markdown_url = link.get('href')
            # Fetch the content of the markdown file
            markdown_response = requests.get(markdown_url)
            if markdown_response.status_code == 200:
                markdown_content = markdown_response.text
                # Check if the API name appears in the markdown content
                if api_name.lower() in markdown_content.lower():
                    return markdown_url
    return None

def calculate_trustworthiness(api_details):
    # Initialize trustworthiness score
    trustworthiness_score = 0
    
    # Check documentation quality
    if 'description' in api_details and len(api_details['description']) > 50:  # Example threshold for documentation length
        trustworthiness_score += 1
    
    # Check for community support
    if 'community' in api_details and api_details['community'].lower() == 'active':
        trustworthiness_score += 1
    
    # Check for security measures (e.g., SSL encryption)
    if 'security' in api_details and 'SSL' in api_details['security']:
        trustworthiness_score += 1
    
    # Check for reliability (e.g., uptime/downtime history)
    if 'reliability' in api_details and api_details['reliability'] == 'High':
        trustworthiness_score += 1
    
    return trustworthiness_score

def get_api_details(api_name):
    api_url = search_api_documentation(api_name)
    if api_url:
        response = requests.get(api_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Simulated extraction of details
            api_description = "This is a description of the API."
            api_usage = "api.get('data')"
            api_details = {
                'name': api_name,
                'description': api_description,
                'usage': api_usage,
            }
            api_details['trustworthiness_score'] = calculate_trustworthiness(api_details)
            return api_details
        else:
            print(f"Failed to fetch documentation page for API: {api_name}")
    else:
        print(f"No documentation found for API: {api_name}")
    return None

# Example usage:
api_name = "concur"
api_details = get_api_details(api_name)
if api_details:
    print("API Details:")
    print(api_details)
else:
    print(f"Unable to retrieve details for API: {api_name}")
