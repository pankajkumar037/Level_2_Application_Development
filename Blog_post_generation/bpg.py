from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
import streamlit as st


def getmodel(api_key):
    llm = GoogleGenerativeAI(model="gemini-pro",temperature=0.3,api_key=api_key)
    return llm



template = """
Title: {topic}

Introduction:
Write an engaging introduction for a blog post on the topic: {topic}. It should provide a hook that draws the reader in and introduces the subject in some words.

Body:
- Create a few subheadings based on the main points you want to cover in the post.
- Under each subheading, provide detailed content for each section, ensuring it is informative and valuable.
- Write at least 3 sections but you can go with more with clear subheadings, covering the following aspects of the topic:
  
  
Conclusion:
Summarize the key points covered in the blog post. Provide a clear conclusion or a call to action for the reader to take after reading the article.

Formatting instructions:
- Use bullet points or numbered lists for key takeaways, if applicable.
- Use bold text for key terms and phrases.
"""

prompt=PromptTemplate(
    input_variables=["title"],
    template=template
)



st.title("Blog generation Application")

col1, col2 = st.columns([1, 3])  


with col1:
    st.header("API Key")
    api_key = st.text_input("Enter API Key", type="password")
    if api_key:
        st.success("API Key saved securely!")


with col2:
    st.header("Chat Interface")


    # Chat input
    prompts = st.chat_input("Say something")
    if prompt:
        llm=getmodel(api_key)
        chain=prompt | llm
        st.write(chain.invoke(prompts))



    



