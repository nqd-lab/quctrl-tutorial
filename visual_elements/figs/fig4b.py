import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"



path = "../../data/raw/Fig4b/"


datafig4b = np.loadtxt(path+"Fig4b_LMG_ContourPlot.dat")


np.shape(datafig4b)
a = np.reshape(datafig4b,(46,47,3))
points = np.zeros((46,47))

for i in range(0,46):
    for j in range(0,47):
        for k in range(0,3):
            points[i][j] = a[i][j][k]


x = np.linspace(1,10,46)
y = np.linspace(-1,1.3,47)

X,Y = np.meshgrid(y,x)
plt.contourf(Y,X,points,[0, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 0.995, 0.9995], cmap=cm.magma)

plt.xlabel(r"$a$ [parameter]",)
plt.ylabel(r"$b$ [parameter]",)
plt.colorbar()

plt.text(-0.7,1.3, '(b)', ha='left', va='top', fontsize=18, )

#plt.show()
plt.savefig(save_dir + "LMG_plot2.pdf",dpi=300)


