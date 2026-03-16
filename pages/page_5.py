import streamlit as st

st.set_page_config(page_title="Заключение", page_icon="✅")

st.markdown("<div class='slide-header'>✅ Заключение</div>", unsafe_allow_html=True)

st.markdown("""
<div class='content-box' style='text-align: center;'>
    <h2>📚 Основные выводы:</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.success("""
    **✅ Что мы изучили:**
    - Gmsh — мощный инструмент для генерации сеток
    - Поддерживает 2D и 3D геометрии
    - Гибкая система маркирования областей
    - Интеграция с FEniCS и другими FEM пакетами
    - Python API для автоматизации
    """)

with col2:
    st.info("""
    **🔗 Полезные ресурсы:**
    - 📎 Документация: [gmsh.info/doc/](https://gmsh.info/doc/)
    - 📎 Примеры: [GitLab Gmsh](https://gitlab.onelab.info/gmsh/gmsh)
    - 📎 pygmsh: [PyPI](https://pypi.org/project/pygmsh/)
    - 📎 meshio: [GitHub](https://github.com/nschloe/meshio)
    """)

# Финальная кнопка
st.markdown("---")
if st.button("🏠 Вернуться на главную", type="primary", use_container_width=True):
    st.switch_page("0_🏠_Главная.py")

st.markdown("""
<div class='content-box' style='text-align: center;'>
    <h3>🙏 Спасибо за внимание!</h3>
    <p>Вопросы?</p>
</div>
""", unsafe_allow_html=True)
