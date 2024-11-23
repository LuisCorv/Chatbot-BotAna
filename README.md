# Chatbot BotAna


## Setup and Installation

Follow these steps to set up the project and run the chatbot interface:

### 1. Clone the repository
If you haven't already, clone the repository where this code is stored:
```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Set up a virtual environment
It's recommended to use a virtual environment to manage dependencies. You can create one using `venv` or `conda`.

#### Using `venv` (Python's built-in option):
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### 3. Install required packages
With your virtual environment activated, install the necessary Python packages:

``` bash
pip install -r requirements.txt
```
Alternatively, you can manually install the required packages using:

``` bash
pip install streamlit transformers torch python-dotenv
```

### 4. Download the model

Make sure you have the model files (`model.safetensor` and `config.json`) in a directory called model/. This is the directory the app will load the model from. You have to place the model files there or download a pre-trained model from Hugging Face and save it in this folder.

In our case, you must download the` model.safetensor`, `config.json` and `generation_config.json` from the model folder found in the inform of this proyect (`GPT2-small-spanish`).

### 5. Run the Streamlit app
Once everything is set up, run the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will start the app, and it should automatically open in your browser (typically at http://localhost:8501).

## Prompts

To interact with the chatbot, you can ask questions. The chatbot is designed to understand Spanish culinary-related queries, such as recipes or cooking instructions.

Here are some example prompts you can try:

- **¿Cómo se hace una arepa de queso?**  

- **Cómo se hace un pescado al horno**  

The chatbot will generate a responses based on the provided prompt. Please note that the time taken to generate a response might be longer, as the model processes the input and generates the text. During this process, a loading animation will be displayed at the top right of the page. Once the response is ready, it will be displayed in the chat interface.




## Streamlit
[Streamlit](https://streamlit.io/)  is used to create a user-friendly web interface for the chatbot.