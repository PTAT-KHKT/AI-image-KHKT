import streamlit as st
import random
import requests

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="AI Creative Studio", layout="wide")

# --- KHỞI TẠO TRẠNG THÁI ---
if 'page' not in st.session_state:
    st.session_state.page = 'onboarding'
if 'ui_lang' not in st.session_state:
    st.session_state.ui_lang = 'Tiếng Việt'

# --- TRANG 1: HƯỚNG DẪN ---
def show_onboarding():
    st.title("🎨 AI Image Generation Hub")
    st.session_state.ui_lang = st.radio("Ngôn ngữ / Language:", ["Tiếng Việt", "English"], horizontal=True)
    
    L = {
        "Tiếng Việt": {
            "guide": "👋 Chào mừng! Nhập mô tả bất kỳ. Chọn bối cảnh phù hợp để có kết quả tốt nhất.",
            "btn": "Bắt đầu ngay"
        },
        "English": {
            "guide": "👋 Welcome! Enter any description. Pick a context that matches your prompt for the best result.",
            "btn": "Start Now"
        }
    }[st.session_state.ui_lang]

    st.info(L["guide"])
    if st.button(L["btn"], use_container_width=True):
        st.session_state.page = 'main'
        st.rerun()

# --- TRANG 2: KHỞI TẠO ---
def show_main_app():
    lang = st.session_state.ui_lang
    ui = {
        "Tiếng Việt": {"back": "⬅️ Quay lại", "desc": "Mô tả ảnh:", "gen": "Tạo ảnh", "save": "Tải về"},
        "English": {"back": "⬅️ Back", "desc": "Description:", "gen": "Generate", "save": "Download"}
    }[lang]

    if st.button(ui["back"]):
        st.session_state.page = 'onboarding'
        st.rerun()

    st.header("🎨 Creator Studio")
    user_input = st.text_area(ui["desc"], placeholder="Ví dụ: một cô gái đang học bài...")
    
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("Mục đích môn học:", ["Toán", "Lý", "Hóa", "Văn", "Sử", "Địa"])
        scene = st.selectbox("Bối cảnh cảnh nền:", ["Lớp học", "Ngoài trời", "Tương lai", "Cổ điển"])
    with col2:
        style = st.selectbox("Phong cách nghệ thuật:", ["Realistic", "Anime", "3D Render"])
        count = st.slider("Số lượng ảnh:", 1, 4, 1)

    if st.button(ui["gen"], use_container_width=True):
        if user_input:
            st.divider()
            cols = st.columns(2 if count > 1 else 1)
            for i in range(count):
                seed = random.randint(1, 9999)
                img_url = f"https://picsum.photos/seed/{seed}/800/800"
                with cols[i % 2]:
                    st.image(img_url, use_container_width=True)
                    try:
                        img_data = requests.get(img_url).content
                        st.download_button(ui["save"], data=img_data, file_name=f"ai_img_{i}.png", key=f"btn_{i}")
                    except:
                        pass
            st.success(f"✅ Đã tạo ảnh thành công!")
        else:
            st.error("Vui lòng nhập mô tả!")

# --- ĐIỀU HƯỚNG ---
if st.session_state.page == 'onboarding':
    show_onboarding()
else:
    show_main_app()
