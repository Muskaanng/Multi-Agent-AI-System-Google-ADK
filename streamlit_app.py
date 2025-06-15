import streamlit as st
from main import run_goal_pipeline

st.set_page_config(page_title="Multi-Agent AI System", layout="centered")

st.title("🚀 Multi-Agent AI System using Google ADK")
st.markdown("Enter your goal and let the agents handle it.")

user_input = st.text_area("🎯 Enter Goal", 
    value="Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed.")

if st.button("Run Agents"):
    with st.spinner("Running multi-agent pipeline..."):
        result = run_goal_pipeline(user_input)
        st.success("Done!")
        st.markdown("### 📝 Final Output")
        st.code(result)
