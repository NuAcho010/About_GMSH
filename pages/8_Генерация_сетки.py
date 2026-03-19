import streamlit as st

st.markdown("""
<style>
    /* Разделители + отступы */
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
</style>
""", unsafe_allow_html=True)

# Настройка страницы
st.set_page_config(
    page_title="Генерация сетки в Gmsh",
    page_icon="🔷",
    layout="wide"
)

st.title("Методы построения и оптимизации сеток в Gmsh")

# Создание вкладок для каждого слайда
tabs = st.tabs([
    "Введение",
    "Что такое сетка?",
    "Виды сетки",
    "Алгоритмы",
    "Типы сеток",
    "Управление размером"
])

# ==================== СЛАЙД 1 ====================
with tabs[0]:
    st.header("Исходные данные для построения сетки")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📁 Источники геометрии")
        st.markdown("""
        - **Встроенный язык Gmsh**
        - **Геометрическое ядро OpenCascade**
        - **Импорт в формате STEP**
        """)
    
    with col2:
        st.subheader("🔧 Алгоритмы поверхностной сетки")
        st.markdown("""
        - **MeshAdapt**
        - **Delaunay**
        - **Frontal Delaunay**
        """)
    
    st.info("💡 Для генерации поверхностной сетки предлагаются три основных алгоритма")

# ==================== СЛАЙД 2 ====================
with tabs[1]:
    st.header("Что такое сетка в GMSH?")
    
    st.markdown("""
    **Сетка** — это совокупность узлов и элементов, которые аппроксимируют геометрию.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Узлы")
        st.markdown("""
        - Точки в пространстве
        - Координаты: **(x, y, z)**
        - Базовые элементы сетки
        """)
    
    with col2:
        st.subheader("🔷 Элементы")
        st.markdown("""
        - Фигуры, соединяющие узлы
        - Типы: линии, треугольники, тетраэдры и т.д.
        - Определяют дискретизацию
        """)
    
    st.success("✅ Сетка позволяет численно решать задачи на сложных геометриях")

# ==================== СЛАЙД 3 ====================
with tabs[2]:
    st.header("Виды сетки по размерности")
    
    st.markdown("""
    В GMSH сетка строится **иерархически**: сначала 0D (точки), потом 1D (линии), 2D (поверхности) и 3D (объемы).
    """)
    
    tab1, tab2, tab3 = st.tabs(["1D Сетка", "2D Сетка", "3D Сетка"])
    
    with tab1:
        st.subheader("📏 1D Сетка (Линейные элементы)")
        st.markdown("""
        **Элементы:** Отрезки (Line elements)
        
        **Применение:**
        - Расчёт балок и ферм (Beam/Truss elements)
        - Задание граничных условий на рёбрах 3D модели
        - Каркас для построения 2D и 3D сеток
        """)
    
    with tab2:
        st.subheader("🔲 2D Сетка (Поверхностные элементы)")
        st.markdown("""
        **Элементы:**
        - Треугольники (Triangles): 3 узла (линейные) или 6 узлов (квадратичные)
        - Четырёхугольники (Quadrangles/Quads): 4 узла (линейные) или 8 узлов (квадратичные)
        
        **Применение:**
        - Задачи плоской деформации или плоского напряжённого состояния
        - Оболочечные конструкции (Shells)
        - Поверхности для CFD (вход/выход потока)
        - Промежуточный этап перед генерацией 3D сетки
        """)
    
    with tab3:
        st.subheader("🧊 3D Сетка (Объёмные элементы)")
        st.markdown("""
        **Элементы:**
        - Тетраэдры (Tetrahedra): 4 узла (линейные) или 10 узлов (квадратичные)
        - Гексаэдры (Hexahedra/Bricks): 8 узлов (линейные) или 20 узлов (квадратичные)
        - Призмы (Prisms/Wedges): 6 узлов
        - Пирамиды (Pyramids): 5 узлов
        
        **Применение:**
        - 3D анализ напряжений
        - Теплопередача
        - Электромагнетизм
        - 3D гидродинамика (CFD)
        """)

# ==================== СЛАЙД 4 ====================
with tabs[3]:
    st.header("Алгоритмы генерации сетки в GMSH")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔷 2D (Поверхности)")
        st.markdown("""
        | Алгоритм | Описание |
        |----------|----------|
        | **MeshAdapt** | Адаптивный. Для сложной геометрии |
        | **Delaunay** | Классическая триангуляция. Быстрый |
        | **Frontal-Delaunay** | Комбинация. Лучшее качество |
        | **Packing** | Упаковка кругов. Специфические задачи |
        | **Transfinite** | Структурированная сетка. Требует ручной подготовки |
        """)
    
    with col2:
        st.subheader("🧊 3D (Объёмы)")
        st.markdown("""
        | Алгоритм | Описание |
        |----------|----------|
        | **Delaunay (3D)** | Стандарт. Заполняет тетраэдрами |
        | **Frontal (3D)** | Лучшее качество на границах |
        | **Extrude** | 2D → 3D (треугольники → призмы) |
        | **Transfinite (3D)** | Структурированная гексаэдральная сетка |
        """)
    
    st.warning("⚠️ Transfinite требует, чтобы объём был топологически эквивалентен гексаэдру (6 граней)")

# ==================== СЛАЙД 5 ====================
with tabs[4]:
    st.header("Виды сеток")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Неструктурированная Тетраэдральная",
        "Неструктурированная Гексаэдральная",
        "Структурированная Тетраэдральная",
        "Структурированная Гексаэдральная"
    ])
    
    with tab1:
        st.subheader("🔷 Неструктурированная Тетраэдральная")
        st.markdown("""
        - Настраивается параметрами во входных файлах
        - Для каждой точки добавлен параметр с разделителем `;`""")
        st.code("data:\n\tclass: block.Matrix\n\tmatrix: [ [0;0.01, 0.250;0.1], [0;0.01, 1;0.1], [0;0.01, 0.250;0.1] ]", language = "bash")
        st.markdown("""
        - Пример: `0;0.01` для первой точки по оси X
        - Параметры `0.01` или `0.1` = приблизительный размер сетки вблизи точек
        """)
        st.code("python -m gmsh_scripts bottom.yaml", language = "bash")
        st.code("metadata:\n\trun:\n\t\tfactory: geo\n\t\tstrategy :\n\t\t\tclass: strategy.NoBoolean\ndata:\n\tclass: block.Matrix\n\tmatrix: [[0;0.01, 0.250;0.1], [0;0.01, 1;0.1], [0;0.01, 0.250;0.1]]", language = "bash")
        cols = st.columns([1, 3, 1])
        with cols[1]: 
            st.image("/home/nvf/Work/University/MKR/pages/pictures/3.jpg", caption="Неструктурированная тетраэдральная сетка", width=600)
    with tab2:
        st.subheader("🧊 Неструктурированная Гексаэдральная")
        st.markdown("""
        - Объём заполняется гексаэдрами
        - Соединены произвольно
        - Нет логической сетки координат (i, j, k)
        """)
        st.code("python -m gmsh_scripts bottom.yaml", language = "bash")
        st.code("metadata:\n\trun:\n\t\tfactory: geo\n\t\tstrategy:\n\t\t\tclass: strategy.NoBoolean\n\t\toptions:\n\t\t\tMesh.MeshSizeFactor: 1\n\t\t\tMesh.MeshSizeMin: 0\n\t\t\tMesh.MeshSizeMax: 0\n\t\t\tMesh.MeshSizeFromPoints: 0\n\t\t\tMesh.SubdivisionAlgorithm: 2\ndata:\n\tclass: block.Matrix\n\tmatrix: [[0, 0.250], [0, 1], [0, 0.250]]", language = "bash")
        cols = st.columns([1, 3, 1])
        with cols[1]:
            st.image("/home/nvf/Work/University/MKR/pages/pictures/5.jpg", caption="Неструктурированная гексаэдральная сетка", width=600)
    
    with tab3:
        st.subheader("🔷 Структурированная Тетраэдральная")
        st.markdown("""
        - Каждый элемент адресуется тремя индексами (i, j, k)
        - У каждого внутреннего узла предсказуемое количество соседей
        - Топология регулярна
        
        **Варианты создания:**
        - Разбиение структурированной гекса-сетки на тетраэдры
        - Структурированная треугольная сетка в 2D
        - Направленно-структурированные (полуструктурированные) сетки""")
        st.markdown("""
        **Для создания:** добавить третий параметр к точке в поле `matrix` с разделителем `;`
        """)    
        st.code("metadata:\n\trun:\n\t\tfactory: geo\n\t\tstrategy:\n\t\t\tclass: strategy.NoBoolean\n\ndata\n\tclass: block.Matrix\n\tmatrix: [[0;0.01, 0.250;0.1;4], [0;0.01, 1;0.1;8], [0;0.01, 0.250;0.1;16]]", language = "bash")
        
        cols = st.columns([3, 1, 3])
        with cols[0]:
            st.image("/home/nvf/Work/University/MKR/pages/pictures/7.jpg", caption="Неструктурированная гексаэдральная сетка", width=600)
        with cols[2]:
            st.image("/home/nvf/Work/University/MKR/pages/pictures/8.jpg", caption="Структурированная тетраэдральная сетка", width=600)
        st.markdown("""Отключить генерацию структурированной сетки сразу для всех блоков можно установив children_items_do_structure_map = [0, ..., количество дети] в родительском блоке, например, для main.yaml""")
        st.code("metadata:\n\trun:\n\t\tfactory: geo\n\t\tstrategy:\n\t\t\tclass: strategy.NoBoolean\ndata:\n\tclass: block.Block\n\tdo_register: 0\n\tchildren: [\n\t\t/bottom.yaml,\n\t\t/top_1.yaml,\n\t\t/top_2.yaml,\n\t\t/top_3.yaml\n\t]\n\tchildren_transforms: [\n\t\t[],\n\t\t[[0, 0, 0.250]],\n\t\t[[0.250, 0, 0.250]],\n\t\t[[0.470, 0, 0.250]]\n\t]\n\tchildren_items_do_structure_map: [0, 0, 0, 0]", language = "bash")
        cols = st.columns([1, 3, 1])
        with cols[1]:
            st.image("/home/nvf/Work/University/MKR/pages/pictures/11.jpg", caption="Структурированная тетраэдральная сетка с отключенными ""children_items_do_structure_map""", width=600)
        
    with tab4:
        st.subheader("🧊 Структурированная Гексаэдральная")
        st.markdown("""
        ⭐ **«Золотой стандарт» конечно-элементного анализа**
        
        - Каждый внутренний узел имеет строго определённое количество соседей
        - Элементы упорядочены по логическим направлениям (I, J, K)
        
        **Для создания:**
        - `items_do_quadrate_map = 1` в поле `data` (0 по умолчанию)""")
        
        st.code("metadata:run:\n\tfactory: geo\n\tstrategy:\n\t\tclass: strategy.NoBoolean\n\ndata:\n\tclass: block.Matrix\n\tmatrix: [ \n\t[ 0;0.01, 0.250;0.1;4 ], \n\t[ 0;0.01, 1;0.1;8 ], \n\t[ 0;0.01, 0.250;0.1;16 ] ]\n\titems_do_quadrate_map: 1", language = "bash")
        cols = st.columns([1, 3, 1])
        with cols[1]:
            st.image("/home/nvf/Work/University/MKR/pages/pictures/14.jpg", caption="Структурированная гексаэдральная сетка""", width=600)
        st.markdown("""
        **Методы изменения положения узлов:**
        1. **progression** - увеличение/уменьшение расстояния от начальной до конечной точки
        2. **bump** - увеличение/уменьшение расстояния от центра до точек
        
        **Для progression указать 2 дополнительных подпараметра:**
        1. Первый: `0` (выбирает тип progression)
        2. Второй: коэффициент progression (>1 - увеличение, <1 - уменьшение)
        """)

# ==================== СЛАЙД 6 ====================
with tabs[5]:
    st.header("Управление размером сетки")
    
    
    st.subheader("📐 1. Характеристическая длина")
    st.markdown("""
    **Characteristic Length** - базовый параметр размера ячейки
    """)
    
    st.subheader("🎯 2. Поля (Fields)")
    st.markdown("""
    | Поле | Описание |
    |------|----------|
    | **Distance Field** | Размер зависит от расстояния до линии/точки |
    | **Threshold Field** | Плавный переход от мелкой к крупной сетке |
    | **MathEval Field** | Размер задётся формулой (например, x² + y²) |
    | **Box Field** | Задание размера внутри прямоугольной области |
    """)


    st.subheader("🔍 3. Локальное измельчение")
    st.markdown("""
    **Refinement** - можно выбрать готовые элементы и разбить их на более мелкие
    
    Для генерации сетки добавить поле metadata в main.yaml""")
    st.code("metadata:\n\trun:\n\t\tfactory: geo\n\t\tstrategy:\n\t\t\tclass: strategy.NoBoolean\ndata:\n\tclass: block.Block\n\tdo_register: 0\n\tchildren: [\n\t\t/bottom.yaml,\n\t\t/top_1.yaml,\n\t\t/top_2.yaml,\n\t\t/top_3.yaml\n\t]\nchildren_transforms: [\n\t[],\n\t[[ 0, 0, 0.250 ]],\n\t[[ 0.250, 0, 0.250 ]],\n\t[[ 0.470, 0, 0.250 ]]\n]", language = "bash")
    cols = st.columns([1, 3, 1])
    with cols[1]:
        st.image("/home/nvf/Work/University/MKR/pages/pictures/17.jpg", caption="Сетка по умолчанию""", width=600)


# ==================== ПОДВАЛ ====================
st.divider()
