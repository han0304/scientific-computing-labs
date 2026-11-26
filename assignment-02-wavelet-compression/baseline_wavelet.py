import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


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


win = mathTEACHWINURLabelFrame
for ww in win.winfo_children():
    ww.destroy()

mathTEACHSIMULATECanvas = tkinter.Canvas(mathTEACHWINURLabelFrame)
mathTEACHSIMULATECanvas.place(relx=0, rely=0, relwidth=1, relheight=1)

mathTEACHSIMULATECanvasFig = plt.Figure()
mathTEACHSIMULATECanvas2 = FigureCanvasTkAgg(mathTEACHSIMULATECanvasFig, mathTEACHSIMULATECanvas)
mathTEACHSIMULATECanvas2.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

csqWLTFig = mathTEACHSIMULATECanvasFig
csqWLTLF1Canvas = mathTEACHSIMULATECanvas2

# === 使用 sin(2*pi*(x+y)) 產生人工影像 ===
csqWLTFig.clf()
n = 8
N = 2**n
dx = 1 / N
supp = 1
x = np.arange(0, supp, dx)
y = np.sin(2.0 * np.pi * x)

yy = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        yy[i, j] = np.sin(2.0 * np.pi * (x[i] + x[j]))

ax1 = csqWLTFig.add_subplot(131)
ax1.imshow(yy, cmap='gray')
ax1.axis('off')

# === 小波分解（p=2, L=3，無高頻歸零壓縮與壓縮比計算） ===
p = 2
L = 3
h, g, ht, gt = DaubCoef(p)
Nx, Ny = np.array(yy).shape
uu = yy.copy()

for i in range(L):
    iend = int(Nx / 2**i)
    for j in range(int(Ny / 2**i)):
        uu[:iend, j] = daub1D(h, g, uu[:iend, j])
    jend = int(Ny / 2**i)
    for k in range(int(Nx / 2**i)):
        uu[k, :jend] = daub1D(h, g, uu[k, :jend])

ax2 = csqWLTFig.add_subplot(132)
ax2.imshow(uu, cmap='gray')
ax2.axis('off')
ax2.title.set_text('Decomposition')
csqWLTLF1Canvas.draw()

# === 小波重建（無誤差圖） ===
ru = uu.copy()

for i in range(L):
    jend = int(Ny / 2**(L - i - 1))
    for k in range(int(Nx / 2**(L - i - 1))):
        ru[k, :jend] = daub1R(h, g, ru[k, :jend])
    iend = int(Nx / 2**(L - i - 1))
    for j in range(int(Ny / 2**(L - i - 1))):
        ru[:iend, j] = daub1R(h, g, ru[:iend, j])

ax3 = csqWLTFig.add_subplot(133)
ax3.imshow(ru, cmap='gray')
ax3.axis('off')
ax3.title.set_text('Reconstruction')
csqWLTLF1Canvas.draw()