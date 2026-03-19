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

st.title("Установка на различные ОС")
 
tab = st.tabs([
        "Windows", 
        "Linux",
        "MacOS"
        ])
  
with tab[0]:
    st.markdown("##### Установка в Windows")
    
    st.subheader("Способ А: Официальный установщик")
    st.markdown("""    
    1. Перейдите на [gmsh.info](https://gmsh.info/    )
    2. Раздел **Download** → Windows (`.msi`)
    3. Запустите установщик
    4. Отметьте галочку:
       > `Add Gmsh to the PATH for all users`
    5. Завершите установку
    """)
    st.info("Это позволит запускать Gmsh из командной строки и использовать Python API без дополнительных настроек.")
    
    st.subheader("Способ Б: Портативная версия")
    st.markdown("""
    **Для использования без установки**
        
    1. Скачайте архив `.zip` с сайта
    2. Распакуйте в удобную папку, например:
       ```
       C:\\Programs\\gmsh
       ```
    3. *(Опционально)* Добавьте в PATH вручную:
       - Панель управления → Система → Переменные среды
       - В `Path` добавьте: `C:\\Programs\\gmsh\\bin`
    """)
    st.code(r"C:\Programs\gmsh\bin\gmsh.exe", language="bash", line_numbers=False)
    st.warning("Без добавления в PATH запуск возможен только через полный путь к исполняемому файлу.")
    
    # Способ В: Сборка из исходников (для единообразия с Linux)
    with st.expander("Способ В: Сборка из исходников", expanded=False):
        st.markdown("""
        Если нужна специфическая конфигурация (PETSc, MPI, особые компиляторы):
        
        ```bash
        # Установка зависимостей (пример для Windows + MSYS2)
        # Требуется: cmake, gcc, python, git
        
        # Клонирование репозитория
        git clone https://gitlab.onelab.info/gmsh/gmsh.git  
        cd gmsh
        
        # Создание и настройка сборки
        mkdir build && cd build
        cmake .. -DCMAKE_BUILD_TYPE=Release -DENABLE_BUILD_SHARED=OFF
        
        # Компиляция и установка
        cmake --build . --config Release --parallel
        ```
        """)
    
with tab[1]:
    st.markdown("##### Установка в Linux")
    
    st.subheader("Способ А: Менеджер пакетов") 
        
    col_ubuntu, col_fedora, col_arch = st.columns(3)
        
    with col_ubuntu:
        st.markdown("**Ubuntu / Debian**")
        st.code("sudo apt update\nsudo apt install gmsh", language="bash")
        
    with col_fedora:
        st.markdown("**Fedora / CentOS**")
        st.code("sudo dnf install gmsh", language="bash")
        
    with col_arch:
        st.markdown("**Arch Linux**")
        st.code("sudo pacman -S gmsh", language="bash")
    
    # Способ Б: Официальные бинарники
    st.subheader("Способ Б: Официальные бинарные файлы")
    st.markdown("Позволяет получить последнюю стабильную версию напрямую от разработчиков.")
        
    st.markdown("#### Пошаговая инструкция:")
        
    step1, step2, step3, step4 = st.columns(4)
        
    with step1:
        st.markdown("**Скачать**")
        st.code("wget https://gmsh.info/bin/Linux/gmsh-<ver>-Linux64.tgz", language="bash", line_numbers=False)
        
    with step2:
        st.markdown("**Распаковать**")
        st.code("tar -xzf gmsh-*.tgz", language="bash", line_numbers=False)
        
    with step3:
        st.markdown("**Переместить**")
        st.code("sudo mv gmsh-*-Linux64 /opt/gmsh", language="bash", line_numbers=False)
        
    with step4:
        st.markdown("**Создать ссылку**")
        st.code("sudo ln -s /opt/gmsh/bin/gmsh /usr/local/bin/gmsh", language="bash", line_numbers=False)
        
    st.success("Теперь `gmsh` доступен в терминале из любой директории.")
    
    # Способ В: Сборка из исходников
    with st.expander("Способ В: Сборка из исходников", expanded=False):
        st.markdown("""
        Если нужна специфическая конфигурация (PETSc, MPI, особые компиляторы):
        
        ```bash
        # Установка зависимостей (пример для Ubuntu)
        sudo apt install build-essential cmake libgl1-mesa-dev libglu1-mesa-dev
        
        # Клонирование репозитория
        git clone https://gitlab.onelab.info/gmsh/gmsh.git    
        cd gmsh
        
        # Создание и настройка сборки
        mkdir build && cd build
        cmake .. -DCMAKE_BUILD_TYPE=Release
        
        # Компиляция и установка
        make -j$(nproc)
        sudo make install
        ```
        """)
    
with tab[2]:
    st.markdown("##### Установка в MacOS")
    
    st.subheader("Способ А: Менеджер пакетов")
        
    col_brew, col_macports = st.columns(2)
        
    with col_brew:
        st.markdown("**Homebrew**")
        st.code("brew install gmsh", language="bash")
        
    with col_macports:
        st.markdown("**MacPorts**")
        st.code("sudo port install gmsh", language="bash")
    
    # Способ Б: Официальные бинарники
    st.subheader("Способ Б: Официальные бинарные файлы")
        
    st.markdown("#### Пошаговая инструкция:")
        
    step1, step2, step3 = st.columns(3)
        
    with step1:
        st.markdown("**Скачать**")
        st.code("wget https://gmsh.info/bin/MacOS/gmsh-<ver>-MacOS-universal.dmg", language="bash", line_numbers=False)
        
    with step2:
        st.markdown("**Установить**")
        st.code("open gmsh-*.dmg\n# Перетащите Gmsh в /Applications", language="bash", line_numbers=False)
        
    with step3:
        st.markdown("**Добавить в PATH**")
        st.code("echo 'export PATH=\"/Applications/gmsh.app/Contents/MacOS:$PATH\"' >> ~/.zshrc\nsource ~/.zshrc", language="bash", line_numbers=False)
        
    st.success("Теперь `gmsh` доступен в терминале из любой директории.")
    
    # Способ В: Сборка из исходников
    with st.expander("Способ В: Сборка из исходников", expanded=False):
        st.markdown("""
        Если нужна специфическая конфигурация (PETSc, MPI, особые компиляторы):
        
        ```bash
        # Установка зависимостей через Homebrew
        brew install cmake gcc llvm
        
        # Клонирование репозитория
        git clone https://gitlab.onelab.info/gmsh/gmsh.git    
        cd gmsh
        
        # Создание и настройка сборки
        mkdir build && cd build
        cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++
        
        # Компиляция и установка
        make -j$(sysctl -n hw.ncpu)
        sudo make install
        ```
        """)
