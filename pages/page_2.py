import streamlit as st

st.set_page_config(page_title="Геометрические элементы", page_icon="📐")

st.markdown("<div class='slide-header'>📐 Геометрические элементы</div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["0D - Точки", "1D - Линии", "2D - Поверхности", "3D - Объемы"])

with tab1:
    st.markdown("### Точки (Points)")
    st.write("Базовые элементы для построения геометрии")
    st.code("Point(1) = {0, 0, 0, lc};", language="cpp")
    st.info("💡 `lc` — характерный размер элемента сетки")

with tab2:
    st.markdown("### Линии (Lines)")
    st.write("Отрезки, окружности, сплайны")
    st.code("""
Line(1) = {1, 2};
Circle(2) = {2, 3, 4};
Spline(3) = {4, 5, 6, 1};
    """, language="cpp")

with tab3:
    st.markdown("### Поверхности (Surfaces)")
    st.write("Плоские и криволинейные поверхности")
    st.code("""
Line Loop(1) = {1, 2, 3, 4};
Plane Surface(2) = {1};
    """, language="cpp")

with tab4:
    st.markdown("### Объемы (Volumes)")
    st.write("Трехмерные тела")
    st.code("""
Surface Loop(1) = {1, 2, 3, 4, 5, 6};
Volume(2) = {1};
    """, language="cpp")

# Навигация
st.markdown("---")
col_prev, col_next = st.columns(2)


