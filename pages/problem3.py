import streamlit as st
import webbrowser

kaisa_url = "https://universe.leagueoflegends.com/ko_KR/story/champion/kaisa"
kaisa_url2 = "https://universe.leagueoflegends.com/ko_KR/story/champion/kaisa"
#kassadin_url =
#velkoz_url =
#belveth_url =
malzahar_url = "https://universe.leagueoflegends.com/ko_KR/story/champion/malzahar"

kaisa = 'images/kaisa.jpg'
kassadin = 'images/kassadin.jpg'
velkoz = 'images/velkoz.jpg'
belveth = 'images/belveth.jpg'
malzahar = "images/malzahar.jpg"

st.title('공허의 딸')
st.image(kaisa)

st.markdown('카이사는 어린나이에 불과했을때 공허로 끌려들어갔다.'
            '불굴의 의지와 집요한 노력 끝에 간신히 살아남을 수 있었다.'
            '이때의 경험으로 카이사는 치명적인 위력의 사냥꾼이 되었다.')

st.markdown('***')
problem = st.radio(
    '카이사를 공허에 빠뜨린 챔피언은 누구일까?',
    ('카사딘','벨코즈','벨베스','말자하','몰라요'),
    index=4
)
if problem == '말자하':
    st.write('**:green[정답]**')
    st.image(malzahar)
    st.markdown('말자하는 한때 잘나가는 예언가였다.'
                '하지만 자신의 삶을 예언할 수 없다는 것을 느끼고 방랑한다.'
                '말자하는 공허에서 끝을 보았고, 공허의 뜻을 따르기로 한다.')
    st.markdown('말자하 배경 이야기')
    kaisa_button = st.button('**말자하 소설 읽기**', type="primary")
    if kaisa_button:
        webbrowser.open_new_tab(kaisa_url)
    st.markdown('카이사 배경 이야기')
    kaisa_button = st.button('**카이사 소설 읽기**', type="primary")
    if kaisa_button:
        webbrowser.open_new_tab(kaisa_url)
else:
    if problem!='몰라요':
        st.write('**:red[오답]**')

if problem == '카사딘':
    st.image(kassadin)
    st.markdown('카사딘은 카이사의 아버지다.')
if problem == '벨코즈':
    st.image(velkoz)
    st.markdown('벨코즈는 지능이 높은 공허 태생이다.')
if problem == '벨베스':
    st.image(belveth)
    st.markdown('벨베스는 연보라빛 바다의 여왕이다.')
st.markdown('***')

problem2 = st.radio(
    '카이사와 친구가 된 사람은 누구일까?',
    ('탈리야','시비르','아무무','이즈리얼','몰라요'),
    index=4
)
if problem2 == '탈리야':
    st.write('**:green[정답]**')

    st.markdown('카이사 단편 소설')
    kaisa_button2 = st.button('**틈으로 엮인 인연**', type="primary")
    if kaisa_button2:
        webbrowser.open_new_tab(kaisa_url2)
    st.markdown('***')
elif problem2 == '몰라요':
    st.markdown('***')
else:
    st.write('**:red[오답]**')
    st.markdown('***')
