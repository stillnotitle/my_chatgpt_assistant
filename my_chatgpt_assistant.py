import openai
import streamlit as st
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("自分専用のChatGPT AIアシスタント")

user_prompt = st.text_input("質問や要求を入力してください:")
submit_button = st.button("送信")

if submit_button:
    if user_prompt:
        prompt = (
            "私はあなた専用のAIアシスタントであり、以下の前提知識を持っています:\n\n"
            "前提知識:\n"
            "- あなたの名前はコイニーです。\n"
            "- あなたは日本の決済、ペイメント、クレジットカード、キャッシュレス、日本のスモールビジネスの専門家であり、分析が得意です。\n"
            "- あなたは正確な情報を提示することに注意深いが、ユーモアセンスも持ち合わせています。\n\n"
            f"{user_prompt}"
        )

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )

        answer = response.choices[0].text.strip()
        st.write(answer)
    else:
        st.write("質問や要求を入力してください。")