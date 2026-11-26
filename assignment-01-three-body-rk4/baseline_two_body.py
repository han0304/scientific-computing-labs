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
mathTEACHSIMULATECanvas.place(relx=0,rely=0.24,relwidth=0.8,relheight=0.7)
mathTEACHSIMULATECanvasFig=plt.Figure()
mathTEACHSIMULATECanvas2=FigureCanvasTkAgg(mathTEACHSIMULATECanvasFig,mathTEACHSIMULATECanvas)
mathTEACHSIMULATECanvas2.get_tk_widget().place(relx=0,rely=0,relwidth=1,relheight=1)
print("TaylorSeries.py")
import numpy as np

mathTEACHSIMULATECanvasFig.clf()
ax=mathTEACHSIMULATECanvasFig.add_subplot(111,projection = '3d')
#ax=mathTEACHSIMULATECanvasFig.add_subplot(111)
import tkinter

L1=tkinter.Label(win)
L1.place(relx=0,rely=0,relwidth=0.25,relheight=0.06)
L1.configure(text='m1')
E1Var=tkinter.StringVar()
E1=tkinter.Entry(win,textvariable=E1Var)
E1.place(relx=0.25,rely=0,relwidth=0.25,relheight=0.06)
E1Var.set('1')
L2=tkinter.Label(win)
L2.place(relx=0.5,rely=0,relwidth=0.25,relheight=0.06)
L2.configure(text='m2')
E2Var=tkinter.StringVar()
E2=tkinter.Entry(win,textvariable=E2Var)
E2.place(relx=0.75,rely=0,relwidth=0.25,relheight=0.06)
E2Var.set('2')
###
####
LP1=tkinter.Label(win)
LP1.place(relx=0,rely=0.06,relwidth=0.25,relheight=0.06)
LP1.configure(text='P1')
EP1Var=tkinter.StringVar()
EP1=tkinter.Entry(win,textvariable=EP1Var)
EP1.place(relx=0.25,rely=0.06,relwidth=0.25,relheight=0.06)
EP1Var.set('(-1,-1,-1)')
EP1.configure(font=("Arial",12,'bold'))
###
LP2=tkinter.Label(win)
LP2.place(relx=0.5,rely=0.06,relwidth=0.25,relheight=0.06)
LP2.configure(text='P2')
EP2Var=tkinter.StringVar()
EP2=tkinter.Entry(win,textvariable=EP2Var)
EP2.place(relx=0.75,rely=0.06,relwidth=0.25,relheight=0.06)
EP2Var.set('(1,1,1)')
EP2.configure(font=("Arial",12,'bold'))
###
####
LV1=tkinter.Label(win)
LV1.place(relx=0,rely=0.12,relwidth=0.25,relheight=0.06)
LV1.configure(text='V1')
EV1Var=tkinter.StringVar()
EV1=tkinter.Entry(win,textvariable=EV1Var)
EV1.place(relx=0.25,rely=0.12,relwidth=0.25,relheight=0.06)
EV1Var.set('(0,-1,0)')
EV1.configure(font=("Arial",12,'bold'))
###
LV2=tkinter.Label(win)
LV2.place(relx=0.5,rely=0.12,relwidth=0.25,relheight=0.06)
LV2.configure(text='V2')
EV2Var=tkinter.StringVar()
EV2=tkinter.Entry(win,textvariable=EV2Var)
EV2.place(relx=0.75,rely=0.12,relwidth=0.25,relheight=0.06)
EV2Var.set('(0,1,0)')
EV2.configure(font=("Arial",12,'bold'))

###
LT1=tkinter.Label(win)
LT1.place(relx=0,rely=0.18,relwidth=0.25,relheight=0.06)
LT1.configure(text='t0')
ET1Var=tkinter.StringVar()
ET1=tkinter.Entry(win,textvariable=ET1Var)
ET1.place(relx=0.25,rely=0.18,relwidth=0.25,relheight=0.06)
ET1Var.set('0')
LT2=tkinter.Label(win)
LT2.place(relx=0.5,rely=0.18,relwidth=0.25,relheight=0.06)
LT2.configure(text='t1')
ET2Var=tkinter.StringVar()
ET2=tkinter.Entry(win,textvariable=ET2Var)
ET2.place(relx=0.75,rely=0.18,relwidth=0.25,relheight=0.06)
ET2Var.set('1')

def cmdRUN():
    pass

EB=tkinter.Button(win)
EB.place(relx=0.75,rely=0.25,relwidth=0.25,relheight=0.1)
EB.configure(text='RUN')
EB.configure(command=cmdRUN)
##
EBR=tkinter.Button(win)
EBR.place(relx=0.75,rely=0.35,relwidth=0.25,relheight=0.1)
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
    global mathTEACHSIMULATECanvas2
    global mathTEACHSIMULATECanvasFig
    mathTEACHSIMULATECanvasFig.clf()
    ax=mathTEACHSIMULATECanvasFig.add_subplot(111,projection = '3d')
    print('HIII')
    cmds='(x1,y1,z1)='+EP1Var.get()
    exec(cmds,globals())
    cmds='(vx,vy,vz)='+EV1Var.get()
    exec(cmds,globals())
    vx1 = vx
    vy1 = vy
    vz1 = vz
    #ax.scatter3D(x1, y1, z1, s=int(50*int(E1Var.get())), c='blue') 
    # s=50 sets the marker size
    cmds='(x2,y2,z2)='+EP2Var.get()
    exec(cmds,globals())
    cmds='(vx,vy,vz)='+EV2Var.get()
    exec(cmds,globals())
    vx2=vx
    vy2=vy
    vz2=vz
    #ax.scatter3D(x2, y2, z2, s=int(50*int(E2Var.get())), c='red') 
    # s=50 sets the marker size    
    cmds='m='+E1Var.get()
    exec(cmds,globals())
    m1=m
    cmds='m='+E2Var.get()
    exec(cmds,globals())
    m2=m  
    print(m1,m2)
    # Initial position and velocity of the particle
    x,y,z=x1,y1,z1
    xx,yy,zz=x2,y2,z2
    # Lists to store the particle's trajectory
    trajectory_x1 = [x]
    trajectory_y1 = [y]
    trajectory_z1 = [z]
    trajectory_x2 = [xx]
    trajectory_y2 = [yy]
    trajectory_z2 = [zz]

    # Simulate movement over time
    num_steps = 1000
    dt = 0.01  # Time step
    cmds='t='+ET2Var.get()
    exec(cmds,globals())
    tfinal=t
    num_steps=int(tfinal/dt)
    import numpy as np
    for _ in range(num_steps):
       # Update position based on velocity
       r=np.sqrt((x-xx)**2+(y-yy)**2+(z-zz)**2)
       vx1+= m2*(xx-x)*dt / r
       vy1+= m2*(yy-y)*dt / r
       vz1+= m2*(zz-z)*dt / r

       vx2-= m1*(xx-x)*dt / r
       vy2-= m1*(yy-y)*dt / r
       vz2-= m1*(zz-z)*dt / r

       x += vx1 * dt
       y += vy1 * dt
       z += vz1 * dt
       xx+= vx2 * dt
       yy+= vy2 * dt
       zz+= vz2 * dt

       # Store current position
       trajectory_x1.append(x)
       trajectory_y1.append(y)
       trajectory_z1.append(z)

       trajectory_x2.append(xx)
       trajectory_y2.append(yy)
       trajectory_z2.append(zz)

    # Plot the trajectory
    ax.plot(trajectory_x1, trajectory_y1, trajectory_z1, label='Particle Trajectory')
    ax.plot(trajectory_x2, trajectory_y2, trajectory_z2, label='Particle Trajectory')

    # Plot the current position of the particle (optional, as the line shows it)
    ax.scatter(x, y, z, color='red', marker='o', s=50*int(m1+1), label='Current Position')
    ax.scatter(xx, yy, zz, color='blue', marker='o', s=50*int(m2+1), label='Current Position')

    ax.set_xlabel('X-axis',fontsize=6)
    ax.set_ylabel('Y-axis',fontsize=6)
    ax.set_zlabel('Z-axis',fontsize=6)
    ax.set_title('3D Scatter Plot with Fixed Dot Size',fontsize=6)
    mathTEACHSIMULATECanvas2.draw()


    def animate(i):
        #ax.set_xlim3d([-border, border])
        #ax.set_ylim3d([-border, border])
        #ax.set_zlim3d([-border, border])
        ax.scatter(trajectory_x1[i],trajectory_y1[i],trajectory_z1[i])
        ax.scatter(trajectory_x2[i],trajectory_y2[i],trajectory_z2[i])        
    timesteps=num_steps
    anim = animation.FuncAnimation(mathTEACHSIMULATECanvasFig, animate, frames=timesteps, interval=1, blit=False, repeat=False)
    mathTEACHSIMULATECanvas2.draw()
    

EB.configure(command=cmdRUN2)

mathTEACHSIMULATECanvas2.draw()
