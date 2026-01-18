import streamlit as st
from metaai_api import MetaAI

st.set_page_config(
    page_title="MetaAI Streamlit",
    layout="centered"
)

st.title("🤖 MetaAI – Chat & Video Generator")

# ===============================
# AMBIL COOKIES DARI SECRETS
# ===============================
try:
    cookies = {
        "datr": st.secrets["META_DATr"],
        "abra_sess": st.secrets["META_ABRA_SESS"],
        "dpr": "1.25",
        "wd": "1536x443"
    }
except Exception:
    st.error("❌ Cookies MetaAI belum di-set di secrets.toml")
    st.stop()

# ===============================
# INIT META AI (ONCE)
# ===============================
@st.cache_resource
def init_meta_ai():
    return MetaAI(cookies=cookies)

ai = init_meta_ai()

st.success("✅ MetaAI berhasil di-initialize")

# ===============================
# CHAT SECTION
# ===============================
st.subheader("💬 Chat dengan MetaAI")

chat_prompt = st.text_area(
    "Masukkan pertanyaan",
    value="What's the weather in San Francisco?"
)

if st.button("Kirim Chat"):
    with st.spinner("Mengirim ke MetaAI..."):
        try:
            chat = ai.prompt(chat_prompt, stream=False)
            st.success("✅ Chat Response")
            st.write(chat["message"])
        except Exception as e:
            st.error(f"❌ Chat Error: {e}")

# ===============================
# VIDEO GENERATION
# ===============================
st.subheader("🎥 Generate Video")

video_prompt = st.text_input(
    "Prompt video",
    value="Generate a video of a sunset over mountains"
)

if st.button("Generate Video"):
    with st.spinner("Sedang generate video..."):
        try:
            video = ai.generate_video(video_prompt)

            if video.get("success"):
                st.success("✅ Video berhasil dibuat")
                st.write("Conversation ID:", video["conversation_id"])

                for i, url in enumerate(video["video_urls"], 1):
                    st.markdown(f"**{i}.** [Buka Video]({url})")

            else:
                st.warning("⚠️ Video masih diproses atau URL belum tersedia")

        except Exception as e:
            st.error(f"❌ Video Error: {e}")

st.divider()
st.caption("Running on Streamlit Cloud")
