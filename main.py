import streamlit as st
import webbrowser
import time

# Título de la aplicación
st.title("Abrir Enlaces desde un Archivo")

# Subir archivo
uploaded_file = st.file_uploader("Sube un archivo .txt con los enlaces", type=["txt"])

if uploaded_file is not None:
    # Leer contenido del archivo
    links = uploaded_file.read().decode("utf-8").splitlines()
    
    # Filtrar enlaces vacíos
    links = [link.strip() for link in links if link.strip()]
    
    if links:
        st.write("### Enlaces encontrados:")
        for link in links:
            st.write(f"- {link}")

        # Botón para abrir los enlaces
        if st.button("Abrir Enlaces"):
            for link in links:
                webbrowser.open(link)
                time.sleep(1)  # Esperar 1 segundo entre cada enlace
            st.success("Enlaces abiertos correctamente 🚀")
    else:
        st.error("El archivo está vacío o no contiene enlaces.")
