import streamlit as st
import CodeChapter.Chapter05 as c5
from PIL import Image
import cv2 as cv2


def Layout(imgin, imgout):
    col1, col2 = st.columns(2)
    col1.header(':red[Before]')
    col1.image(imgin, use_column_width=True)
    col2.header(':red[After]')
    col2.image(imgout, use_column_width=True)


def onCreateMotionNoise():
    path = 'Image/Digital_image_processing.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c5.CreateMotionNoise(imgin)
    Layout(imgin, imgout)


def onDenoiseMotion():
    path = 'Image/Digital_noise.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c5.DenoiseMotion(imgin)
    Layout(imgin, imgout)


def onDenoisestMotion():
    path = 'Image/Denoise.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    temp = cv2.medianBlur(imgin, 7)
    global imgout
    imgout = c5.DenoiseMotion(temp)
    Layout(imgin, imgout)
