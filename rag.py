import streamlit as st
import ollama
import numpy as np

st.title("🤖 My First Ragbot")
with open("Data.txt","r") as file:
    text=file.read()
chunks=text.split("\n\n")
chunk_vectors=[]
for chunk in chunks:
    response=ollama.embed(
        model="nomic-embed-text",
        input=chunk
    )
    vector=response["embeddings"][0]
    chunk_vectors.append(vector)
question=st.chat_input("Ask something...")
if question:
    with st.chat_message("user"):
        st.write(question)
    response=ollama.embed(
        model="nomic-embed-text",
        input=question
    )
    question_vector=response["embeddings"][0]

    #similarity search 
    score=[]
    for vector in chunk_vectors:
        similarity=np.dot(question_vector,vector)/(
            np.linalg.norm(question_vector)*
            np.linalg.norm(vector)
        )
        score.append(similarity)

    #finding best chunk
    best_index=np.argmax(score)
    best_chunk=chunks[best_index]

    #create prompt
    prompt=f"""""
    Answer the question using only the context below.and
    context:
    {
        best_chunk
    }
    question:
    {
        question
    }
    """

    #Ask ollama
    response=ollama.chat(
        model="gemma",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    answer=response["message"]["content"]
    
    #Display answer
    with st.chat_message("assistant"):
        st.write(answer)