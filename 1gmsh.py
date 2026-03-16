import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Генерация сеток: Gmsh",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Кастомные стили
st.markdown("""
    <style>
    .title-container {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
        margin: 2rem 0;
    }
    .title-text {
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .subtitle-text {
        font-size: 1.8rem;
        opacity: 0.9;
        margin-bottom: 3rem;
    }
    .info-box {
        background-color: white;
        color: #333;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 2rem auto;
        max-width: 600px;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown("""
    <div class='title-container'>
        <div class='title-text'> Кратко о Gmsh</div>
    </div>
""", unsafe_allow_html=True)

# Информация об авторе
st.markdown("""
    <div class='info-box'>
        <h3 style='text-align: center; color: #667eea;'>Презентацию подготовили:</h3>
        <p style='text-align: center; font-size: 1.3rem;'><strong>Елизавета Пуцарь, Алёна Тетерина, Никита Федоров, Александр Шкляев</strong></p>
        <p style='text-align: center; color: #999; margin-top: 1rem;'>2026</p>
    </div>
""", unsafe_allow_html=True)


