import streamlit as st
import CodeChapter.Chapter04 as c4
from PIL import Image
import cv2 as cv2


def Layout(imgin, imgout):
    col1, col2 = st.columns(2)
    col1.header(':red[Before]')
    col1.image(imgin, use_column_width=True)
    col2.header(':red[After]')
    col2.image(imgout, use_column_width=True)


def onSpectrum():
    path = 'Image/Spectrum.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c4.Spectrum(imgin)
    Layout(imgin, imgout)


def onFrequencyFilter():
    path = 'Image/FrequencyFilter.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c4.FrequencyFilter(imgin)
    Layout(imgin, imgout)


def onDrawNotchRejectFilter():
    global imgout
    imgout = c4.DrawNotchRejectFilter()
    st.image(imgout, use_column_width=True)
