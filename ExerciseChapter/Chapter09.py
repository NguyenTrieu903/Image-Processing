import streamlit as st
import CodeChapter.Chapter09 as c9
from PIL import Image
import cv2 as cv2


def Layout(imgin, imgout):
    col1, col2 = st.columns(2)
    col1.header(':red[Before]')
    col1.image(imgin, use_column_width=True)
    col2.header(':red[After]')
    col2.image(imgout, use_column_width=True)


def onConnectedComponent():
    path = 'Image/ConnectedComponent.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c9.ConnectedComponent(imgin)
    Layout(imgin, imgout)


def onCountRice():
    path = 'Image/Count_Rice.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c9.CountRice(imgin)
    Layout(imgin, imgout)
