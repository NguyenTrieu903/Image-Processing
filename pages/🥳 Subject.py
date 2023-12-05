import streamlit as st

st.set_page_config(
    page_title="Digital Image Processing",
    page_icon="👋",
)

st.write("# :orange[Welcome to Digital Image Processing!] 😙")
page_bg_img = '''
    <style>
    .stApp {
        background: url("https://cutewallpaper.org/21x/2olaxzatm/25-Awesome-Web-Background-Animation-Effects-Css-animation-.jpg");
        background-size: cover;
    }
    </style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(
    """
    :orange[Xử lý ảnh số là một môn học trong lĩnh vực trí tuệ nhân tạo và công nghệ thông tin. 
    Nó tập trung vào việc áp dụng các phương pháp và thuật toán để xử lý và phân tích ảnh số. Môn học này cung cấp các công cụ và kỹ thuật cho việc nhận dạng, trích xuất thông tin và hiểu nội dung của các hình ảnh số.]
"""
)
