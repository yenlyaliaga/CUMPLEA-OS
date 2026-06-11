st.markdown("""
<style>

.balloon {
    position: fixed;
    bottom: -150px;
    width: 80px;
    height: 100px;
    border-radius: 50%;
    opacity: 0.8;
    animation: float 15s linear infinite;
}

.balloon:before {
    content: "";
    position: absolute;
    width: 2px;
    height: 100px;
    background: white;
    left: 50%;
    top: 100px;
}

.b1 { left: 5%; background: #ff4d6d; animation-duration: 12s; }
.b2 { left: 20%; background: #ffbe0b; animation-duration: 15s; }
.b3 { left: 35%; background: #8338ec; animation-duration: 18s; }
.b4 { left: 50%; background: #3a86ff; animation-duration: 13s; }
.b5 { left: 65%; background: #06d6a0; animation-duration: 16s; }
.b6 { left: 80%; background: #fb5607; animation-duration: 14s; }
.b7 { left: 92%; background: #ff006e; animation-duration: 17s; }

@keyframes float {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(-120vh);
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
