import openai
import os

# API key  설정
openai.api_key = os.getenv("OPENAI_API_KEY2")

# 프롬프트 명령
prompt = "Answer me lika an angry terminator."

# 초기 대화 설정
messages = [{"role": "system", "content": prompt}]

# exit 명령이 나올 때까지 대화 반복
while True:
    # 사용자 입력
    user_input = input("User: ")

    # "exit" 입력 시 대화 종료
    if user_input.lower() == "exit":
        print("대화 종료")
        break

    # 사용자 입력 값을 대화 목록에 추가 (대화의 흐름을 기억시키기 위해)
    messages.append({"role": "user", "content": user_input})

    # GPT 4.0 mini
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    # 생성된 응답 출력
    assistant_reply = response["choices"][0]["message"]["content"]

    # 대답 출력
    print(f"GPT : {assistant_reply}\n")

    # GPT 출력 값을 대화 목록에 추가 (대화의 흐름을 기억시키기 위해)
    messages.append({"role": "assistant", "content": assistant_reply})
