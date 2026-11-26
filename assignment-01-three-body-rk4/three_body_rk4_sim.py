win=mathTEACHWINURLabelFrame
for ww in win.winfo_children():
    ww.destroy()
global E1Var, E2Var
global EP1Var, EP2Var
global EV1Var, EV2Var
global ET1Var, ET2Var
global mathTEACHSIMULATECanvas2
global mathTEACHSIMULATECanvasFig

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import tkinter
mathTEACHSIMULATECanvas=tkinter.Canvas(mathTEACHWINURLabelFrame)
mathTEACHSIMULATECanvas.place(relx=0,rely=0.3,relwidth=0.8,relheight=0.7)
mathTEACHSIMULATECanvasFig=plt.Figure()
mathTEACHSIMULATECanvas2=FigureCanvasTkAgg(mathTEACHSIMULATECanvasFig,mathTEACHSIMULATECanvas)
mathTEACHSIMULATECanvas2.get_tk_widget().place(relx=0,rely=0,relwidth=1,relheight=1)
print("TaylorSeries.py")
import numpy as np

mathTEACHSIMULATECanvasFig.clf()
ax=mathTEACHSIMULATECanvasFig.add_subplot(111,projection = '3d')
#ax=mathTEACHSIMULATECanvasFig.add_subplot(111)
import tkinter

# === m1, m2, m3 ===
L1=tkinter.Label(win)
L1.place(relx=0,rely=0,relwidth=0.25,relheight=0.06)
L1.configure(text='m1')
E1Var=tkinter.StringVar()
E1=tkinter.Entry(win,textvariable=E1Var)
E1.place(relx=0.25,rely=0,relwidth=0.25,relheight=0.06)
E1Var.set('1.0')
###
L2=tkinter.Label(win)
L2.place(relx=0.5,rely=0,relwidth=0.25,relheight=0.06)
L2.configure(text='m2')
E2Var=tkinter.StringVar()
E2=tkinter.Entry(win,textvariable=E2Var)
E2.place(relx=0.75,rely=0,relwidth=0.25,relheight=0.06)
E2Var.set('1.0')
###
L3=tkinter.Label(win)
L3.place(relx=0,rely=0.06,relwidth=0.25,relheight=0.06)
L3.configure(text='m3')
E3Var=tkinter.StringVar()
E3=tkinter.Entry(win,textvariable=E3Var)
E3.place(relx=0.25,rely=0.06,relwidth=0.25,relheight=0.06)
E3Var.set('1.0')

# ==== P1, P2, P3 ====
LP1=tkinter.Label(win)
LP1.place(relx=0.5,rely=0.06,relwidth=0.25,relheight=0.06)
LP1.configure(text='P1')
EP1Var=tkinter.StringVar()
EP1=tkinter.Entry(win,textvariable=EP1Var)
EP1.place(relx=0.75,rely=0.06,relwidth=0.25,relheight=0.06)
EP1Var.set('(1,0,0)')
EP1.configure(font=("Arial",12,'bold'))
###
LP2=tkinter.Label(win)
LP2.place(relx=0,rely=0.12,relwidth=0.25,relheight=0.06)
LP2.configure(text='P2')
EP2Var=tkinter.StringVar()
EP2=tkinter.Entry(win,textvariable=EP2Var)
EP2.place(relx=0.25,rely=0.12,relwidth=0.25,relheight=0.06)
EP2Var.set('(-1,0,0)')
EP2.configure(font=("Arial",12,'bold'))
###
LP3=tkinter.Label(win)
LP3.place(relx=0.5,rely=0.12,relwidth=0.25,relheight=0.06)
LP3.configure(text='P3')
EP3Var=tkinter.StringVar()
EP3=tkinter.Entry(win,textvariable=EP3Var)
EP3.place(relx=0.75,rely=0.12,relwidth=0.25,relheight=0.06)
EP3Var.set('(0,0,1)')
EP3.configure(font=("Arial",12,'bold'))

# ==== V1, V2, V3 ====
LV1=tkinter.Label(win)
LV1.place(relx=0,rely=0.18,relwidth=0.25,relheight=0.06)
LV1.configure(text='V1')
EV1Var=tkinter.StringVar()
EV1=tkinter.Entry(win,textvariable=EV1Var)
EV1.place(relx=0.25,rely=0.18,relwidth=0.25,relheight=0.06)
EV1Var.set('(0,0.5,0)')
EV1.configure(font=("Arial",12,'bold'))
###
LV2=tkinter.Label(win)
LV2.place(relx=0.5,rely=0.18,relwidth=0.25,relheight=0.06)
LV2.configure(text='V2')
EV2Var=tkinter.StringVar()
EV2=tkinter.Entry(win,textvariable=EV2Var)
EV2.place(relx=0.75,rely=0.18,relwidth=0.25,relheight=0.06)
EV2Var.set('(0,-0.5,0)')
EV2.configure(font=("Arial",12,'bold'))
###
LV3=tkinter.Label(win)
LV3.place(relx=0,rely=0.24,relwidth=0.25,relheight=0.06)
LV3.configure(text='V3')
EV3Var=tkinter.StringVar()
EV3=tkinter.Entry(win,textvariable=EV3Var)
EV3.place(relx=0.25,rely=0.24,relwidth=0.25,relheight=0.06)
EV3Var.set('(0.5,-0.5,0)')
EV3.configure(font=("Arial",12,'bold'))

# ==== t0, t1 ====
LT1=tkinter.Label(win)
LT1.place(relx=0.5,rely=0.24,relwidth=0.25,relheight=0.06)
LT1.configure(text='t0')
ET1Var=tkinter.StringVar()
ET1=tkinter.Entry(win,textvariable=ET1Var)
ET1.place(relx=0.75,rely=0.24,relwidth=0.25,relheight=0.06)
ET1Var.set('0')
LT2=tkinter.Label(win)
LT2.place(relx=0,rely=0.30,relwidth=0.25,relheight=0.06)
LT2.configure(text='t1')
ET2Var=tkinter.StringVar()
ET2=tkinter.Entry(win,textvariable=ET2Var)
ET2.place(relx=0.25,rely=0.30,relwidth=0.25,relheight=0.06)
ET2Var.set('1')

def cmdRUN():
    pass

EB=tkinter.Button(win)
EB.place(relx=0.75,rely=0.30,relwidth=0.25,relheight=0.1)
EB.configure(text='RUN')
EB.configure(command=cmdRUN)
##
EBR=tkinter.Button(win)
EBR.place(relx=0.75,rely=0.38,relwidth=0.25,relheight=0.1)
EBR.configure(text='ReSet')
##

#ax.scatter3D(1, 1, 1, s=int(50*int(E1Var.get())), c='blue') 
# s=50 sets the marker size
#ax.scatter3D(-1, -1, -1, s=int(50*int(E2Var.get())), c='red') 
# s=50 sets the marker size


###
global cmdRUN2
def cmdRUN2():
    import matplotlib.animation as animation
    import numpy as np
    import ast
    global mathTEACHSIMULATECanvas2, mathTEACHSIMULATECanvasFig
    global E1Var, E2Var, E3Var
    global EP1Var, EP2Var, EP3Var
    global EV1Var, EV2Var, EV3Var
    global ET1Var, ET2Var

    mathTEACHSIMULATECanvasFig.clf()
    ax=mathTEACHSIMULATECanvasFig.add_subplot(111,projection = '3d')
    print('3-body Simulation with Runge-Kutta Method')

    # === 讀取輸入 ===
    masses = []
    positions = []
    velocities = []
    for i, (mVar, pVar, vVar) in enumerate([
        (E1Var, EP1Var, EV1Var),
        (E2Var, EP2Var, EV2Var),
        (E3Var, EP3Var, EV3Var)
    ]):
        m = float(mVar.get())
        p = np.array(ast.literal_eval(pVar.get()), dtype=float)
        v = np.array(ast.literal_eval(vVar.get()), dtype=float)
        masses.append(m)
        positions.append(p)
        velocities.append(v)

    masses = np.array(masses)
    positions = np.array(positions)
    velocities = np.array(velocities)

    # === 時間參數 ===
    t0 = float(ET1Var.get())
    tf = float(ET2Var.get())
    dt = 0.01
    num_steps = int((tf - t0) / dt)

    # === 儲存軌跡 ===
    traj = [positions.copy()]

    # === 定義加速度（萬有引力） ===
    def acceleration(pos, m):
        N = len(m)
        a = np.zeros_like(pos)
        for i in range(N):
            for j in range(N):
                if i != j:
                    r_vec = pos[j] - pos[i]
                    r = np.linalg.norm(r_vec)
                    if r != 0:
                        a[i] += m[j] * r_vec / r**3
        return a

    # === Runge-Kutta 4th order ===
    for _ in range(num_steps):
        a1 = acceleration(positions, masses)
        k1v = a1 * dt
        k1x = velocities * dt

        a2 = acceleration(positions + 0.5 * k1x, masses)
        k2v = a2 * dt
        k2x = (velocities + 0.5 * k1v) * dt

        a3 = acceleration(positions + 0.5 * k2x, masses)
        k3v = a3 * dt
        k3x = (velocities + 0.5 * k2v) * dt

        a4 = acceleration(positions + k3x, masses)
        k4v = a4 * dt
        k4x = (velocities + k3v) * dt

        positions += (k1x + 2*k2x + 2*k3x + k4x) / 6
        velocities += (k1v + 2*k2v + 2*k3v + k4v) / 6

        traj.append(positions.copy())

    traj = np.array(traj)  # (time, N, 3)

    # === 畫圖 ===
    colors = ['red', 'blue', 'green']
    for i in range(3):
        ax.plot(traj[:, i, 0], traj[:, i, 1], traj[:, i, 2], color=colors[i], label=f'Body {i+1}')
        ax.scatter(traj[-1, i, 0], traj[-1, i, 1], traj[-1, i, 2],
                   color=colors[i], s=50*(masses[i]+1))

    ax.set_xlabel('X-axis',fontsize=6)
    ax.set_ylabel('Y-axis',fontsize=6)
    ax.set_zlabel('Z-axis',fontsize=6)
    ax.set_title('3D Three-body Simulation (Runge-Kutta 4th)',fontsize=6)
    ax.legend()
    mathTEACHSIMULATECanvas2.draw()

    # === 動畫 ===
    def animate(i):
        ax.cla()
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_zlim(-3, 3)
        for j in range(3):
            ax.plot(traj[:i, j, 0], traj[:i, j, 1], traj[:i, j, 2], color=colors[j])
            ax.scatter(traj[i, j, 0], traj[i, j, 1], traj[i, j, 2],
                       color=colors[j], s=40*(masses[j]+1))
        return []

    animation.FuncAnimation(mathTEACHSIMULATECanvasFig, animate,
                            frames=len(traj), interval=10, blit=False)
    mathTEACHSIMULATECanvas2.draw()

EB.configure(command=cmdRUN2)
def cmdRESET():
    # 清除畫布上的所有內容
    mathTEACHSIMULATECanvasFig.clf()
    ax = mathTEACHSIMULATECanvasFig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    mathTEACHSIMULATECanvas2.draw()

    # 重設所有輸入欄位回預設值
    E1Var.set('1.0')
    E2Var.set('1.0')
    E3Var.set('1.0')

    EP1Var.set('(1,0,0)')
    EP2Var.set('(-1,0,0)')
    EP3Var.set('(0,0,1)')

    EV1Var.set('(0,0.5,0)')
    EV2Var.set('(0,-0.5,0)')
    EV3Var.set('(0.5,-0.5,0)')

    ET1Var.set('0')
    ET2Var.set('1')

EBR.configure(command=cmdRESET)

mathTEACHSIMULATECanvas2.draw()
