import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="장민성 자기소개서",
    layout="wide"
)

# ===== 사이드바 =====
st.sidebar.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg", width=100)
st.sidebar.title("👤 장민성 자기소개")
st.sidebar.markdown("---")

# 기본 정보
st.sidebar.subheader("📌 기본 정보")
st.sidebar.markdown("""
- **이름:** 장민성  
- **생일:** 2002년 11월 13일  
- **나이:** 24세  
- **성별:** 남자
""")

# 좋아하는 것
st.sidebar.subheader("🍴 좋아하는 것")
st.sidebar.markdown("- 라면\n- 돈가스\n- 제육\n- 쇼츠보기")

# 학력 정보
st.sidebar.subheader("🎓 학력")
st.sidebar.markdown("""
- 천안부성초등학교 (졸업)  
- 천안성성중학교 (졸업)  
- 천안두정고등학교 (졸업)  
- 건양대학교 재난안전소방학과 (재학 중)
""")

# ===== 본문 =====
st.title("📝 장민성 자기소개서")
st.markdown("### 건양대학교 재난안전소방학과")

st.markdown("저는 **재난안전소방 분야의 전문가**를 목표로 다양한 특성화 교육을 이수하고 있습니다.")

# 학과 인재상
st.subheader("🔥 학과 인재상")
st.markdown("""
> **BIM기반 재난안전소방 전문가**  
> 실용위주의 소방기술과 지식을 체계적이고 전문화된 교육 시스템을 통해  
> 미래가치를 창출하는 창의적 소방인재
""")

# 특성화 교육
st.subheader("📚 학과 특성화 교육")

# 소방 특성화
with st.expander("🚒 소방 특성화 교육"):
    st.write("화재 및 재난으로부터 인간의 생명과 재산을 보호하기 위한 전문 교육")
    st.markdown("""
    **주요 교과목:**  
    - 소방학개론  
    - 소방행정학  
    - 소방관계법규  
    - 소방설비공학(전기, 기계)
    """)

# 재난안전 특성화
with st.expander("⚠️ 재난안전 특성화 교육"):
    st.write("태풍, 지진 등 자연재해 및 재난으로부터 국민과 지역주민의 안전을 담보하는 방재교육")
    st.markdown("""
    **주요 교과목:**  
    - 방재학개론  
    - 재난관리론  
    - 산업안전공학
    """)

# BIM 특성화
with st.expander("🏗️ BIM 특성화 교육"):
    st.write("구조물의 기획, 설계, 시공에 이르는 통합설계프로세스 교육")
    st.markdown("""
    **주요 교과목:**  
    - Auto CAD  
    - BIM 개론  
    - Revit Architecture & MEP  
    """)

# 교육 목표
st.subheader("🎯 교육 목표")
st.markdown("""
- 재난극복기술을 중심으로 미래가치를 창출하는 창의적 인재 양성  
- 인문융합 역량을 갖춘 안전한 사회 구현을 위한 재난안전소방 공무원 양성  
- 공학적 리더십과 창의력을 갖춘 BIM 기반 재난안전소방 설계 전문가 양성
""")

import streamlit as st

# 사이드바
st.sidebar.title("장민성 자기소개서")
st.sidebar.markdown("📌 **항목 선택**")
section = st.sidebar.radio(
    "내용 보기",
    ["자격증 로드맵", "취득 목표 및 기대효과"]
)

# 본문
st.title("📘 자격증 취득 계획")
st.markdown("##### 재난안전 분야의 전문성 강화를 위한 자격증 로드맵")

if section == "자격증 로드맵":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔥 소방 분야")
        st.markdown("**소방설비기사 (기계)**  \n소방 기계설비의 설계, 시공, 감리, 점검 전문가")
        st.markdown("**소방설비기사 (전기) (준비중)**  \n소방 전기설비의 설계, 시공, 감리, 점검 전문가")
    with col2:
        st.subheader("🦺 안전 분야")
        st.markdown("**산업안전기사**  \n산업현장의 안전관리 및 재해예방 전문가")
        st.markdown("**위험물산업기사**  \n위험물 취급 관리 전문가")

    with col3:
        st.subheader("🏢 BIM/설계 분야")
        st.markdown("**ACU 자격증**  \nAutodesk Certified User 이미 가지고 있음")

elif section == "취득 목표 및 기대효과":
    st.subheader("🎯 자격증 취득 목표 및 기대효과")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("- ✅ 2개 이상의 소방 관련 자격증(전기/기계) 취득으로 전문성 확보")
        st.markdown("- ✅ 산업안전기사, 위험물산업기사 등으로 취업 경쟁력 강화")

    with col2:
        st.markdown("- ✅ BIM 자격증으로 건축정보 모델링 기술 습득")
        st.markdown("- ✅ 다양한 분야 자격증으로 재난안전 전문가로서의 역량 강화")

import streamlit as st
from PIL import Image

st.title("미래 진로 및 비전")
st.markdown("### 소방공무원과 BIM 전문가로 성장하기 위한 계획")

col1, col2 = st.columns(2)

with col1:
    st.subheader("플랜 A: 소방공무원")
    st.markdown("필기시험 합격과 체력을 길러 소방공무원 경력채용에 도전하고, 전문 화재조사관으로 성장하는 것을 목표로 합니다.")
    st.markdown("#### 실천 계획")
    st.markdown("""
    1. **소방공무원 필기시험 합격**  
       - 소방학개론, 국어, 영어, 한국사 등 필기시험 대비 체계적 학습
    2. **체력 단련 및 체력시험 대비**  
       - 달리기, 윗몸일으키기, 팔굽혀펴기 등 체력 훈련 프로그램 실행
    3. **소방공무원 공개채용이나, 경력채용 지원**  
       - 전공과 자격증을 활용한 소방직 경력채용 준비
    4. **화재조사관 전문화**  
       - 화재감식평가기사 자격 취득 및 화재조사 전문교육 이수
    """)

with col2:
    st.subheader("플랜 B: BIM 전문가, 안전관리자")
    st.markdown("BIM 관련 지식과 기술을 심화 학습하여 재난안전 분야의 BIM 전문가 또는 안전관리자로 성장하는 것을 목표로 합니다.")
    st.markdown("#### 실천 계획")
    st.markdown("""
    1. **BIM 활용능력 심화**  
       - Revit, AutoCAD 등 BIM 소프트웨어 심화 학습 및 실무 프로젝트 참여
    2. **BIM 관련 자격증 취득**  
       - BIM 운용 전문가, BIM Coordinator 자격 취득
    3. **안전관리 역량 강화**  
       - 산업안전기사, 위험물산업기사 취득 및 안전관리 실무 경험 쌓기
    4. **BIM 관련 회사 취업**  
       - 소방엔지니어링, 설계사무소, 건설IT 회사 등에서 BIM 전문가로 활동
    """)

st.markdown("---")
st.markdown("### 기대 역량")

col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    <div style='text-align: center;'>
        <i class='fas fa-users' style='color: #3b82f6; font-size: 24px;'></i><br>
        <span style='font-size: 14px;'>리더십 역량</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='text-align: center;'>
        <i class='fas fa-wrench' style='color: #3b82f6; font-size: 24px;'></i><br>
        <span style='font-size: 14px;'>문제해결 능력</span>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div style='text-align: center;'>
        <i class='fas fa-laptop-code' style='color: #3b82f6; font-size: 24px;'></i><br>
        <span style='font-size: 14px;'>기술적 전문성</span>
    </div>
    """, unsafe_allow_html=True)

import streamlit as stㄴ

st.title("앞으로의 학습 목표")
st.markdown("### 재난안전소방 분야의 전문성을 넓히기 위한 계획")

col1, col2 = st.columns(2)

with col1:
    st.subheader("기초 역량 강화")
    st.markdown("재난안전소방 분야의 전문가가 되기 위한 기초 학문과 기술 역량을 강화합니다.")
    st.markdown("""
    <div style='margin-bottom: 12px;'>
        <span style='background-color:#DBEAFE;color:#1D4ED8;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>🔧 용접</span>
        <span style='background-color:#DBEAFE;color:#1D4ED8;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>🧮 수학</span>
        <span style='background-color:#DBEAFE;color:#1D4ED8;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>⚛️ 과학</span>
        <span style='background-color:#DBEAFE;color:#1D4ED8;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>📐 공학</span>
        <span style='background-color:#DBEAFE;color:#1D4ED8;padding:6px 12px;border-radius:20px;font-weight:500;'>💻 프로그래밍</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - 소방 및 안전 분야 핵심 이론에 대한 깊이 있는 학습  
    - 건축 구조 및 설계 관련 기초 지식 습득  
    - 다양한 공학 분야의 기초 학문에 대한 이해도 향상
    """)

with col2:
    st.subheader("실무 지식 습득")
    st.markdown("재난안전소방 분야의 전문가로서 필수적인 실무 지식을 적극적으로 습득합니다.")
    st.markdown("""
    <div style='margin-bottom: 12px;'>
        <span style='background-color:#FECACA;color:#B91C1C;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>🏢 BIM</span>
        <span style='background-color:#FECACA;color:#B91C1C;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>🛡️ 안전관리</span>
        <span style='background-color:#FECACA;color:#B91C1C;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>⚠️ 재난예방</span>
        <span style='background-color:#FECACA;color:#B91C1C;padding:6px 12px;border-radius:20px;margin-right:6px;font-weight:500;'>⛑️ 산업안전</span>
        <span style='background-color:#FECACA;color:#B91C1C;padding:6px 12px;border-radius:20px;font-weight:500;'>🔥 소방실무</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - BIM 기반 재난안전소방 설계 기술 심화 학습  
    - 소방설비의 설계, 시공, 감리에 관한 실무 지식 습득  
    - 재난 대응 매뉴얼 작성 및 현장 적용 능력 향상
    """)

st.markdown("---")
st.subheader("📍 학습 로드맵")

st.markdown("""
<div style='display:flex;justify-content:space-between;text-align:center;margin-top:24px;'>
    <div>
        <div style='background-color:#E0E7FF;border-radius:9999px;height:64px;width:64px;display:flex;align-items:center;justify-content:center;margin:auto;font-size:24px;'>📚</div>
        <p style='font-size:14px;margin-top:8px;font-weight:500;'>전공 기초 학습</p>
    </div>
    <div style='display:flex;align-items:center;color:#A0AEC0;font-size:24px;'>➡️</div>
    <div>
        <div style='background-color:#E0E7FF;border-radius:9999px;height:64px;width:64px;display:flex;align-items:center;justify-content:center;margin:auto;font-size:24px;'>📜</div>
        <p style='font-size:14px;margin-top:8px;font-weight:500;'>자격증 취득</p>
    </div>
    <div style='display:flex;align-items:center;color:#A0AEC0;font-size:24px;'>➡️</div>
    <div>
        <div style='background-color:#E0E7FF;border-radius:9999px;height:64px;width:64px;display:flex;align-items:center;justify-content:center;margin:auto;font-size:24px;'>🧑‍💻</div>
        <p style='font-size:14px;margin-top:8px;font-weight:500;'>실무 역량 강화</p>
    </div>
    <div style='display:flex;align-items:center;color:#A0AEC0;font-size:24px;'>➡️</div>
    <div>
        <div style='background-color:#E0E7FF;border-radius:9999px;height:64px;width:64px;display:flex;align-items:center;justify-content:center;margin:auto;font-size:24px;'>🎓</div>
        <p style='font-size:14px;margin-top:8px;font-weight:500;'>전문가 성장</p>
    </div>
</div>
""", unsafe_allow_html=True)
