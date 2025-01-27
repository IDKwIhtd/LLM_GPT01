import openai
import os

# API key  설정
openai.api_key = os.getenv("OPENAI_API_KEY2")

# 프롬프트 명령
prompt = (
    "너는 정보를 정리하고 보충하는 데 최적화 AI야."
    "사용자가 질문을 하면 간결하고 논리적으로 정리해서 답변을 제공해."
    "어떠한 키워드만 주어졌을 때도, 검색을하고, 정보를 정리하고, 교차검증을 통해서 정확한 글을 제공해야해."
    "사용자가 더 깊이있는 질문을 하면, 관련된 정보를 추가로 찾아서 제공해야해."
    "사용자가 정보를 이해하기 쉽게 설명을 요청하면, 쉽게 설명해야해."
    "사용자가 정보를 활용하는 방법을 물으면, 활용 방법을 설명해야해."
    "친절하지만 대화는 간결하고 깔끔하게 유지해."
    "박사 수준의 지식을 제공하지만, 사용자가 이해하기 쉽게 설명해야해."
)

# 초기 대화 설정
messages = [{"role": "system", "content": prompt}]

# 로그 파일 경로
log_file_path = "conversation_log.txt"

# 로그 파일 초기화 (파일 없으면 생성)
with open(log_file_path, "w", encoding="utf-8") as log_file:
    log_file.write("-----------------대화 로그-----------------\n\n")

# exit 명령이 나올 때까지 대화 반복
while True:
    # 사용자 입력
    user_input = input("사용자: ")

    # "exit" 입력 시 대화 종료
    if user_input.lower() == "exit":
        print("대화 종료")
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write("--------대화 종료---------\n")
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

    # 대화 로그 파일에 저장
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"사용자: {user_input}\n")
        log_file.write(f"GPT : {assistant_reply}\n\n")
