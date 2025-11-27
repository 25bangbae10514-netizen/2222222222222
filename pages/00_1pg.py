import streamlit as st
import random

st.title("🎲 숫자 야구 게임 (5자리 버전)")
st.write("5자리 숫자를 맞춰보세요! 각 자리는 서로 다른 숫자여야 합니다.")

# 정답 생성 함수
def generate_answer():
    digits = list(range(0, 10))
    random.shuffle(digits)
    # 맨 앞자리가 0이 되지 않도록 처리
    if digits[0] == 0:
        for i in range(1, 10):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
    return digits[:5]

# 정답 저장
if "answer" not in st.session_state:
    st.session_state.answer = generate_answer()

# 스트라이크/볼 계산
def check_guess(guess, answer):
    strike = 0
    ball = 0
    for i in range(5):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    return strike, ball

# 사용자 입력
user_input = st.text_input("5자리 숫자를 입력하세요 (예: 12345)")

# 기록 저장용
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("확인"):
    if len(user_input) != 5 or not user_input.isdigit():
        st.error("⚠️ 5자리 숫자만 입력하세요.")
    elif len(set(user_input)) != 5:
        st.error("⚠️ 모든 자리는 서로 다른 숫자여야 합니다.")
    elif user_input[0] == "0":
        st.error("⚠️ 첫 숫자는 0이 될 수 없습니다.")
    else:
        guess = [int(d) for d in user_input]
        answer = st.session_state.answer
        strike, ball = check_guess(guess, answer)

        # 기록 저장
        st.session_state.history.append(
            {"guess": user_input, "strike": strike, "ball": ball}
        )

        st.write(f"👉 **{strike} 스트라이크, {ball} 볼**")

        if strike == 5:
            st.success("🎉 정답입니다! 게임 종료!")
            st.balloons()

# 기록 출력
st.subheader("📜 시도 기록")
for item in st.session_state.history[::-1]:
    st.write(f"입력: {item['guess']} → {item['strike']}S {item['ball']}B")

# 게임 리셋 버튼
if st.button("게임 다시 시작"):
    st.session_state.answer = generate_answer()
    st.session_state.history = []
    st.warning("🔄 새로운 게임이 시작되었습니다!")
