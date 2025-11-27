import streamlit as st
import random

st.title("🔢 숫자 비교 게임 (UP / DOWN)")
st.write("내가 비밀 숫자 하나를 골라두었어. 네가 입력한 숫자와 비교해서 알려줄게!")

# 세션 상태에 비밀 숫자 저장 (1~1000)
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 1000)

# 사용자 입력 (1~1000)
user_input = st.number_input("숫자를 입력하세요:", min_value=1, max_value=1000, step=1)

# 결과 확인
if st.button("결과 확인"):
    secret = st.session_state.secret_number

    if user_input < secret:
        st.warning("🔼 **UP!** (더 큰 숫자)")
    elif user_input > secret:
        st.warning("🔽 **DOWN!** (더 작은 숫자)")
    else:
        st.success("🎉 정답!")

# 비밀 숫자 다시
