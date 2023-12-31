import numpy as np
import cv2

L = 256


def Negative(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            s = L-1-r
            imgout[x, y] = s
    return imgout


def Logarit(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    c = (L-1)/np.log(L)

    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            if r == 0:
                r = 1
            s = c*np.log(1.0 + r)
            imgout[x, y] = s.astype(np.uint8)
    return imgout


def Power(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    gamma = 5.0
    c = np.power(L - 1, 1 - gamma)
    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            s = c*np.power(r, gamma)
            imgout[x, y] = s.astype(np.uint8)
    return imgout


def PiecewiseLinear(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    rmin, rmax, vi_tri_min, vi_tri_max = cv2.minMaxLoc(imgin)
    r1 = rmin
    s1 = 0
    r2 = rmax
    s2 = L-1
    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            # Doan I
            if r < r1:
                s = s1/r1*r
            # Doan II
            elif r < r2:
                s = (s2-s1)/(r2-r1)*(r-r1) + s1
            # Doan III
            else:
                s = (L-1-s2)/(L-1-r2)*(r-r2) + s2
            imgout[x, y] = np.uint8(s)
    return imgout


def Histogram(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, L), np.uint8) + (L-1)
    h = np.zeros(L, np.int32)
    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            h[r] = h[r] + 1
    p = h/(M*N)  # xac suat theo ti le xuat hien diem anh
    scale = 2000
    for r in range(0, L):
        # ---------------------------------------------B,G,R
        cv2.line(imgout, (r, M-1), (r, M-1-int(scale*p[r])), (0, 0, 0))
    return imgout


def HistEqual(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)

    h = np.zeros(L, np.int32)
    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            h[r] = h[r] + 1
    p = h/(M*N)  # xac suat theo ti le xuat hien diem anh

    s = np.zeros(L, np.float64)
    for k in range(0, L):
        for j in range(0, k+1):
            s[k] = s[k] + p[j]

    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            imgout[x, y] = np.uint64((L-1)*s[r])

    return imgout


def HistEqualColor(imgin):
    M, N, C = imgin.shape
    imgout = np.zeros((M, N, C), np.uint8)

    R = imgin[:, :, 2]
    G = imgin[:, :, 1]
    B = imgin[:, :, 0]

    R = cv2.equalizeHist(R)
    G = cv2.equalizeHist(G)
    B = cv2.equalizeHist(B)

    imgout[:, :, 2] = R
    imgout[:, :, 1] = G
    imgout[:, :, 0] = B
    return imgout


def LocalHist(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)

    m = 3
    n = 3
    w = np.zeros((m, n), np.uint8)
    a = m // 2
    b = n // 2
    for x in range(a, M-a):
        for y in range(b, N-b):
            for s in range(-a, a+1):
                for t in range(-b, b+1):
                    w[s+a, t+b] = imgin[x+s, y+t]
            w = cv2.equalizeHist(w)
            imgout[x, y] = w[a, b]
    return imgout


def HistStat(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)

    m = 3
    n = 3
    w = np.zeros((m, n), np.uint8)
    a = m // 2
    b = n // 2

    mG, sigmaG = cv2.meanStdDev(imgin)
    C = 22.8
    k0 = 0
    k1 = 0.1
    k2 = 0
    k3 = 0.1

    for x in range(a, M-a):
        for y in range(b, N-b):
            for s in range(-a, a+1):
                for t in range(-b, b+1):
                    w[s+a, t+b] = imgin[x+s, y+t]
            msxy, sigmasxy = cv2.meanStdDev(w)
            r = imgin[x, y]
            if (k0*mG <= msxy <= k1*mG) and (k2*sigmaG <= sigmasxy <= k3*sigmaG):
                imgout[x, y] = np.uint8(C*r)
            else:
                imgout[x, y] = r
    return imgout


def MyBoxFilter(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    m = 21
    n = 21
    w = np.ones((m, n), np.float64)
    w = w / (m*n)
    a = m//2
    b = n//2
    for x in range(0, M):
        for y in range(0, N):
            r = 0.0
            for s in range(-a, a+1):
                for t in range(-b, b+1):
                    r = r+w[s+a, t+b]*imgin[(x+s) % M, (y+t) % N]
            imgout[x, y] = np.uint8(r)
    return imgout


def BoxFilter(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    m = 21
    n = 21
    w = np.ones((m, n), np.float64)
    w = w / (m*n)
    imgout = cv2.filter2D(imgin, cv2.CV_8UC1, w)
    return imgout


def TinhBoLoGauss(m, n, sigma):
    w = np.zeros((m, n), np.float64)
    sigma = 1.0
    a = m//2
    b = n//2
    for s in range(-a, a+1):
        for t in range(-b, b+1):
            w[s+a, t+b] = np.exp(-(s**2+t**2)/(2*sigma**2))
    k = np.sum(w)
    w = w/k
    return w


def GaussFilter(imgin):
    m = 43
    n = 43
    sigma = 7.0
    w = TinhBoLoGauss(m, n, sigma)
    imgout = cv2.filter2D(imgin, cv2.CV_8UC1, w)
    return imgout


def MyThreshold(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)

    temp = cv2.blur(imgin, (15, 15))
    for x in range(0, M):
        for y in range(0, N):
            r = temp[x, y]
            if r <= 65:
                r = 0
            else:
                r = L-1
            imgout[x, y] = r
    return imgout


def Threshold(imgin):
    temp = cv2.blur(imgin, (15, 15))
    retval, imgout = cv2.threshold(temp, 64, L-1, cv2.THRESH_BINARY)
    return imgout


def MedianFilter(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    m = 5
    n = 5
    w = np.zeros((m, n), np.uint8)
    a = m // 2
    b = n // 2
    for x in range(0, M):
        for y in range(0, N):
            for s in range(-a, a+1):
                for t in range(-b, b+1):
                    w[s+a, t+b] = imgin[(x+s) % M, (y+t) % N]
            w_1D = np.reshape(w, (m*n,))
            w_1D = np.sort(w_1D)
            imgout[x, y] = w_1D[m*n//2]
    return imgout


def Sharpen(imgin):
    # Đạo hàm cấp 2 của ảnh
    w = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    temp = cv2.filter2D(imgin, cv2.CV_32FC1, w)

    # Hàm cv2.Laplacian chỉ tính đạo hàm cấp 2
    # cho bộ lọc có số -4 chính giữa
    imgout = imgin - temp
    imgout = np.clip(imgout, 0, L-1)
    imgout = imgout.astype(np.uint8)
    return imgout


def Gradient(imgin):
    sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobel_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    # Đạo hàm cấp 1 theo hướng x
    mygx = cv2.filter2D(imgin, cv2.CV_32FC1, sobel_x)
    # Đạo hàm cấp 1 theo hướng y
    mygy = cv2.filter2D(imgin, cv2.CV_32FC1, sobel_y)

    # Lưu ý: cv2.Sobel có hướng x nằm ngang
    # ngược lại với sách Digital Image Processing
    gx = cv2.Sobel(imgin, cv2.CV_32FC1, dx=1, dy=0)
    gy = cv2.Sobel(imgin, cv2.CV_32FC1, dx=0, dy=1)

    imgout = abs(gx) + abs(gy)
    imgout = np.clip(imgout, 0, L-1)
    imgout = imgout.astype(np.uint8)
    return imgout
