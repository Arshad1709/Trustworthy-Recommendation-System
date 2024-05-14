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
def api():
    print("API ranking")
    apis = [
        {"name": "Google-Maps", "documentation_quality": 9.2, "community_support": 8.75, "security_measures": 8.5},
        {"name": "Twitter", "documentation_quality": 8.8, "community_support": 7.75, "security_measures": 8.5},
        {"name": "Amazon-Product-Advertising", "documentation_quality": 8.2, "community_support": 8.0, "security_measures": 8.25},
        {"name": "Microsoft-Binge-Maps", "documentation_quality": 7.4, "community_support": 7.75, "security_measures": 7.75},
        {"name": "Google-App-Engine", "documentation_quality": 9.2, "community_support": 8.0, "security_measures": 8.25},
        {"name": "Twilio", "documentation_quality": 7.4, "community_support": 8.0, "security_measures": 7.25},
    ]

# Define weights for criteria
    weights = {
        "documentation_quality": 0.3,
        "community_support": 0.3,
        "security_measures": 0.4
    }

# Function to calculate overall score
    def calculate_overall_score(api):
        overall_score = 0
        for criterion, weight in weights.items():
            overall_score += api[criterion] * weight
        return overall_score

    # Calculate overall scores for each API
    for api in apis:
        api["Trust_score"] = calculate_overall_score(api)

    # Convert list of dictionaries to dataframe
    df_api_scores = pd.DataFrame(apis)

    # Rank APIs based on overall score
    ranked_apis = df_api_scores.sort_values(by="Trust_score", ascending=False)

    st.table(ranked_apis)

    # Plot player metrics radar chart for each API
    # for api in apis:
    #     plot_player_metrics(api)
    plot_api_metrics(apis)
