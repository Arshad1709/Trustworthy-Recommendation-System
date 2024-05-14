import requests
from bs4 import BeautifulSoup

def scrape_community_metrics(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract community metrics (example)
            members_count_elem = soup.find('span', class_='user')
            responsiveness_elem = soup.find('span', class_='responsiveness')
            activity_elem = soup.find('span', class_='activity')
            engagement_elem = soup.find('span', class_='engagement')
            print(members_count_elem,responsiveness_elem,activity_elem,engagement_elem)

            if members_count_elem and responsiveness_elem and activity_elem and engagement_elem:
                members_count = int(members_count_elem.text)
                responsiveness_score = float(responsiveness_elem.text)
                activity_score = float(activity_elem.text)
                engagement_score = float(engagement_elem.text)
                
                return {
                    'members_count': members_count,
                    'responsiveness_score': responsiveness_score,
                    'activity_score': activity_score,
                    'engagement_score': engagement_score
                }
            else:
                print("Failed to find one or more community metrics elements.")
                return None
        else:
            print(f"Failed to fetch community metrics from {url}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
api_community_url = "https://customers.twilio.com/en-us/community"
community_data = scrape_community_metrics(api_community_url)
# if community_data:
#     community_score = calculate_community_score(community_data)
#     print(f"Community Score: {community_score}")