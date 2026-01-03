import streamlit as st
import random
--- QUẢN LÝ TRẠNG THÁI ---
if 'page' not in st.session_state:
st.session_state.page = 'onboarding'
if 'ui_lang' not in st.session_state:
st.session_state.ui_lang = 'Tiếng Việt'
if 'theme' not in st.session_state:
st.session_state.theme = 'Light'
def switch_page(page_name):
st.session_state.page = page_name
--- TRANG 1: HƯỚNG DẪN & CÀI ĐẶT CHUNG ---
def show_onboarding():
# Giao diện sáng/tối
theme_icon = "🌙" if st.session_state.theme == 'Light' else "☀️"
if st.button(f"{theme_icon} Chế độ Sáng/Tối"):
st.session_state.theme = 'Dark' if st.session_state.theme == 'Light' else 'Light'
st.rerun()
codeCode
st.title("🚀 AI Generation Hub")
# Chọn ngôn ngữ UI
st.session_state.ui_lang = st.radio(
    "Ngôn ngữ / Language:", ["Tiếng Việt", "English"], horizontal=True
)

L = {
    "Tiếng Việt": {
        "h1": "Hướng dẫn sử dụng",
        "guide": """
        * 🖋️ **Mô tả:** Nhập chính xác những gì bạn muốn (Ví dụ: 'a girl studying').
        * 📚 **Môn học:** Chọn môn học bạn muốn áp dụng (để phân loại mục đích).
        * 🏞️ **Cảnh nền:** Chọn bối cảnh cho bức ảnh (Trong nhà, Ngoài trời...).
        * 🎨 **Phong cách:** Chọn định dạng nghệ thuật (Anime, Realistic...).
        """,
        "btn": "Tiếp theo ➡️"
    },
    "English": {
        "h1": "User Guide",
        "guide": """
        * 🖋️ **Description:** Enter exactly what you want (e.g., 'a girl studying').
        * 📚 **Subject:** Pick a subject for classification purposes.
        * 🏞️ **Scene:** Choose the background style (Indoor, Outdoor...).
        * 🎨 **Style:** Choose the art format (Anime, Realistic...).
        """,
        "btn": "Next ➡️"
    }
}[st.session_state.ui_lang]

st.info(L["guide"])
st.button(L["btn"], on_click=switch_page, args=('main',), use_container_width=True)
--- TRANG 2: KHỞI TẠO ---
def show_main_app():
lang = st.session_state.ui_lang
ui = {
"Tiếng Việt": {
"back": "⬅️ Quay lại",
"title": "🎨 Khởi tạo hình ảnh",
"desc_label": "Nhập mô tả ảnh:",
"subj_label": "Mục đích môn học:",
"scene_label": "Phong cách cảnh nền:",
"art_label": "Phong cách nghệ thuật:",
"count_label": "Số lượng ảnh:",
"btn_gen": "Tạo ảnh",
"res_title": "📝 Thông tin ảnh (Tiếng Việt):"
},
"English": {
"back": "⬅️ Back",
"title": "🎨 Image Generator",
"desc_label": "Description:",
"subj_label": "Subject Purpose:",
"scene_label": "Environment Style:",
"art_label": "Art Style:",
"count_label": "Quantity:",
"btn_gen": "Generate",
"res_title": "📝 Image Details (English):"
}
}[lang]
codeCode
st.button(ui["back"], on_click=switch_page, args=('onboarding',))
st.header(ui["title"])

col1, col2 = st.columns([2, 1])
with col1:
    user_desc = st.text_input(ui["desc_label"], placeholder="a girl studying...")
    # Lựa chọn ngôn ngữ cho Prompt gửi AI
    p_lang = st.selectbox("Ngôn ngữ mô tả gửi AI (Prompt Language):", ["English", "Tiếng Việt"])
with col2:
    subject = st.selectbox(ui["subj_label"], ["Toán", "Lý", "Hóa", "Văn", "Sử", "Địa"])
    scene_style = st.selectbox(ui["scene_label"], ["Trong lớp học", "Ngoài trời", "Tương lai", "Cổ điển", "Vũ trụ"])
    art_style = st.selectbox(ui["art_label"], ["Realistic", "Anime", "3D Render", "Sketch"])
    img_count = st.select_slider(ui["count_label"], options=[1, 2, 3, 4])
if st.button(ui["btn_gen"], use_container_width=True):
    if user_desc:
        with st.spinner("Đang tạo..."):
            st.divider()
            grid = st.columns(2 if img_count > 1 else 1)
            for i in range(img_count):
                seed = random.randint(1, 99999)
                img_url = f"https://picsum.photos/seed/{seed}/800/800"
                grid[i % 2].image(img_url, use_container_width=True, caption=f"Img {i+1}")
            
            # HIỂN THỊ MÔ TẢ ĐÚNG NGÔN NGỮ UI
            st.success(ui["res_title"])
            # Logic: Mô tả bên dưới sẽ hiển thị theo ngôn ngữ UI bạn đã chọn
            if lang == "Tiếng Việt":
                st.write(f"**Nội dung:** {user_desc}")
                st.write(f"**Mục đích:** Môn {subject}")
                st.write(f"**Cảnh nền:** {scene_style} | **Nghệ thuật:** {art_style}")
            else:
                st.write(f"**Content:** {user_desc}")
                st.write(f"**Purpose:** {subject} Subject")
                st.write(f"**Environment:** {scene_style} | **Art Style:** {art_style}")
    else:
        st.error("Missing description!")
--- RENDER THEME ---
if st.session_state.theme == 'Dark':
st.markdown("<style>body { background-color: #1E1E1E; color: white; }</style>", unsafe_allow_html=True)
if st.session_state.page == 'onboarding':
show_onboarding()
else:
show_main_app()
