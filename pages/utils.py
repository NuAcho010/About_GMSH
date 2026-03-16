# Общие стили для всех страниц
COMMON_STYLES = """
    <style>
    .slide-header {
        font-size: 2.5rem;
        color: #1f77b4;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-bottom: 2rem;
    }
    .content-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    </style>
"""

def render_navigation(prev_page, next_page, prev_label="⬅️ Назад", next_label="Вперёд ➡️"):
    """Рендерит кнопки навигации"""
    st.markdown("---")
    col_prev, col_next = st.columns(2)
    
    with col_prev:
        if prev_page:
            if st.button(prev_label, use_container_width=True):
                st.switch_page(prev_page)
    
    with col_next:
        if next_page:
            if st.button(next_label, use_container_width=True):
                st.switch_page(next_page)
