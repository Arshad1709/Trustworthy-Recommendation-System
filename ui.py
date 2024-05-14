import sys
import streamlit as st
import pandas as pd
sys.path.append("tools")
import Recommendation
sys.path.append("trust_ranking")
import ranking

def recommendation(input_text,choice):
    recommended_apis,recommended_categories=Recommendation.recommendation(input_text,int(choice))
    st.write(f"Top {choice} Recommended APIs with Categories")
    df=pd.DataFrame({"API":recommended_apis,'Categories':recommended_categories})
    st.table(df)
    trust_rating(recommended_apis)

def trust_rating(recommended_apis):
    ranking.api(recommended_apis)

st.title("Recommendation System")
input_text = st.text_area("Enter your website description here:")

choice = st.radio("No of Recommendations:", ("5", "10", "15", "20"),index=0, format_func=str, key=None,horizontal=True)

if st.button("Get Recommendations"):
    if input_text:
        size_inp=len(input_text.split())
        if size_inp>=10:
            recommendation(input_text,choice)
            # trust_rating()
        else:
            st.warning("Input description must be of at least 10 words")