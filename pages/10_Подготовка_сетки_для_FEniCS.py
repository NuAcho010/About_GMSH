import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Перенос сетки в FEniCS",
    page_icon="🔢",
    layout="wide"
)


# Создание вкладок для каждого слайда
tabs = st.tabs([
    "О FEniCS",
    "Инструмент meshio",
    "Маркировка объектов",
    "Рабочий процесс"
])

# ==================== СЛАЙД 1 ====================
with tabs[0]:
    st.header("📚 Коротко о FEniCS")
    
    st.markdown("""
    **FEniCS** — набор бесплатных программных компонентов с открытым исходным кодом, 
    цель которых — **автоматизированное решение дифференциальных уравнений методом конечных элементов (FEM)**.
    """)
    
    st.info("💡 FEniCSx — новая версия FEniCS с улучшенной архитектурой")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📁 Поддерживаемые форматы")
        st.markdown("""
        | Формат | Описание |
        |--------|----------|
        | **.msh** | Прямой импорт сеток из Gmsh |
        | **XDMF** | eXtensible Data Model and Format |
        """)
    
    with col2:
        st.subheader("✅ Рекомендации")
        st.markdown("""
        - **FEniCSx** имеет встроенную поддержку **.msh**
        - **XDMF** рекомендуется для **долгосрочного хранения данных**
        - Оба формата отлично работают в экосистеме FEniCSx
        """)
    
    st.success("✅ Современная экосистема FEniCSx обеспечивает гибкость в выборе форматов")

# ==================== СЛАЙД 2 ====================
with tabs[1]:
    st.header("🔧 Ключевой инструмент — meshio")
    
    st.markdown("""
    **meshio** — это универсальная библиотека на Python, предназначенная для 
    **чтения и записи множества различных форматов сеток и данных**, связанных с ними.
    """)
    
    st.code("""
# Установка meshio
pip install meshio

# Пример использования
import meshio

# Чтение сетки
mesh = meshio.read("mesh.msh")

# Запись в другой формат
meshio.write("mesh.xdmf", mesh)
    """, language="python")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Возможности meshio")
        st.markdown("""
        - Конвертация между форматами
        - Чтение/запись .msh, .xdmf, .vtk и др.
        - Работа с физическими группами
        - Поддержка данных узлов и ячеек
        """)
    
    with col2:
        st.subheader("📊 Поддерживаемые форматы")
        st.markdown("""
        - **Gmsh** (.msh v2, v4)
        - **XDMF** (.xdmf, .h5)
        - **VTK** (.vtk, .vtu)
        - **ABAQUS** (.inp)
        - **ANSYS** (.msh)
        - И многие другие
        """)
    
    st.warning("⚠️ meshio является ключевым звеном между Gmsh и FEniCS")

# ==================== СЛАЙД 3 ====================
with tabs[2]:
    st.header("🏷️ Маркировка геометрических объектов")
    
    st.markdown("""
    Ключевым аспектом подготовки сетки является **корректная маркировка геометрических объектов в GMSH**. 
    Для этого используется система так называемых **"физических групп"**.
    """)
    
    st.info("💡 Физические группы позволяют идентифицировать границы и области для применения граничных условий")
    
    st.subheader("📋 Пример создания физических групп в Gmsh (.geo)")
    
    st.code("""
// Создание физических групп для границ
Physical Surface("Граница_1") = {1};
Physical Surface("Граница_2") = {2};
Physical Volume("Область_1") = {1};

// Или с числовыми идентификаторами
Physical Line(1) = {1, 2, 3};  // Идентификатор 1
Physical Line(2) = {4, 5, 6};  // Идентификатор 2
    """, language="cpp")
    
    st.subheader("🔑 Важность маркировки")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Для граничных условий
        - Определение границ Дирихле
        - Определение границ Неймана
        - Разные условия на разных частях границы
        """)
    
    with col2:
        st.markdown("""
        ### Для материалов
        - Разные модули упругости
        - Разные коэффициенты теплопроводности
        - Композитные материалы
        """)
    
    st.success("✅ Правильная маркировка упрощает применение граничных условий в FEniCS")

# ==================== СЛАЙД 4 ====================
with tabs[3]:
    st.header("🔄 Рабочий процесс: 4 этапа")
    
    st.markdown("""
    Рекомендуемый рабочий процесс можно разделить на **четыре основных этапа**:
    """)
    
    # Этап 1
    st.subheader("📐 Этап 1: Подготовка геометрии и сетки в GMSH")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **1. Создание геометрии**
        - Встроенный язык Gmsh
        - Импорт STEP
        - OpenCascade ядро
        """)
    
    with col2:
        st.markdown("""
        **2. Сгущение сетки**
        - Поля размера (Fields)
        - Локальное измельчение
        - Физические группы
        """)
    
    st.divider()
    
    # Этап 2
    st.subheader("📤 Этап 2: Экспорт сетки")
    
    st.markdown("""
    Сетка экспортируется в принятых форматах:
    """)
    
    st.code("""
# В Gmsh GUI: File → Export
# Или в скрипте .geo:
Save "mesh.msh";
# Или
Save "mesh.xdmf";
    """, language="cpp")
    
    st.divider()
    
    # Этап 3
    st.subheader("📥 Этап 3: Импорт сетки и маркеров в FEniCS")
    
    st.markdown("""
    В Python-скрипте, который будет выполнять само моделирование, первым делом импортируется сетка.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Прямой импорт .msh")
        st.code("""
from dolfinx import mesh
from mpi4py import MPI

mesh = mesh.create_mesh(
    MPI.COMM_WORLD,
    "path/to/mesh.msh"
)
        """, language="python")
    
    with col2:
        st.subheader("Импорт .xdmf")
        st.code("""
from dolfinx import io

# Сетка и маркеры импортируются отдельно
mesh = io.read_mesh("mesh.xdmf")
markers = io.read_meshtags("markers.xdmf")
        """, language="python")
    
    st.warning("⚠️ При использовании meshio могут генерироваться отдельные файлы для сетки и маркеров")
    
    st.divider()
    
    # Этап 4
    st.subheader("🧮 Этап 4: Решение задачи")
    
    st.markdown("""
    После того как сетка и маркеры граничных элементов успешно импортированы, 
    можно переходить к определению пробного пространства, функций, уравнений и граничных условий.
    """)
    
    st.code("""
from dolfinx import fem, bc

# MeshFunction с маркерами граничных элементов
# используется для выбора подмножества границ

# Пример: Условия Дирихле на границе с идентификатором 1
dofs = fem.locate_dofs_topological(V, 1, boundary_markers.find(1))
bc_dirichlet = bc.dirichletbc(value, dofs)

# boundary_markers и marker_id указывают, 
# как выбрать степени свободы
    """, language="python")
    
    st.info("💡 MeshFunction позволяет применять разные граничные условия к разным частям границы модели")
    
    st.success("✅ Аналогично можно определять области действия различных коэффициентов в уравнении")

# ==================== ПОДВАЛ ====================
st.divider()
st.markdown("""
<center>
📚 Материал подготовлен для студентов МГУ  
🔧 Gmsh + FEniCS — мощный инструмент для FEM анализа  
👤 Никита Валерьевич, 1 курс магистратуры МГУ
</center>
""", unsafe_allow_html=True)
