import numpy as np
import matplotlib.pyplot as plt


plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"





path = "../../data/raw/Fig2/"

datafig1bg = np.loadtxt(path+"Fig2_Bare_Ground.dat")
datafig1be = np.loadtxt(path+"Fig2_Bare_Excited.dat")
datafig1T0p5g = np.loadtxt(path+"Fig2_T=0p5_Ground.dat")
datafig1T0p5e = np.loadtxt(path+"Fig2_T=0p5_Excited.dat")
datafig1T1g = np.loadtxt(path+"Fig2_T=1_Ground.dat")
datafig1T1e = np.loadtxt(path+"Fig2_T=1_Excited.dat")


plt.plot(datafig1bg[::,0],datafig1bg[::,1],color="k")
plt.plot(datafig1be[::,0],datafig1be[::,1],color="k")

plt.plot(datafig1T0p5g[::,0],datafig1T0p5g[::,1],linestyle="-.",color="blue",label=r"$T=0.5$")
plt.plot(datafig1T0p5e[::,0],datafig1T0p5e[::,1],linestyle="-.",color="blue")

plt.plot(datafig1T1g[::,0],datafig1T1g[::,1],linestyle="--",color="red",label=r"$T=1.0$")
plt.plot(datafig1T1e[::,0],datafig1T1e[::,1],linestyle="--",color="red")

plt.xlabel(r"$t/T$ [time]",)
plt.ylabel(r"$E_n$ [eigenenergy]",)
plt.legend(frameon=True)

#plt.show()
plt.savefig(save_dir + "Sec2-A-IV-LZ_Energies.pdf",dpi=300)

