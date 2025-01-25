import streamlit as st
from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("MIRA_API_KEY")

# Initialize Mira client
client = MiraClient(config={"API_KEY": api_key})

# Initialize the flow
flow = Flow(source="./flows/project-idea-generation-flow.yaml")

# Streamlit App UI
st.set_page_config(page_title="Project Idea Generator", layout="wide")
st.title("🚀 Project Idea Generation")

# Description
st.write(
    """
    Welcome to the **Project Idea Generator**! 🎯
    
    This app helps you generate unique and innovative project ideas for your hackathon or personal projects.
    Just provide some details about your industry, preferred technology, and project scale, and we'll suggest tailored ideas for you. 💡
    """
)

# Input fields for user to define project
st.write("### 📋 Enter Your Project Details")

industry = st.text_input("Industry", "Healthcare")
technology_preference = st.text_input("Technology Preference", "AI")
prize_sponsors = st.text_area("Prize Sponsors (Optional)", "Google Cloud")
project_scale = st.selectbox("Project Scale", ["Solo", "Team", "Large Scale"])
objective = st.text_area("Hackathon Objective", "Problem-solving")
deadline = st.text_input("Deadline", "2 days")

# Create dictionary with input data
input_dict = {
    "industry": industry,
    "technology_preference": technology_preference,
    "prize_sponsors": prize_sponsors,
    "project_scale": project_scale,
    "objective": objective,
    "deadline": deadline,
}

# Action button to generate ideas
st.write("---")
if st.button("💥 Generate Ideas"):
    with st.spinner("Generating creative project ideas..."):
        try:
            # Run the flow with user inputs
            response = client.flow.test(flow, input_dict)
            
            # Display the response if successful
            st.success("🎉 Project Ideas Generated Successfully!")
            st.subheader("Suggested Project Ideas 💡")
            st.markdown(response)
            
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
