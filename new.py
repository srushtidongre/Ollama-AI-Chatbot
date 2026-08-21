# import streamlit as st
# st.title("Hello World")
# st.header("My first streamlit app")
# name = st.text_input("Enter your name")
# st.write(name)
 
# if st.button("click me"):
#     st.write("This button was Click")

# age = st.number_input("Enter your age")
# age = st.slider("Enter your age",1,100)

# course = st.selectbox("Chose your course",["JAVA","Python","CSS"])
# agree = st.checkbox("I agree")

# gender = st.radio("Choose youur gender",["Male","Female","other"]) #Radio is used to select only two options

# question=st.text_area("Enter your Question")

# upload=st.file_uploader("Upload your Resume",type = ("txt","pdf"))
# sidebar=st.sidebar.title("Sidebar")
# st.sidebar.selectbox("Chose your course",
#                     ["JAVA","Python","HTML"])
# col1, col2 = st.columns(2)
# with col1:
#     st.header("Input")
# with col2:
#     st.header("Output")

# prompt =st.chat_input("Ask me anything")
# if prompt:
#     with st.chat_message("user"):
#         st.write(prompt)
#     with st.chat_message("Assistant"):
#         st.write("This is an AI Assistance")


# 

# 

import streamlit as st
import ollama

# st.title("Chat with Ollama")

# prompt = st.text_input("Ask something:")

# if prompt:
#     response = ollama.chat(
#         model="llama3.2",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.write(response["message"]["content"])

question = st.chat_input("Ask anything?")

if question:
    with st.chat_message("user"):
        st.write(question)

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response["message"]["content"]

    with st.chat_message("assistant"):
        st.write(answer)