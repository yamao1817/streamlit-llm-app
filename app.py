from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 質問文（input_message）とモード（selected_item）を受け取り、LLMの回答を返す関数
def get_llm_response(input_message, selected_item):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    if selected_item == "睡眠アドバイス":
        system_content = "You are a helpful assistant. You answer questions about sleep based on scientific knowledge."
    elif selected_item == "運動アドバイス":
        system_content = "You are a helpful assistant. You answer questions about exercise based on expert knowledge."
    else:
        system_content = "You are a helpful assistant."
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_message),
    ]
    result = llm(messages)
    return result.content

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

st.title("睡眠×運動ナビ")

st.write("##### 動作モード1: 睡眠アドバイス")

st.write("睡眠に関する質問を入力すると、LLMが科学的知見に基づいて回答を返します。快眠のための生活習慣や環境改善のヒントを得られます。")

st.write("##### 動作モード2: 運動アドバイス")

st.write("運動に関する質問を入力すると、LLMが専門的知識をもとに回答を返します。健康維持や体力向上のための運動方法や注意点を確認できます。")

selected_item = st.radio(

    "動作モードを選択してください。",

    ["睡眠アドバイス", "運動アドバイス"]

)

st.divider()

if selected_item == "睡眠アドバイス":
    input_message = st.text_input(label="睡眠に関する質問を入力してください。")
elif selected_item == "運動アドバイス":
    input_message = st.text_input(label="運動に関する質問を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "睡眠アドバイス":
        if input_message:
                response = get_llm_response(input_message, selected_item)
                st.write(f"LLMの回答: {response}")

        else:
            st.error("睡眠に関する質問を入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
                response = get_llm_response(input_message, selected_item)
                st.write(f"LLMの回答: {response}")

        else:
            st.error("運動に関する質問を入力してから「実行」ボタンを押してください。")