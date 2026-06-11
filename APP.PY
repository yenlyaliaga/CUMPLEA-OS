import streamlit as st
import base64

st.set_page_config(
    page_title="Feliz Cumpleaños Jesenia",
    page_icon="🎂",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);
    background-size: 400% 400%;
}

.titulo{
    text-align:center;
    font-size:70px;
    font-weight:bold;
    color:white;
    margin-top:20px;
    text-shadow: 3px 3px 10px rgba(0,0,0,0.4);
}

.subtitulo{
    text-align:center;
    font-size:28px;
    color:white;
    margin-bottom:20px;
}

.mensaje{
    text-align:center;
    color:white;
    font-size:24px;
    max-width:900px;
    margin:auto;
    line-height:1.8;
}

.video-container{
    display:flex;
    justify-content:center;
    margin-top:30px;
    margin-bottom:30px;
}

.video-frame{
    border-radius:25px;
    overflow:hidden;
    box-shadow:0 0 40px rgba(255,255,255,0.8);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="titulo">🎂 ¡Feliz Cumpleaños Jesenia! 🎂</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">💖 Hoy celebramos a una persona muy especial 💖</div>',
    unsafe_allow_html=True
)

# Leer video
video_file = open("jesenia.mp4", "rb")
video_bytes = video_file.read()
video_base64 = base64.b64encode(video_bytes).decode()

st.markdown(f"""
<div class="video-container">
    <div class="video-frame">
        <video width="500" autoplay muted loop controls>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mensaje">
Hoy es un día muy especial porque celebramos tu cumpleaños. 🌷<br><br>

Gracias por ser una hermana increíble, por tu cariño, tu apoyo y por todos los momentos compartidos. 💕<br><br>

Te deseo un año lleno de salud y muchas bendiciones. 🎁🎉<br><br>

<b>¡Feliz Cumpleaños, Jesenia! 🎂🥳</b>
</div>
""", unsafe_allow_html=True)

st.balloons()
