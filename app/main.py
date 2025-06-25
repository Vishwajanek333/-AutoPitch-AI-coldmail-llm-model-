import streamlit as st
from langchain.chains.natbot.crawler import Crawler
from langchain_community.document_loaders import WebBaseLoader

from chain import Chain
from portfolio import portfolio
from utils import clean_text


def create_streamlit_app(llm,portfolio,clean_text):
    st.title(" cold-email generator")
    url_input = st.text_input("Enter the URL ", value="https://juspay.io/careers/sde-systems")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                # Change from job('skills',[]) to job.get('skills',[])
                skills = job.get('skills',[])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job,links)
                st.code(email,language='markdown')
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    chain = Chain()
    portfolio = portfolio()
    st.set_page_config(layout="wide",page_title="Cold Email Generator",page_icon="📧")
    create_streamlit_app(chain,portfolio,clean_text)


