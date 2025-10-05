import streamlit as st
import asyncio
from manager import TourManager
from agents import set_default_openai_key
import tempfile
import os
import openai

# ---------- Audio (TTS) ----------
def tts(text, api_key, language="en"):
    try:
        client = openai.OpenAI(api_key=api_key)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            speech_file_path = tmp_file.name

        # Pass language hint to the TTS model
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=f"Language: {language}. {text}",
        )
        response.stream_to_file(speech_file_path)
        return speech_file_path
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

# ---------- Async helper ----------
def run_async(func, *args, **kwargs):
    try:
        return asyncio.run(func(*args, **kwargs))
    except RuntimeError:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(func(*args, **kwargs))

# ---------- Page Config ----------
st.set_page_config(
    page_title="SonicGuide AI • Immersive Audio Tours",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- White Background Theme + Dark Blue Text ----------
st.markdown("""
<style>
/* App + Main background */
html, body, [data-testid="stAppViewContainer"], .main {
    background-color: #FFFFFF !important; /* white */
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #F8F9FA !important; /* light gray */
    color: #0B3D91 !important;            /* dark blue text */
    border-right: 1px solid #DEE2E6 !important;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #0B3D91 !important;            /* dark navy blue */
    font-weight: 800 !important;
}

/* Generic text */
p, span, div, label {
    color: #0B3D91 !important;
}

/* Cards / containers */
.custom-card {
    background-color: #F8F9FA !important; /* light gray */
    border: 1px solid #DEE2E6 !important;
    border-radius: 16px !important;
    padding: 20px !important;
    margin-bottom: 18px !important;
}

/* Inputs (text/select/multiselect) */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background-color: #FFFFFF !important; /* white */
    color: #0B3D91 !important;
    border: 1px solid #9BC0FF !important;
    border-radius: 10px !important;
}

/* Placeholder (hint) */
::placeholder {
    color: #5C7EBF !important;            /* medium blue hint */
    opacity: 1 !important;
}

/* Dropdown menu panel + options */
.stSelectbox [role="listbox"] div,
.stMultiSelect [role="listbox"] div {
    background-color: #FFFFFF !important;
    color: #0B3D91 !important;
}

/* Multiselect tags (interests) */
.stMultiSelect [data-baseweb="tag"] {
    background-color: #BBD2FF !important; /* medium light blue chip */
    color: #0B3D91 !important;            /* dark blue text */
    font-weight: 700 !important;
    border-radius: 8px !important;
}

/* Buttons (light blue background, dark blue text) */
.stButton > button, .stDownloadButton > button {
    background-color: #C7DDFF !important;
    color: #0B3D91 !important;
    border: 1px solid #9BC0FF !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: 10px 20px !important;
    transition: 0.25s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background-color: #BBD2FF !important;
    transform: translateY(-1px);
}

/* Slider track: red → blue gradient */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #E63946, #1D4ED8) !important; /* red to blue */
    border-radius: 8px !important;
}
/* Slider handle (thumb) */
[data-baseweb="slider"] [role="slider"] {
    background-color: #0B3D91 !important;  /* dark blue handle */
    box-shadow: none !important;
    border: 2px solid #9BC0FF !important;
}

/* Alerts */
.stSuccess, .stError, .stInfo, .stWarning {
    background-color: #F8F9FA !important;
    color: #0B3D91 !important;
    border: 1px solid #DEE2E6 !important;
    border-radius: 12px !important;
}

/* Audio player */
audio {
    width: 100% !important;
    border-radius: 10px !important;
    background: #F8F9FA !important;
}

/* Footer */
.footer-text {
    color: #0B3D91 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("<h1 style='text-align:center;'>🎧 SonicGuide AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Immersive Audio Experiences</p>", unsafe_allow_html=True)

    st.markdown("### 🔐 API Key")
    api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state["OPENAI_API_KEY"])
    if api_key:
        st.session_state["OPENAI_API_KEY"] = api_key
        try:
            set_default_openai_key(api_key)
            st.success("API key set")
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")

    # Slider heading styled to match red→blue gradient concept (dark blue text)
    st.markdown("### ⚙️ Tour Duration")

    duration = st.slider("Select duration (minutes)", min_value=1, max_value=60, value=15, step=5)

    voice_style = st.selectbox("Voice Personality", ["Friendly", "Professional", "Energetic"])

    st.markdown("### 🌐 Language")
    language = st.selectbox(
        "Choose Language for Audio",
        ["en", "fr", "es", "de", "it", "zh", "ar", "ur"],
        index=0
    )

    st.markdown("---")
    st.markdown("<p style='text-align:center;'>Powered by OpenAI</p>", unsafe_allow_html=True)

# ---------- Main ----------
st.markdown("<h1 style='text-align:center;'>🌍 SonicGuide AI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Transform Your Journey with Intelligent Audio Tours</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='custom-card'><h3>📍 Enter Destination</h3>", unsafe_allow_html=True)
    location = st.text_input(
        "destination_input",
        placeholder="✍️ Type your destination here (e.g., Paris, Kyoto Temples, Lahore Fort...)",
        label_visibility="collapsed"
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='custom-card'><h3>🎯 Choose Interests</h3>", unsafe_allow_html=True)
    interests = st.multiselect(
        "interests_input",
        ["History", "Architecture", "Food", "Culture"],
        default=["History", "Architecture"],
        label_visibility="collapsed"
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Action ----------
if st.button("🚀 Generate Tour", use_container_width=True):
    if not st.session_state["OPENAI_API_KEY"]:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not location:
        st.error("Please enter a destination.")
    elif not interests:
        st.error("Please choose at least one interest.")
    else:
        with st.spinner(f"Creating a {duration}-minute tour for {location}..."):
            try:
                mgr = TourManager()
                # (Ensure your TourManager expects simple strings for interests)
                final_tour_content = run_async(mgr.run, location, interests, duration)

                if final_tour_content:
                    st.markdown("<div class='custom-card'><h3>📝 Tour Preview</h3>", unsafe_allow_html=True)
                    st.text_area("", final_tour_content, height=300, label_visibility="collapsed")
                    st.markdown("</div>", unsafe_allow_html=True)

                    # Audio generation
                    audio_file = tts(final_tour_content, st.session_state["OPENAI_API_KEY"], language=language)
                    if audio_file and os.path.exists(audio_file):
                        st.success("Audio generated")
                        st.audio(audio_file, format="audio/mp3")
                        with open(audio_file, "rb") as f:
                            st.download_button(
                                "💾 Download Audio (MP3)",
                                f,
                                file_name=f"sonicguide_{location.lower().replace(' ', '_')}_tour.mp3",
                                mime="audio/mp3",
                                use_container_width=True
                            )
                        try:
                            os.unlink(audio_file)
                        except:
                            pass
                    else:
                        st.error("Audio generation failed. Please check your API key and try again.")
            except Exception as e:
                st.error(f"Error generating tour: {e}")

# ---------- Footer ----------
st.markdown("<p class='footer-text' style='text-align:center; margin-top: 24px;'>© 2025 SonicGuide AI</p>", unsafe_allow_html=True)