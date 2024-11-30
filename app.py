import streamlit as st
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

load_dotenv()

st.title("BotAna Chatbot")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"


MODEL_PATH = "model"  

@st.cache_resource
def load_model_and_tokenizer():
    # Load the model and tokenizer from the directory containing model.safetensor and config.json
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True)
    return tokenizer, model

tokenizer, model = load_model_and_tokenizer()

def format_the_response(text):
    instruction,bot_response = text.split("### Respuesta:")
    
    return instruction + "\n" + bot_response

# Generate response from the model
def generate_response(prompt, tokenizer, model):
    # Add special token for GPT-2 models
    prompt = f"{prompt}<|endoftext|>"
    
    # Tokenize input with attention mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Generate response with stricter sampling
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=512,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9
    )
    
    # Decode and return response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("How can I help?"):

    # Display user input
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    # Generate response and update chat history
    response = generate_response(prompt, tokenizer, model)

    response = format_the_response(response)

    # Display model's response
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        message_placeholder.markdown(response)



    

