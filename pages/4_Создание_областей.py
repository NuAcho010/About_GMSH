# pages/creating_volume.py
# Страница: Создание области

import streamlit as st

def show():
    st.title("🎯 Создание области (Volume)")
    
    st.markdown("""
    ## Что такое область?
    
    Область (объём) — это трёхмерная замкнутая область, ограниченная поверхностями.
    В Gmsh есть два основных способа создания областей.
    """)
    
    tab1, tab2 = st.tabs(["🔨 Способ 1: 'Снизу вверх' (Bottom-up)", "🧊 Способ 2: Твердотельное моделирование (CSG)"])
    
    with tab1:
        st.markdown("""
        ### Пошаговое создание куба
        
        Этот метод используется во встроенном геометрическом ядре Gmsh.
        """)
        
        steps = [
            ("1. Точки", """
            Point(1) = {0,0,0};
            Point(2) = {1,0,0};
            Point(3) = {1,1,0};
            Point(4) = {0,1,0};
            Point(5) = {0,0,1};
            Point(6) = {1,0,1};
            Point(7) = {1,1,1};
            Point(8) = {0,1,1};
            """),
            ("2. Рёбра", """
            Line(1) = {1,2}; Line(2) = {2,3}; Line(3) = {3,4}; Line(4) = {4,1};
            Line(5) = {5,6}; Line(6) = {6,7}; Line(7) = {7,8}; Line(8) = {8,5};
            Line(9) = {1,5}; Line(10) = {2,6}; Line(11) = {3,7}; Line(12) = {4,8};
            """),
            ("3. Петли и поверхности", """
            Curve Loop(1) = {1,2,3,4}; Plane Surface(1) = {1};
            Curve Loop(2) = {-5,-6,-7,-8}; Plane Surface(2) = {2};
            Curve Loop(3) = {1,10,-5,-9}; Plane Surface(3) = {3};
            Curve Loop(4) = {2,11,-6,-10}; Plane Surface(4) = {4};
            Curve Loop(5) = {3,12,-7,-11}; Plane Surface(5) = {5};
            Curve Loop(6) = {4,9,-8,-12}; Plane Surface(6) = {6};
            """),
            ("4. Оболочка и объём", """
            Surface Loop(1) = {1,2,3,4,5,6};
            Volume(1) = {1};
            """)
        ]
        
        for title, code in steps:
            with st.expander(title):
                st.code(code, language="python")
    
    with tab2:
        st.markdown("""
        ### Булевы операции с примитивами
        
        Этот метод использует мощное ядро OpenCASCADE.
        """)
        
        code_occ = """
        SetFactory("OpenCASCADE");
        
        // Создаём примитивы
        Box(1) = {0,0,0, 2,2,2};        // куб
        Sphere(2) = {1,1,1, 0.7};        // сфера
        Cylinder(3) = {1,1,-1, 0,0,4, 0.3}; // цилиндр
        
        // Объединение
        BooleanUnion(4) = { Volume{1,2}; Delete; };
        
        // Разность (отверстие)
        BooleanDifference(5) = { Volume{4}; Delete; } { Volume{3}; Delete; };
        """
        st.code(code_occ, language="python")
        
        st.info("""
        **Ключевой момент:** 
        - `Delete` удаляет исходные объекты
        - `BooleanFragments` создаёт конформную сетку на границах раздела
        """)
    
    st.markdown("---")
    
    st.markdown("### 📝 Команды для работы с объёмами")
    
    commands = {
        "Volume": "Volume(tag) = {surface_loop1, surface_loop2, ...};",
        "Surface Loop": "Surface Loop(tag) = {surface1, surface2, ...};",
        "BooleanUnion": "BooleanUnion { Volume{...}; } { Volume{...}; };",
        "BooleanDifference": "BooleanDifference { Volume{...}; } { Volume{...}; };",
        "BooleanIntersection": "BooleanIntersection { Volume{...}; } { Volume{...}; };",
        "BooleanFragments": "BooleanFragments { Volume{...}; } { Volume{...}; };"
    }
    
    for cmd, syntax in commands.items():
        st.code(f"{cmd}: {syntax}", language="python")

# Для автономного тестирования
if __name__ == "__main__":
    show()
