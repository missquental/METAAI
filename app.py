import streamlit as st
from metaai_wrapper import MetaAIWrapper

st.set_page_config("MetaAI Cloud", layout="centered")
st.title("🤖 MetaAI – Cloud Safe")

# =========================
# INIT
# =========================
try:
    COOKIE = st.secrets["META_COOKIE"]
except Exception:
    st.error("❌ Cookie MetaAI belum di-set")
    st.stop()

@st.cache_resource
def load_ai():
    return MetaAIWrapper(COOKIE)

ai = load_ai()
st.success("✅ MetaAI wrapper siap (REAL MODE)")

# =========================
# CHAT
# =========================
st.subheader("💬 Chat")

prompt_chat = st.text_area(
    "Prompt Chat",
    "What's the weather in San Francisco?"
)

if st.button("Kirim Chat"):
    with st.spinner("Menghubungi MetaAI..."):
        try:
            reply = ai.chat(prompt_chat)
            st.success("Response")
            st.write(reply)
        except Exception as e:
            st.error(str(e))

# =========================
# VIDEO
# =========================
st.subheader("🎥 Generate Video")

prompt_video = st.text_input(
    "Prompt Video",
    "Generate a video of a sunset over mountains"
)

if st.button("Generate Video"):
    with st.spinner("Request video..."):
        try:
            res = ai.generate_video(prompt_video)
            cid = res["conversation_id"]

            st.info(f"Conversation ID: {cid}")
            st.write("Menunggu video...")

            urls = ai.poll_video(cid)

            if urls:
                st.success("🎉 Video siap!")
                for i, u in enumerate(urls, 1):
                    st.markdown(f"**{i}.** [Buka Video]({u})")
            else:
                st.warning("⚠️ Video belum siap / masih diproses")

        except Exception as e:
            st.error(str(e))
