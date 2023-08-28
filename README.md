# English-German-Translator

A streamlit application which translates text from English to German using Transformers.  
Click the link below to go to the live site.

**Go to site: https://en2ge-translator.streamlit.app/**

Model used for translation: [Helsinki-NLP/opus-mt-en-de](https://huggingface.co/Helsinki-NLP/opus-mt-en-de)

This application was deployed on **AWS Elastic Container Service**.  
The AWS service is currently *disabled*.

<details>
<summary>View Screenshots</summary>
<img src="https://i.ibb.co/9ZQLy0Z/ecs.png" title="Elastic Container Service">

<br />
<img src="https://i.ibb.co/p08dxnz/site.png" title="WebApp">
</details>

# How to run locally

## Using Python

1. Clone this repository and move into the folder.  
```bash
git clone https://github.com/ZenithFlux/English-German-Translator.git  
cd English-German-Translator
```

2. Install all dependencies.  
`pip install -r requirements.txt`

3. Run streamlit server.  
`streamlit run app.py`  

The app will be served on *localhost* where it can be used to translate text.

## Using Docker

If you have docker installed, just run the following command in terminal:  

```bash
docker run -it --gpus all -p 5000:80 chaitanyalakhchaura12/en2ge-translator
```

The app will be served on ***localhost:5000***.  
Type *localhost:5000* in your browser to view the webapp.

First launch will take some time to download the model files.