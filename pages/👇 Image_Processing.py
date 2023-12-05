import streamlit as st
import ExerciseChapter.Chapter03 as c3
import ExerciseChapter.Chapter04 as c4
import ExerciseChapter.Chapter05 as c5
import ExerciseChapter.Chapter09 as c9

app_mode = st.sidebar.selectbox(
    '👇 Image Processing Select', ['Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 9'])

page_bg_img = '''
    <style>
    .stApp {
        background: url("https://cutewallpaper.org/21x/2olaxzatm/25-Awesome-Web-Background-Animation-Effects-Css-animation-.jpg");
        background-size: cover;
    }
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
if app_mode == 'Chapter 3':
    with st.sidebar.container():
        st.header("Biến đổi độ sáng và lọc trong không gian")
        ques = st.radio(
            "Choose one", ['3.1 Làm âm ảnh (Negative)', '3.2 Logarit ảnh', '3.3 Lũy thừa ảnh', '3.4 Biến đổi tuyến tính từng phần',
                           '3.5 Histogram', '3.6 Cân bằng Histogram', '3.7 Cân bằng Histogram của ảnh màu', '3.8 Local Histogram', '3.9 Thống kê histogram',
                           '3.10 Lọc box', '3.11 Lọc Gauss', '3.12 Phân ngưỡng', '3.13 Lọc median', '3.14 Sharpen', '3.15 Gradient'
                           ])
    if ques == '3.1 Làm âm ảnh (Negative)':
        st.subheader(':blue[Làm âm ảnh (Negative)]')
        c3.OnNegative()
    elif ques == '3.2 Logarit ảnh':
        st.subheader(':blue[Logarit ảnh]')
        c3.OnLogarit()
    elif ques == '3.3 Lũy thừa ảnh':
        st.subheader(':blue[Lũy thừa ảnh]')
        c3.OnPower()
    elif ques == '3.4 Biến đổi tuyến tính từng phần':
        st.subheader(':blue[Biến đổi tuyến tính từng phần]')
        c3.OnPiecewiseLinear()
    elif ques == '3.5 Histogram':
        st.subheader(':blue[Histogram]')
        c3.OnHistogram()
    elif ques == '3.6 Cân bằng Histogram':
        st.subheader(':blue[Cân bằng Histogram]')
        c3.onHistEqual()
    elif ques == '3.7 Cân bằng Histogram của ảnh màu':
        st.subheader(':blue[Cân bằng Histogram của ảnh màu]')
        c3.onHistEqualColor()
    elif ques == '3.8 Local Histogram':
        st.subheader(':blue[Local Histogram]')
        c3.onLocalHist()
    elif ques == '3.9 Thống kê histogram':
        st.subheader(':blue[Thống kê histogram]')
        c3.onHistStat()
    elif ques == '3.10 Lọc box':
        st.subheader(':blue[Lọc box]')
        c3.onBoxFilter()
    elif ques == '3.11 Lọc Gauss':
        st.subheader(':blue[Lọc Gauss]')
        c3.onLowpassGauss()
    elif ques == '3.12 Phân ngưỡng':
        st.subheader(':blue[Phân ngưỡng]')
        c3.onThreshold()
    elif ques == '3.13 Lọc median':
        st.subheader(':blue[Lọc median]')
        c3.onMedianFilter()
    elif ques == '3.14 Sharpen':
        st.subheader(':blue[Sharpen]')
        c3.onSharpen()
    elif ques == '3.15 Gradient':
        st.subheader(':blue[Gradient]')
        c3.onGradient()
elif app_mode == 'Chapter 4':
    with st.sidebar.container():
        st.header("Lọc trong miền tần số")
        ques = st.radio(
            "Choose one", ['4.1 Spectrum', '4.2 Lọc trong miền tần số - highpass filter', '4.3 Vẽ bộ lọc Notch Reject'])
    if ques == '4.1 Spectrum':
        st.subheader(':blue[Spectrum]')
        c4.onSpectrum()
    elif ques == '4.2 Lọc trong miền tần số - highpass filter':
        st.subheader(':blue[Lọc trong miền tần số - highpass filter]')
        c4.onFrequencyFilter()
    elif ques == '4.3 Vẽ bộ lọc Notch Reject':
        st.subheader(':blue[Vẽ bộ lọc Notch Reject]')
        c4.onDrawNotchRejectFilter()
elif app_mode == 'Chapter 5':
    with st.sidebar.container():
        st.header("Khôi phục ảnh")
        ques = st.radio(
            "Choose one", ['5.1 Tạo nhiễu chuyển động', '5.2 Gỡ nhiễu của ảnh có ít nhiễu', '5.3 Gỡ nhiễu của ảnh có nhiều nhiễu'])
    if ques == '5.1 Tạo nhiễu chuyển động':
        st.subheader(':blue[Tạo nhiễu chuyển động]')
        c5.onCreateMotionNoise()
    elif ques == '5.2 Gỡ nhiễu của ảnh có ít nhiễu':
        st.subheader(':blue[Gỡ nhiễu của ảnh có ít nhiễu]')
        c5.onDenoiseMotion()
    elif ques == '5.3 Gỡ nhiễu của ảnh có nhiều nhiễu':
        st.subheader(':blue[Gỡ nhiễu của ảnh có nhiều nhiễu]')
        c5.onDenoisestMotion()
elif app_mode == 'Chapter 9':
    with st.sidebar.container():
        st.header("Xử lý ảnh hình thái")
        ques = st.radio(
            "Choose one", ['9.1 Đếm thành phần liên thông của miếng phi lê gà (Connected Component)', '9.2 Đếm hạt gạo (Count Rice)'])
    if ques == '9.1 Đếm thành phần liên thông của miếng phi lê gà (Connected Component)':
        st.subheader(
            ':blue[Đếm thành phần liên thông của miếng phi lê gà (Connected Component)]')
        c9.onConnectedComponent()
    elif ques == '9.2 Đếm hạt gạo (Count Rice)':
        st.subheader(
            ':blue[Đếm hạt gạo (Count Rice)]')
        c9.onCountRice()
