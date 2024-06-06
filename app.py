import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd
import time
from datetime import datetime as dt
from PIL import Image

# CONFIGURACIPON 

st.set_page_config(
    page_icon='😮‍💨',
    layout = 'wide',
    )

# TITULOS
st.title('Hello :rainbow[fella]')
st.markdown('Yes, heteros and cis are still _unfortunately_ welcome')
st.text('PD: this month u r lgbt+ too')

st.logo('tu_imagen.jpg',link=None)

# VIDEO
st.subheader("You're very welcome for the next piece of art.",divider='rainbow')
video = open('SAOKO.mp4', 'rb')
video_bytes = video.read()
st.video(video_bytes, loop=True, autoplay=True)


# FONDO
# Imágenes 
images = {
    'Nothing said yet': None,
    '4': "tu_imagen_1.jpg",
    "2": "tu_imagen_2.jpg",
    "6": "tu_imagen_3.jpg",
    '3': 'Image JPEG-4F80-9955-78-0.jpeg',
    '5': 'Image JPEG-42D4-AF76-8C-0.jpeg',
    '7': 'Image JPEG-446D-8E2A-0A-0.jpeg',
    '1':'tu_imagen.jpg'
}

# Solicitar al usuario que elija una opción
st.subheader("Today's :violet[horoscope]:",divider='rainbow')
option = st.selectbox("Choose wisely:", list(images.keys()), index=0)

# Mostrar la imagen de fondo correspondiente a la opción seleccionada
if option != 'Nothing said yet':
    image_path = images[option]
    st.image(image_path, width=450)


# DRAWING BOX
# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)

st.subheader('Wanna draw with this _beautiful and vastly inspiring work of art_ :red[music]?', divider='rainbow')
# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)



# TEMPORIZADOR
st.subheader('Want a little surprise?',divider='rainbow')
# Solicitar al usuario que ingrese un número entre 1 y 7
minutes = st.number_input('Choose a number between 1 and 7', min_value=1, max_value=7, step=1)

# Botón para iniciar el temporizador
if st.button('Ok'):
    # Inicializa la barra de progreso y el mensaje de tiempo restante
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Asigna la clase CSS a la barra de progreso
    progress_bar_container = st.empty()
    progress_bar_container.markdown("<div class='rainbow-progress'></div>", unsafe_allow_html=True)

    for i in range(minutes):
        # Calcula el porcentaje completado
        percent_complete = int((i + 1) / minutes * 100)
        progress_bar.progress(percent_complete)
        status_text.text(f"There's {minutes - (i + 1)} seconds left")
        time.sleep(1)  # Espera 1 segundo

    status_text.text('U done b*tch')
    progress_bar.progress(100)
    st.balloons()
