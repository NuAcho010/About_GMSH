import streamlit as st

st.set_page_config(page_title="Установка", page_icon="⚙️")

st.markdown("# ⚙️ Установка Gmsh")

# Вкладки для подтем
tab_windows, tab_linux, tab_macos = st.tabs(["🪟 Windows", "🐧 Linux", "🍎 macOS"])

with tab_windows:
    st.markdown("### Установка на Windows")
    st.code("pip install gmsh", language="bash")
    st.info("Скачайте установщик с gmsh.info")

with tab_linux:
    st.markdown("### Установка на Linux")
    st.code("sudo apt-get install gmsh", language="bash")

with tab_macos:
    st.markdown("### Установка на macOS")
    st.code("brew install gmsh", language="bash")

# Или раскрывающиеся списки
with st.expander("🔧 Дополнительные настройки"):
    st.write("Здесь детали для продвинутых пользователей")
    
with st.expander("❓ Решение проблем"):
    st.write("Инструкции по устранению ошибок")
