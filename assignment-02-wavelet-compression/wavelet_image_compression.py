# === Wavelet Daubechies 小波係數 ===
def DaubCoef(p):
    ...
    return h, g, ht, gt


# === 一維小波分解 ===
def daub1D(h, g, u):
    ...
    return u


# === 一維小波重建 ===
def daub1R(ht, gt, u):
    ...
    return uu


# === GUI 畫布初始化 ===
win = mathTEACHWINURLabelFrame
for ww in win.winfo_children():
    ww.destroy()

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

mathTEACHSIMULATECanvas = tkinter.Canvas(mathTEACHWINURLabelFrame)
mathTEACHSIMULATECanvas.place(relx=0, rely=0, relwidth=1, relheight=1)

mathTEACHSIMULATECanvasFig = plt.Figure()
mathTEACHSIMULATECanvas2 = FigureCanvasTkAgg(mathTEACHSIMULATECanvasFig, mathTEACHSIMULATECanvas)
mathTEACHSIMULATECanvas2.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

csqWLTFig = mathTEACHSIMULATECanvasFig
csqWLTLF1Canvas = mathTEACHSIMULATECanvas2


# === 載入 LENA 圖片 ===
n = 8
N = 2**n
lena = Image.open("lena.png").convert("L").resize((N, N))
yy = np.array(lena)

ax1 = csqWLTFig.add_subplot(2, 2, 1)
ax1.imshow(yy, cmap='gray')
ax1.axis('off')
ax1.set_title("Original Image")


# === 小波分解 ===
p = 3        # 小波階數
L = 3        # 分解層數
h, g, ht, gt = DaubCoef(p)

Nx, Ny = yy.shape
uu = yy.copy()

for i in range(L):
    iend = int(Nx / 2**i)
    jend = int(Ny / 2**i)

    # 分解（列）
    for j in range(jend):
        uu[:iend, j] = daub1D(h, g, uu[:iend, j])

    # 分解（行）
    for k in range(iend):
        uu[k, :jend] = daub1D(h, g, uu[k, :jend])


# === 壓縮：將高頻係數設為 0 ===
NN = int(N / (2**L))
for i in range(NN, N):
    for j in range(NN, N):
        uu[i][j] = 0

ax2 = csqWLTFig.add_subplot(2, 2, 2)
ax2.imshow(uu, cmap='gray')
ax2.axis('off')
ax2.set_title("Wavelet Decomposition (Compressed)")


# === 小波重建 ===
ru = uu.copy()

for i in range(L):
    jend = int(Ny / 2**(L - i - 1))
    iend = int(Nx / 2**(L - i - 1))

    for k in range(iend):
        ru[k, :jend] = daub1R(ht, gt, ru[k, :jend])

    for j in range(jend):
        ru[:iend, j] = daub1R(ht, gt, ru[:iend, j])

ax3 = csqWLTFig.add_subplot(2, 2, 3)
ax3.imshow(ru, cmap='gray')
ax3.axis('off')
ax3.set_title("Reconstruction")


# === 誤差圖 ===
dq = np.abs(yy - ru)
ax4 = csqWLTFig.add_subplot(2, 2, 4)
ax4.imshow(dq, cmap='gray')
ax4.axis('off')
ax4.set_title("Error Image")


# === 壓縮比 ===
total_coeff = N * N
remain_coeff = np.sum(uu != 0)
compression_ratio = total_coeff / remain_coeff
print("Compression Ratio =", compression_ratio)

csqWLTLF1Canvas.draw()
