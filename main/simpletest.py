import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY1")

# 대화형 모델을 사용하여 응답 생성
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a teacher.",
        },  # 프롬프트 명령
        {"role": "user", "content": "귀찮아"},  # 사용자 입력
    ],
)

# 생성된 응답 출력
print(response["choices"][0]["message"]["content"])
