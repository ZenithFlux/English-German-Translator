# English-German-Translator

Translates text from English to German.

Model used for translation: [Helsinki-NLP/opus-mt-en-de](https://huggingface.co/Helsinki-NLP/opus-mt-en-de)

# How to run

## Using Python

1. Install all dependencies.  
`pip install -r requirements.txt`

2. Run streamlit server.  
`streamlit run app.py`  

The app will be served on *localhost* where it can be used to translate text.

## Using Docker

Run the following command in terminal:  
`docker run -it --gpus all -p 5000:80 chaitanyalakhchaura12/en2ge-translator`

The app will be served on ***localhost:5000***.  
Type *localhost:5000* in your browser to view the webapp.

First launch will take some time to download the model files.