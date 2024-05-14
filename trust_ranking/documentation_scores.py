import requests
from bs4 import BeautifulSoup
import spacy
import readability
from textstat import flesch_reading_ease
import math
# Load English language model
nlp = spacy.load("en_core_web_sm")

def normalize_score(score):
    min_score = 0  # Minimum possible score
    max_score = 100 # Maximum possible score
    
    # Normalize the score
    normalized_score = ((score - min_score) / (max_score - min_score)) * 10
    return math.ceil(normalized_score * 10) / 10

def evaluate_completeness(soup, total_number_of_endpoints):
    """
    Evaluate completeness score based on the number of endpoints in the documentation.
    """
    endpoints = soup.find_all('endpoint')
    completeness_score = len(endpoints) / total_number_of_endpoints * 10 if total_number_of_endpoints != 0 else 0
    return min(completeness_score, 10)

def evaluate_clarity(soup):
    """
    Evaluate clarity score based on the clarity and organization of documentation sections.
    """
    try:
        # Extract text from HTML elements
        text = ' '.join([element.get_text() for element in soup.find_all([
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',  'p', 'li', 'blockquote', 'pre','table', 'img','code']
        )])
        
        # Calculate Flesch-Kincaid Grade Level readability score
        clarity_score = readability.getmeasures(text, lang='en')['readability grades']['FleschReadingEase']
        clarity_score=normalize_score(clarity_score)
        return clarity_score
    
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def evaluate_organization(soup):
    """
    Evaluate organization score based on the structure and organization of documentation.
    """
    organization_score = 0
    
    if soup.find('section', {'class': 'overview'}):
        organization_score += 2
    if soup.find('section', {'class': 'endpoints'}):
        organization_score += 2
    
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    if headers:
        for header in headers:
            if header.text.strip() != '':
                organization_score += 1
    
    return min(organization_score, 10)

def evaluate_resource_availability(soup):
    """
    Evaluate resource availability score based on the availability of code examples and external links.
    """
    resource_score = 0
    
    code_blocks = soup.find_all('code')
    external_links = soup.find_all('a', href=True)
            
            # Define criteria for resource availability (example: presence of code blocks or external links)
    resource_score = 0
    if code_blocks:
        resource_score += 3
                
                # Check if code blocks contain meaningful content
        for code_block in code_blocks:
            if code_block.text.strip() != '':
                resource_score += 2
            
            # Increase score if external links are present
    if external_links:
        resource_score += 5
                
                # Check if external links lead to useful resources (e.g., tutorials, examples)
        for link in external_links:
            if 'tutorial' in link['href'] or 'example' in link['href']:
                resource_score += 2
            
    return min(resource_score, 10)

def measure_documentation_scores(api_name, documentation_url, total_number_of_endpoints):
    """
    Measure various documentation scores for the given API documentation.
    """
    try:
        response = requests.get(documentation_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # print(soup)
            completeness_score = evaluate_completeness(soup, total_number_of_endpoints)
            clarity_score = evaluate_clarity(soup)
            organization_score = evaluate_organization(soup)
            resource_score = evaluate_resource_availability(soup)
            
            return completeness_score, clarity_score, organization_score, resource_score
        else:
            print(f"Failed to fetch documentation for {api_name}")
            return None, None, None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None, None, None

# Example usage
api_name = ""
documentation_url = "https://developers.google.com/maps/documentation/"
total_number_of_endpoints = 20
completeness_score, clarity_score, organization_score, resource_score = measure_documentation_scores(api_name, documentation_url, total_number_of_endpoints)

print(f"Completeness Score: {completeness_score}")
print(f"Clarity Score: {clarity_score}")
print(f"Organization Score: {organization_score}")
print(f"Resource Availability Score: {resource_score}")
