import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("マスクAI")

# ファイルアップロード
uploaded_file = st.file_uploader("Upload a txt file", type="txt")

# ChatGPTでマスキングを行う関数
def mask_with_chatgpt(text):
    prompt = (
        "Please mask all personal names and company names in the following text. "
        "Use [MASKED NAME] for personal names and [MASKED COMPANY] for company names:\n\n"
        f"{text}"
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    masked_text = completion.choices[0].message.content
    return masked_text

# ファイルの内容を表示し、マスキングを実行
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.subheader("Original Text:")
    st.text(content)

    masked_content = mask_with_chatgpt(content)
    st.subheader("Masked Text:")
    st.text(masked_content)

    # マスクされた内容をダウンロードできるようにする
    st.download_button(
        label="Download Masked Text",
        data=masked_content,
        file_name="masked_text.txt",
        mime="text/plain",
    )
