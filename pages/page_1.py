import streamlit as st

st.set_page_config(page_title="Раздел 1: Общая информация", page_icon="📚")

st.markdown("# 📚 Раздел 1: Общая информация")
st.markdown("Выберите тему:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📋 Характеристика ПО", use_container_width=True, height=100):
        st.switch_page("pages/1.1_📋_Характеристика.py")

with col2:
    if st.button("📐 Геометрические элементы", use_container_width=True, height=100):
        st.switch_page("pages/1.2_📐_Элементы.py")

with col3:
    if st.button("⚙️ Установка", use_container_width=True, height=100):
        st.switch_page("pages/1.3_⚙️_Установка.py")

# Навигация по разделам
st.markdown("---")
st.markdown("### 📂 Другие разделы:")
col_a, col_b, col_c = st.columns(3)
with col_a:
    if st.button("📁 Раздел 2: Геометрия"):
        st.switch_page("pages/2_📚_Раздел_2_Геометрия.py")
with col_b:
    if st.button("📁 Раздел 3: Сетки"):
        st.switch_page("pages/3_📚_Раздел_3_Сетки.py")
