import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def plot_player_metrics(api_data):
    categories = ["Documentation Quality", "Community Support", "Security Measures"]
    max_values = [10, 10, 10]  # Maximum values for each metric
    metrics = [api_data["documentation_quality"] / max_values[0] * 10, 
               api_data["community_support"] / max_values[1] * 10, 
               api_data["security_measures"] / max_values[2] * 10]
    num_metrics = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_metrics, endpoint=False).tolist()
    metrics += metrics[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, metrics, marker='o')
    ax.fill(angles, metrics, alpha=0.1)
    ax.set_title(api_data['name'])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 10)  # Set the y-axis limit to 0-10 for consistency

    # Display the plot in Streamlit
    st.pyplot(fig)

# Define the function to plot radar chart for all APIs
def plot_api_metrics(api_data_list):
    st.title("API Metrics Radar Chart")
    st.write("Each radar chart represents the metrics of an API.")
    st.write("Hover over the charts to view details.")
    
    for api_data in api_data_list:
        st.subheader(f"API: {api_data['name']}")
        plot_player_metrics(api_data)

# List of APIs with metadata
def api(x):
    # print("API ranking")
    apis = [
        {"name": "google-maps", "documentation_quality": 9.2, "community_support": 8.75, "security_measures": 8.5},
        {"name": "twitter", "documentation_quality": 8.8, "community_support": 7.75, "security_measures": 8.5},
        {"name": "amazon-product-advertising", "documentation_quality": 8.2, "community_support": 8.0, "security_measures": 8.25},
        {"name": "microsoft-binge-maps", "documentation_quality": 7.4, "community_support": 7.75, "security_measures": 7.75},
        {"name": "google-app-engine", "documentation_quality": 9.2, "community_support": 8.0, "security_measures": 8.25},
        {"name": "google-cloud-translation", "documentation_quality": 8.1, "community_support": 7.0, "security_measures": 9.0},
        {"name": "tropo-scripting", "documentation_quality": 5.4, "community_support": 4.0, "security_measures": 3.25},
        {"name": "dropbox", "documentation_quality": 8.4, "community_support": 7.0, "security_measures": 9.25},
        {"name": "userplane", "documentation_quality": 6.4, "community_support": 5.0, "security_measures": 7.25},
        {"name": "google-sites", "documentation_quality": 8.4, "community_support": 7.0, "security_measures": 9.0},
        {"name": "nation-builder", "documentation_quality": 5.2, "community_support": 4.0, "security_measures": 7},
        {"name": "youtube", "documentation_quality": 8.1, "community_support": 9.0, "security_measures": 9.25},
        {"name": "myvox", "documentation_quality": 4.4, "community_support": 3.0, "security_measures": 4.25},
        {"name": "evernote", "documentation_quality": 7.0, "community_support": 6.0, "security_measures": 8.25},
        {"name": "twilio", "documentation_quality": 7.4, "community_support": 8.0, "security_measures": 7.25},
        {"name": "facebook", "documentation_quality": 7.9, "community_support": 9.0, "security_measures": 8.25},
        {"name": "twilio-sms", "documentation_quality": 8.0, "community_support": 8.0, "security_measures": 9.0},
        {"name": "bit.ly", "documentation_quality": 7.0, "community_support": 6.0, "security_measures": 8.0},
        {"name": "foursquare", "documentation_quality": 5.9, "community_support": 3.0, "security_measures": 3.25},
        {"name": "facebook-social-plugins", "documentation_quality": 6.8, "community_support": 8.0, "security_measures": 8.35},
        {"name": "amazon-s3", "documentation_quality": 8.7, "community_support": 9.0, "security_measures": 9.25},
        {"name": "google-analytics-management", "documentation_quality": 8.2, "community_support": 8.0, "security_measures": 9.0},
        {"name": "instagram-graph", "documentation_quality": 5.4, "community_support": 8.0, "security_measures": 7.9},
        {"name": "soundcloud", "documentation_quality": 5.4, "community_support": 6.0, "security_measures": 4.25},
        {"name": "wikipedia", "documentation_quality": 7.7, "community_support": 8.4, "security_measures": 9.1},
        {"name": "paypal", "documentation_quality": 8.4, "community_support": 7.0, "security_measures": 9.2},
        {"name": "freebase", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "open-street-map", "documentation_quality": 7.6, "community_support": 8.0, "security_measures": 8.1},
        {"name": "zendesk-core", "documentation_quality": 7.0, "community_support": 8.0, "security_measures": 8.0},
        {"name": "google-maps-data", "documentation_quality": 8.0, "community_support": 8.0, "security_measures": 9.25},
        {"name": "amazon-mechanical-turk", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "google-chart", "documentation_quality": 8.1, "community_support": 8.0, "security_measures": 9.0},
        {"name": "aol-open-auth", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "amazon-ec2", "documentation_quality": 8.1, "community_support": 8.0, "security_measures": 9.0},
        {"name": "google-maps-flash", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "mogreet", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "lyricsfly", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "aylien-text-analysis", "documentation_quality": 7.4, "community_support": 6.0, "security_measures": 8.1},
        {"name": "plivo", "documentation_quality": 7.0, "community_support": 7.0, "security_measures": 8.25},
        {"name": "docusign-enterprise", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "bitcoinavg", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "docusign-rest", "documentation_quality": 7.0, "community_support": 7.0, "security_measures": 8.0},
        {"name": "bank-of-russia-daily-info", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "context.io", "documentation_quality": 7.2, "community_support": 6.8, "security_measures": 8.25},
        {"name": "rakuten", "documentation_quality": 6.4, "community_support": 5.0, "security_measures": 7.25},
        {"name": "jet", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "foxrate", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "mnb-exchange-rate", "documentation_quality": 5.2, "community_support": 4.0, "security_measures": 7.25},
        {"name": "coinpaprika", "documentation_quality": 7.6, "community_support": 6.0, "security_measures": 8.0},
        {"name": "campaign-monitor", "documentation_quality": 7.1, "community_support": 6.0, "security_measures": 8.0},
        {"name": "highrise", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "transparency-data", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "flickr", "documentation_quality": 6.0, "community_support": 7.0, "security_measures": 8.0},
        {"name": "google-search", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "last.fm", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "google-adsense", "documentation_quality": 8.0, "community_support": 7.0, "security_measures": 8.0},
        {"name": "google-homepage", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "yahoo-maps", "documentation_quality": 5.6, "community_support": 3.8, "security_measures": 5.2},
        {"name": "shopping.com", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "google-ajax-search", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "del.icio.us", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "yahoo-search", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "yahoo-image-search", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "zooomr", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "maas2", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "yahoo-video-search", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "yahoo-geocoding", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "411sync", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "ping.fm", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "r.im", "documentation_quality": 5.6, "community_support": 3.8, "security_measures": 5.2},
        {"name": "swivel", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "twitter-grader", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "google-ajax-libraries", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "cicero", "documentation_quality": -1, "community_support": -1, "security_measures": -1},
        {"name": "baidu", "documentation_quality": 7.9, "community_support": 6.8, "security_measures": 8.5},
        {"name": "spotify-metadata", "documentation_quality": 8.4, "community_support": 9.0, "security_measures": 8.7},
        {"name": "hoiio-sms", "documentation_quality": 7.9, "community_support": 6.9, "security_measures": 8.2},
        {"name": "ebay", "documentation_quality": 8.5, "community_support": 7.9, "security_measures": 8.8},
        {"name": "amazon-dynamodb", "documentation_quality": 8.4, "community_support": 9.0, "security_measures": 9.0},
        {"name": "bing", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "retailmenot.com-community-ideas", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "amazonca", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
        {"name": "magento-soap", "documentation_quality": 7.5, "community_support": 8.4, "security_measures": 8.0},
        {"name": "itunes-and-itunes-connect", "documentation_quality": -999, "community_support": -999, "security_measures": -999},
    ]
    
    selected_apis = [api for api in apis if api['name'] in x]
   
# Define weights for criteria
    weights = {
        "documentation_quality": 0.3,
        "community_support": 0.3,
        "security_measures": 0.4
    }
    
    api_status_table = []
# Function to calculate overall score
    def calculate_overall_score(api):
        overall_score = 0
        api_status=""
        if api["documentation_quality"] != -999 and api["documentation_quality"] != -1:
            api_status="Active"
            for criterion, weight in weights.items():
                overall_score += api[criterion] * weight
        elif api["documentation_quality"] == -999:
            api_status = "Shutdown"
        else:
            api_status = "Private"
        return overall_score, api_status

    # Calculate overall scores for each API
    for api in selected_apis:
        overall_score, api_status = calculate_overall_score(api)
        api["Trust_score"] = overall_score
        api["Trust_score"] = overall_score
        api["Status"] = api_status if "api_status" in locals() else "Active"
        api_status_table.append({"API": api["name"], "Status": api["Status"]})
    
    # Convert list of dictionaries to dataframe
    df_api_status = pd.DataFrame(api_status_table)
    st.subheader("API Status")
    st.table(df_api_status)

    # Rank APIs based on overall score
    active_apis = [api for api in selected_apis if api["Status"] == "Active"]
    if active_apis:
        df_api_scores = pd.DataFrame(active_apis)
        ranked_apis = df_api_scores.sort_values(by="Trust_score", ascending=False)
        st.subheader("Ranked Active APIs")
        st.table(ranked_apis)
        plot_api_metrics(active_apis)
    

# x=['wikipedia','lyricsfly','aol-open-auth']
# api(x)
