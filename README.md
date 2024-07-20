# mask-ai
A sample test AI tool for data masking and anonymization.

## Environment Setup

> conda create -n mask-ai python=3.11  
> pip install openai==1.35.10  
> pip install streamlit==1.36.0  

## OpenAI API Key

Create a secrets.toml file in the .streamlit folder and add the following code:

> OPENAI_API_KEY = "xxxxxxxx"  

## Execution

> conda activate code-assistant  
> streamlit run main.py  
