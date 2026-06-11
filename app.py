import streamlit as st

st.set_page_config(
    page_title="Feliz Cumpleaños Jesenia",
    page_icon="🎂",
    layout="wide"
)

# ==========================
# ESTILOS
# ==========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        -45deg,
        #ff9a9e,
        #fad0c4,
        #fbc2eb,
        #a18cd1
    );
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.titulo{
    text-align:center;
    color:black;
    font-size:clamp(2rem, 6vw, 4.5rem);
    font-weight:bold;
    margin-top:20px;
}

.subtitulo{
    text-align:center;
    color:black;
    font-size:clamp(1.2rem, 3vw, 2rem);
    margin-bottom:20px;
}

.mensaje{
    text-align:center;
    color:black;
    font-size:clamp(1rem, 2vw, 1.5rem);
    max-width:900px;
    margin:auto;
    line-height:1.8;
    padding:20px;
    font-weight:500;
}

/* Reducir tamaño del video */
[data-testid="stVideo"]{
    max-width:500px;
    margin:auto;
    border-radius:20px;
    overflow:hidden;
}

/* GLOBOS */

.balloon{
    position:fixed;
    bottom:-150px;
    width:80px;
    height:100px;
    border-radius:50%;
    opacity:0.85;
    z-index:0;
}

.balloon:before{
    content:'';
    position:absolute;
    width:2px;
    height:100px;
    background:white;
    left:50%;
    top:100px;
}

.b1{left:5%;background:#ff4d6d;animation:float 12s linear infinite;}
.b2{left:20%;background:#ffbe0b;animation:float 15s linear infinite;}
.b3{left:35%;background:#8338ec;animation:float 18s linear infinite;}
.b4{left:50%;background:#3a86ff;animation:float 13s linear infinite;}
.b5{left:65%;background:#06d6a0;animation:float 16s linear infinite;}
.b6{left:80%;background:#fb5607;animation:float 14s linear infinite;}
.b7{left:92%;background:#ff006e;animation:float 17s linear infinite;}

@keyframes float{
    0%{
        transform:translateY(0);
    }
    100%{
        transform:translateY(-130vh);
    }
}

@media (max-width:768px){

    .balloon{
        width:50px;
        height:65px;
    }

    .balloon:before{
        height:60px;
        top:65px;
    }

    [data-testid="stVideo"]{
        max-width:300px;
    }
}

</style>

<div class="balloon b1"></div>
<div class="balloon b2"></div>
<div class="balloon b3"></div>
<div class="balloon b4"></div>
<div class="balloon b5"></div>
<div class="balloon b6"></div>
<div class="balloon b7"></div>

""", unsafe_allow_html=True)

# ==========================
# TITULO
# ==========================

st.markdown("""
<div class="titulo">
🎂 ¡Feliz Cumpleaños Jesenia! 🎂
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitulo">
💖 Hoy celebramos a una persona muy especial 💖
</div>
""", unsafe_allow_html=True)

# ==========================
# VIDEO CENTRADO
# ==========================

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.video("jesenia.mp4")

# ==========================
# MENSAJE
# ==========================

st.markdown("""
<div class="mensaje">

🌷 Hoy es un día muy especial porque celebramos tu vida. 🌷

<br><br>

Gracias por ser una hermana increíble,
por tu cariño, tu apoyo y todos los momentos compartidos. 💕

<br><br>

Te deseo un año lleno de alegría,
salud, amor y muchas bendiciones. 🎁🎉

<br><br>

❤️ Que este nuevo año de vida esté lleno de momentos inolvidables. ❤️

<br><br>

🎂🥳 ¡Feliz Cumpleaños Jesenia! 🥳🎂

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🎁 Mensaje Sorpresa"):
    st.success(
        "Jesenia, gracias por ser una hermana maravillosa. "
        "Que Dios te bendiga siempre y que todos tus sueños se hagan realidad. ❤️"
    )
