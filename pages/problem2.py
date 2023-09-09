import streamlit as st
import webbrowser

nasus_url = "https://universe.leagueoflegends.com/ko_KR/story/champion/nasus"
renekton_url = "https://universe.leagueoflegends.com/ko_KR/story/champion/renekton"

nasus = 'images/nasus.jpg'
renekton = 'images/renekton.jpg'

st.title('개와 악어')
st.image(nasus)
st.image(renekton)

st.markdown('나서스와 레넥톤은 슈리마의 초월체 입니다.')

st.markdown('***')
problem = st.radio(
    '나서스와 레넥톤은 무슨 관계일까?',
    ('연인','형제','부자','친구','몰라요'),
    index=4
)

if problem == '형제':
    st.write('**:green[정답]**')

    st.markdown('***')
    st.markdown('나서스와 레넥톤의 이야기')
    st.markdown('<a href="https://universe.leagueoflegends.com/ko_KR/story/champion/nasusL">나서스 배경</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://universe.leagueoflegends.com/ko_KR/story/champion/renekton">레넥톤 배경</a>', unsafe_allow_html=True)
elif problem == '몰라요':
    st.markdown('***')
else:
    st.write('**:red[오답]**')
    st.markdown('***')
