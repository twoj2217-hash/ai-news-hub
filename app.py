import streamlit as st
import pandas as pd
from datetime import datetime

# --- [강 수석의 잔소리] ---
# 대표님, 지금은 DB 연결도 사치입니다. 
# 일단 변수에 데이터를 때려 박아서 화면부터 띄우십시오. 
# 나중에 이 부분을 Google Sheets 연동으로 바꾸면 끝입니다.
# -------------------------

# 페이지 설정 (기본 세팅)
st.set_page_config(
    page_title="AI 뉴스 브리핑 (Ver. Zero-Cost)",
    page_icon="🚀",
    layout="wide"
)

# 사이드바: 구독 및 설정
with st.sidebar:
    st.header("⚙️ 설정")
    st.write("현재 버전: **MVP 1.0**")
    st.info("비용 발생: 0원")
    
    st.divider()
    
    st.subheader("📬 뉴스레터 구독")
    email = st.text_input("이메일 주소", placeholder="ceo@zerocost.com")
    if st.button("무료 구독하기"):
        if email:
            st.success(f"{email}님, 돈 안 드는 정보만 보내드립니다!")
        else:
            st.warning("이메일을 입력하세요.")

# 메인 헤더
st.title("🚀 AI 트렌드 & 인사이트 허브")
st.caption("강 수석이 엄선한 최신 AI 소식 (Powered by Gemini & Streamlit)")

st.divider()

# 탭 구성: 뉴스 vs 팁
tab1, tab2 = st.tabs(["🔥 최신 동향 (News)", "💡 실전 꿀팁 (How-to)"])

# --- 데이터 (대표님 파일에서 추출한 실제 내용) ---
news_data = [
    {
        "date": "2026-02-06",
        [cite_start]"title": "Anthropic, Opus 4.6 및 'Agent Teams' 출시 [cite: 193]",
        "summary": "Anthropic이 새로운 플래그십 모델 Opus 4.6을 공개했습니다. [cite_start]'Agent Teams' 기능을 통해 큰 작업을 쪼개서 병렬로 처리할 수 있으며, 100만 토큰의 컨텍스트 윈도우를 제공합니다. [cite: 193, 194, 195]",
        "tag": "모델 업데이트",
        "impact": "⭐️⭐️⭐️⭐️⭐️ (복잡한 코딩 업무 자동화 가능)"
    },
    {
        "date": "2026-02-06",
        [cite_start]"title": "NASA, 달 탐사에 아이폰 허용 [cite: 207]",
        "summary": "NASA가 방침을 변경하여 Artemis 우주비행사들이 아이폰을 달에 가져가는 것을 허용했습니다. [cite_start]우주 기술의 상용 제품 도입이 가속화되고 있습니다. [cite: 207]",
        "tag": "Tech 일반",
        "impact": "⭐️⭐️"
    },
    {
        "date": "2026-02-04",
        [cite_start]"title": "Gemini 1월 업데이트: 개인 지능(Personal Intelligence) 통합 [cite: 491, 498]",
        "summary": "구글이 Gemini에 Gmail, Photos 등을 연동하는 'Personal Intelligence'를 베타로 출시했습니다. [cite_start]또한 학생들을 위해 SAT 모의고사 기능을 무료로 제공합니다. [cite: 492, 498, 500]",
        "tag": "Google 생태계",
        "impact": "⭐️⭐️⭐️⭐️ (업무 자동화 연결성 강화)"
    },
    {
        "date": "2026-02-06",
        [cite_start]"title": "슈퍼볼 광고를 장악한 AI [cite: 731]",
        "summary": "이번 슈퍼볼 LX에서 AI 관련 광고가 메인을 차지했습니다. [cite_start]대중의 관심이 AI로 완전히 넘어갔음을 시사합니다. [cite: 731]",
        "tag": "마케팅",
        "impact": "⭐️⭐️⭐️"
    }
]

tip_data = [
    {
        "tool": "Claude x Excel",
        [cite_start]"title": "엑셀에서 Claude로 데이터 정제하기 [cite: 822]",
        "content": "지저분한 사용자 데이터(대소문자 혼용, 날짜 형식 엉망 등)를 Claude에게 프롬프트 한 번으로 정리가 가능합니다. [cite_start]'프리미엄/무료 대소문자 통일해줘'라고 하면 알아서 고쳐줍니다. [cite: 822, 824]",
        "difficulty": "하"
    },
    {
        "tool": "Claude x Excel",
        [cite_start]"title": "복잡한 수식 역설계 및 설명 듣기 [cite: 825]",
        "content": "이해하기 힘든 엑셀 수식이 있다면, Claude에게 'E4 셀의 수식이 뭘 계산하는지 설명해줘'라고 물어보세요. [cite_start]30분 걸릴 분석을 30초 만에 끝냅니다. [cite: 826]",
        "difficulty": "중"
    }
]

# 탭 1: 뉴스 렌더링
with tab1:
    for news in news_data:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(f"{news['title']}")
                st.write(news['summary'])
            with col2:
                st.caption(f"📅 {news['date']}")
                st.badge(news['tag'])
                st.write(f"파급력: {news['impact']}")
            st.divider()

# 탭 2: 꿀팁 렌더링
with tab2:
    st.write("### 🚀 실무에서 바로 쓰는 AI 활용법")
    for tip in tip_data:
        with st.expander(f"[{tip['tool']}] {tip['title']}"):
            st.write(tip['content'])
            st.info(f"난이도: {tip['difficulty']}")

# 푸터
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: grey;'>
        Created by <b>Chief Kang (Ver. Zero-Cost)</b> | 서버비 0원 프로젝트
    </div>
    """, 
    unsafe_allow_html=True
)
