import streamlit as st
import webbrowser

#url = ""
#webbrowser.open_new_tab(url)

potion = 'images/potion.png'

st.title('체력물약')
st.image(potion)

st.markdown('체력 물약은 사용시 15초에 걸쳐 120의 체력을 회복합니다.'
            ' 개당 가격은 50골드이며, 상황은 다음과 같습니다.')

st.markdown('**아 우리 서폿 왜 5포션 시작이냐? :blue[x]초 동안 :blue[y]의 체력을 회복하는건 너무 비효율적인거 아님?**')

problem = st.number_input(
    '이 때의 :blue[x+y]값을 구하시오.', min_value=0,
    max_value=100000,
    value=0,
    step=1)

submit_button = st.button('**submit**',type="primary")
if submit_button:
    if problem == 675:
        st.write('**:green[정답]**')
        st.balloons()
    else:
        st.write('**:red[오답]**')

