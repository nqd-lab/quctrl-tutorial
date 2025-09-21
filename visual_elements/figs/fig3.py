import numpy as np
import matplotlib.pyplot as plt


plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"



path = "../../data/processed/Fig3/"

datafig2a = np.loadtxt(path+"Fig3_A1_SingleBody_Red.dat")
datafig2b = np.loadtxt(path+"Fig3_A2_TwoBody_Orange.dat")
datafig2c = np.loadtxt(path+"Fig3_FullSTA_Black.dat")
datafig2d = np.loadtxt(path+"Fig3_NoControlTerm_Blue.dat")


plt.plot(datafig2d[::,0],datafig2d[::,1],color="blue", label="no control term")
plt.plot(datafig2a[::,0],datafig2a[::,1],linestyle="--",color="red",label=r"${A}^{[1]}_\mathrm{GS}$")
plt.plot(datafig2b[::,0],datafig2b[::,1],linestyle="-.",color="orange",label=r"${A}^{[2]}_\mathrm{GS}$")
plt.plot(datafig2c[::,0],datafig2c[::,1],color="black",label=r"$\mathcal{A}$")


plt.xlabel(r"$t/T$ [time]")
plt.ylabel(r"$\mathcal{F}$ [fidelity]")
plt.legend(frameon=True)


#plt.show()
plt.savefig(save_dir + "Sec2-A-V-IsingFigure.pdf",dpi=300)
