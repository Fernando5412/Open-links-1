import streamlit as st
import streamlit.components.v1 as components

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

        # Botón para abrir los enlaces automáticamente
        if st.button("Abrir Enlaces Automáticamente 🚀"):
            # Generar el código JavaScript para abrir los enlaces en nuevas pestañas
            js_code = "<script>\n"
            for link in links:
                js_code += f'window.open("{link}", "_blank");\n'
            js_code += "</script>"

            # Inyectar el código JavaScript con `components.html()`
            components.html(js_code)
    else:
        st.error("El archivo está vacío o no contiene enlaces.")
