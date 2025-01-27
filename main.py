import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Catalin Avarvarei")
    content = """
    Senior Web Developer with 10+ years of experience specializing in designing modern, responsive, and user-friendly websites. Proficient in working with WordPress, HubSpot, and utilizing frameworks like Bootstrap and Tailwind CSS for custom designs. I have successfully delivered custom development projects and collaborated with various international and national clients/companies to achieve their digital goals.
    """
    st.info(content)