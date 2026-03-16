import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Интерактивные возможности", page_icon="🎮")

st.markdown("<div class='slide-header'>🎮 Интерактивные возможности создания области</div>", unsafe_allow_html=True)

st.markdown("""
<div class='content-box'>
    <h3>🎛️ Изменяйте параметры в реальном времени!</h3>
    <p>Используйте виджеты Streamlit для интерактивного изменения геометрии:</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Параметры геометрии")
    width = st.slider("Ширина области", 0.5, 2.0, 1.0, 0.1)
    height = st.slider("Высота области", 0.3, 1.5, 0.5, 0.1)
    mesh_size = st.slider("Размер ячейки сетки", 0.01, 0.2, 0.05, 0.01)
    
    st.metric("Площадь области", f"{width * height:.2f}")
    st.metric("Примерное число узлов", f"{int(width * height / mesh_size**2)}")

with col2:
    st.markdown("#### Визуализация")
    fig, ax = plt.subplots(figsize=(8, 6))
    rect = plt.Rectangle((0, 0), width, height, fill=False, linewidth=2, color='blue')
    ax.add_patch(rect)
    
    # Сетка
    x = np.arange(0, width + mesh_size, mesh_size)
    y = np.arange(0, height + mesh_size, mesh_size)
    X, Y = np.meshgrid(x, y)
    ax.plot(X, Y, 'g-', alpha=0.3, linewidth=0.5)
    ax.plot(X.T, Y.T, 'g-', alpha=0.3, linewidth=0.5)
    
    ax.set_xlim(-0.1, width + 0.1)
    ax.set_ylim(-0.1, height + 0.1)
    ax.set_aspect('equal')
    ax.set_title(f"Область {width}x{height}")
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

# Навигация
st.markdown("---")
col_prev, col_next = st.columns(2)

