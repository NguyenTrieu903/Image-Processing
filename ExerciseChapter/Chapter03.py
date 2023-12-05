import streamlit as st
import CodeChapter.chapter3 as c3
from PIL import Image
import cv2 as cv2


def Layout(imgin, imgout):
    col1, col2 = st.columns(2)
    col1.header(':red[Before]')
    col1.image(imgin, use_column_width=True)
    col2.header(':red[After]')
    col2.image(imgout, use_column_width=True)


def OnNegative():
    path = 'Image/Negative.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Negative(imgin)
    Layout(imgin, imgout)


def OnLogarit():
    path = 'Image/Logarit_1.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Logarit(imgin)
    Layout(imgin, imgout)


def OnPower():
    path = 'Image/Power.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Power(imgin)
    Layout(imgin, imgout)


def OnPiecewiseLinear():
    path = 'Image/Bear.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.PiecewiseLinear(imgin)
    Layout(imgin, imgout)


def OnHistogram():
    path = 'Image/Histogram.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Histogram(imgin)
    Layout(imgin, imgout)


def OnHistogram():
    path = 'Image/Histogram.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Histogram(imgin)
    Layout(imgin, imgout)


def onHistEqual():
    path = 'Image/Bear.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.HistEqual(imgin)
    Layout(imgin, imgout)


def onHistEqual():
    path = 'Image/Bear.jpg'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.HistEqual(imgin)
    Layout(imgin, imgout)


def onHistEqualColor():
    path = 'Image/EqualHistColor.tif'
    imgin = cv2.imread(path, cv2.IMREAD_COLOR)
    global imgout
    imgout = c3.HistEqualColor(imgin)
    Layout(imgin, imgout)


def onLocalHist():
    path = 'Image/LocalHist.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.LocalHist(imgin)
    Layout(imgin, imgout)


def onHistStat():
    path = 'Image/LocalHist.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.HistStat(imgin)
    Layout(imgin, imgout)


def onHistStat():
    path = 'Image/LocalHist.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.HistStat(imgin)
    Layout(imgin, imgout)


def onBoxFilter():
    path = 'Image/BoxFilter.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = cv2.blur(imgin, (21, 21))
    Layout(imgin, imgout)


def onLowpassGauss():
    path = 'Image/BoxFilter.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = cv2.GaussianBlur(imgin, (43, 43), 7.0)
    Layout(imgin, imgout)


def onThreshold():
    path = 'Image/Threshold.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Threshold(imgin)
    Layout(imgin, imgout)


def onMedianFilter():
    path = 'Image/MedianFillter.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.MedianFilter(imgin)
    Layout(imgin, imgout)


def onSharpen():
    path = 'Image/Sharpen.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Sharpen(imgin)
    Layout(imgin, imgout)


def onGradient():
    path = 'Image/Gradient.tif'
    imgin = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    global imgout
    imgout = c3.Gradient(imgin)
    Layout(imgin, imgout)
