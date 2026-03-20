import streamlit as st

# --- Конфигурация страницы ---
st.set_page_config(page_title="Раздел 1: Общая информация", page_icon="📚", layout="wide")

# --- Пользовательские стили (CSS) ---
st.markdown("""
<style>
    /* Разделители + отступы для вкладок */
    div[data-baseweb="tab-list"] {
        gap: 5px !important;
    }
    
    div[data-baseweb="tab-list"] button[role="tab"] {
        border-right: 1px solid #444;
        padding: 10px 25px !important;
    }
    
    div[data-baseweb="tab-list"] button[role="tab"]:last-child {
        border-right: none;
    }
    
    /* Дополнительные стили для карточек */
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- Заголовок раздела ---
st.title("Общая информация")


# --- Функция для вкладки "Характеристика ПО" ---
def show_software_characteristics_tab():
    # Основная информация в виде метрик
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Версия", value="4.15.1")
    with col2:
        st.metric(label="Дата документации", value="Февраль 2026")
    with col3:
        st.metric(label="Лицензия", value="GNU GPL")
    with col4:
        st.metric(label="Платформы", value="Win/macOS/Linux")
    
    st.divider()
    
    # Описание и назначение
    st.subheader("Общее описание")
    st.markdown("""
    **Gmsh** — это трехмерный генератор сеток конечных элементов со встроенным CAD-движком и постпроцессором. 
    Основная цель разработки — предоставление быстрого, легкого и удобного инструмента для работы с сетками 
    с параметрическим вводом и гибкими возможностями визуализации.
    """)
    
    # Архитектура (4 модуля)
    st.subheader("Архитектура системы")
    st.markdown("Gmsh построен вокруг четырех основных модулей:")
    
    col_mod1, col_mod2 = st.columns(2)
    with col_mod1:
        with st.expander("🔷 Geometry (Геометрия)", expanded=True):
            st.write("""
            - Построение геометрии используя граничное представление (BRep).
            - Поддержка ядер: **Built-in** и **OpenCASCADE**.
            - Импорт форматов: STEP, IGES, BREP, XAO.
            - Создание физических групп для определения свойств материалов и границ.
            """)
        with st.expander("🔷 Mesh (Сетка)", expanded=True):
            st.write("""
            - Генерация 1D, 2D и 3D сеток (неструктурированные и структурированные).
            - Алгоритмы: Delaunay, Frontal-Delaunay, MeshAdapt, HXT.
            - Поддержка сеток высокого порядка (high-order meshes).
            - Управление размером элементов через поля (Fields).
            """)
    with col_mod2:
        with st.expander("🔷 Solver (Решатель)", expanded=True):
            st.write("""
            - Интерфейс **ONELAB** для обмена данными с внешними решателями.
            - Клиент-серверная модель взаимодействия.
            - Интеграция с решателем GetDP.
            """)
        with st.expander("🔷 Post-processing (Постпроцессинг)", expanded=True):
            st.write("""
            - Визуализация скалярных, векторных и тензорных данных.
            - Поддержка анимаций и экспорта изображений.
            - Работа с view (представлениями данных).
            - Плагины для обработки данных (CutPlane, Isosurface и др.).
            """)
    
    st.divider()
    
    # Интерфейсы управления
    st.subheader("🎛 Интерфейсы управления")
    st.markdown("""
    Пользователи могут взаимодействовать с Gmsh несколькими способами:
    """)
    tabs_interfaces = st.tabs(["Графический интерфейс", "Командная строка", "Скриптовый язык (.geo)", "Программирование"])
    
    with tabs_interfaces[0]:
        st.write("Интерактивное построение геометрии, генерация сетки и визуализация через меню и дерево моделей.")
    with tabs_interfaces[1]:
        st.code("gmsh file.geo -2 -format msh4", language="bash")
        st.write("Пакетный режим работы, автоматизация процессов без запуска GUI.")
    with tabs_interfaces[2]:
        st.write("Собственный скриптовый язык (.geo файлы) с поддержкой циклов, макросов и условий.")
        st.code("Point(1) = {0, 0, 0, 1.0};", language="cpp")
    with tabs_interfaces[3]:
        st.write("Интеграция в сторонний код через API.")
        st.code("Поддерживаемые языки: C++, C, Python, Julia, Fortran", language="cpp")
    
    st.divider()
    
    # Преимущества и ограничения (на основе разделов 1.5 и 1.6 документации)
    col_pros, col_cons = st.columns(2)
    
    with col_pros:
        st.subheader("Преимущества")
        st.success("""
        - Быстрое описание параметрической геометрии.
        - Тонкий контроль над размером элементов сетки.
        - Генерация криволинейных сеток высокого порядка.
        - Кроссплатформенность и открытое ПО (Free).
        - Возможность работы на серверах без GUI.
        - Встроенные инструменты оптимизации сетки.
        """)
        
    with col_cons:
        st.subheader("Ограничения")
        st.warning("""
        - Не является многоблочным генератором (все сетки конформные).
        - Через графический интерфейс предоставляется только часть возможностей (полный контроль через скрипты).
        - Не заменяет полноценные CAD-системы высшего уровня.
        """)
    
    st.divider()
    
    # Информация для цитирования и авторы
    st.subheader("📚 Информация о разработке")
    st.markdown("""
    **Авторы:** Christophe Geuzaine, Jean-François Remacle  
    """)
    

# --- Создание вкладок ---
# Добавил вторую вкладку для демонстрации работы CSS стилей
tab1, tab2 = st.tabs(["Характеристика ПО", "Внешний вид ПО"])

with tab1:
    show_software_characteristics_tab()

with tab2:
    cols = st.columns([1, 3, 1])
    with cols[1]:
        st.image("/home/nvf/Work/University/MKR/pages/pictures/20.png", caption="""Интерфейс программы""", width=800)
    
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🗂️ Структура интерфейса")
    
        st.markdown("""
        **Верхняя панель:**
        - File (Файл)
        - Tools (Инструменты)
        - Window (Окно)
        - Help (Помощь)
        """)
    

    with col2:
        st.subheader("📋 Дерево модулей")
        st.markdown("""
        Интерфейс организован в виде иерархического дерева с тремя основными модулями
        """)

    st.divider()

    # Модуль Geometry
    with st.expander("🔷 Модуль Geometry (Геометрия)", expanded=True):
        st.markdown("""
        **Назначение:** Создание и редактирование геометрических моделей
    
        **Основные функции:**
    
        *Elementary entities (Элементарные объекты):*
        - **Set geometry kernel** - выбор ядра геометрии (Built-in или OpenCASCADE)
        - **Add** - добавление точек, кривых, поверхностей, объемов
        - **Transform** - трансформация (перемещение, поворот, масштабирование)
        - **Extrude** - экструзия (выдавливание) объектов
        - **Boolean** - булевы операции (объединение, пересечение, вычитание)
        - **Fillet** - создание скруглений
        - **Split curve** - разбиение кривых
        - **Delete** - удаление объектов
        - **Coherence** - проверка связности геометрии
    
        *Physical groups (Физические группы):*
        - Группировка объектов для задания граничных условий
    
        *Script management:*
        - **Reload script** - перезагрузка скрипта
        - **Remove last script command** - отмена последней команды
        - **Edit script** - редактирование .geo файла
        """)

    # Модуль Mesh
    with st.expander("🔷 Модуль Mesh (Сетка)", expanded=True):
        st.markdown("""
        **Назначение:** Генерация конечно-элементной сетки
    
        **Основные функции:**
    
        *Define (Определение):*
        - **Size at points** - задание размера элементов в точках
        - **Size fields** - поля размеров для адаптивной сетки
    
        *Mesh constraints (Ограничения сетки):*
        - **Embedded** - встроенные объекты
        - **Transfinite** - трансфинитная (структурированная) сетка
        - **Compound** - объединение объектов для сетки
        - **Recombine** - рекомбинация в четырехугольники/шестигранники
    
        *Dimension (Размерность):*
        - **1D** - генерация 1D сетки (кривые)
        - **2D** - генерация 2D сетки (поверхности)
        - **3D** - генерация 3D сетки (объемы)
    
        *Optimization (Оптимизация):*
        - **Optimize 3D** - оптимизация 3D сетки
        - **Set order 1/2/3** - порядок элементов (линейные/квадратичные/кубические)
        - **High-order tools** - инструменты для высокопорядковых сеток
        - **Refine by splitting** - измельчение разбиением
    
        *Advanced (Расширенные):*
        - **Partition/Unpartition** - разбиение на части
        - **Smooth 2D** - сглаживание 2D сетки
        - **Recombine 2D** - рекомбинация 2D
        - **Reclassify 2D** - реклассификация 2D
    
        *Other:*
        - **Experimental** - экспериментальные функции
        - **Reverse** - обращение ориентации
        - **Delete** - удаление сетки
        - **Inspect** - инспекция сетки
        - **Save** - сохранение сетки
        """)

    # Модуль Solver
    with st.expander("🔷 Модуль Solver (Решатель)", expanded=False):
        st.markdown("""
        **Назначение:** Интеграция с решателями
    
        **Доступные решатели:**
        - **GetDP** - решатель конечных элементов (по умолчанию)
    
        **Возможности:**
        - Запуск расчетов
        - Обмен параметрами через ONELAB
        - Визуализация результатов
        """)

    st.divider()

    # Описание рабочей области
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🖼️ Рабочая область")
        st.markdown("""
        - Центральная область для визуализации
        - 3D view с возможностью вращения, масштабирования
        - Отображение геометрии и сетки
        - Интерактивное выделение объектов
        """)


    st.divider()
