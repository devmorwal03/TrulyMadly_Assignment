import streamlit as st
from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify

st.title("AI Ops Assistant")

query = st.text_input("Enter your request")

if st.button("Run"):
    plan = create_plan(query)
    st.subheader(" Plan")
    st.json(plan)

    results = execute_plan(plan)
    st.subheader("⚙ Execution")
    st.json(results)

    final = verify(results)
    st.subheader("✅ Final Output")
    st.json(final)