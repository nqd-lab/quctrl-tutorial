import numpy as np
import matplotlib.pyplot as plt


plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"



path = "../../data/processed/Fig4a/"


datafig4a1 = np.loadtxt(path+"Fig4_LMG_FullSTA_Black.dat")
datafig4a2 = np.loadtxt(path+"Fig4_LMG_HarmonicApprox_Blue.dat")
datafig4a3 = np.loadtxt(path+"Fig4_LMG_STA_Red.dat")


plt.plot(datafig4a1[::,0],datafig4a1[::,1],marker="o",color="black",label=r"$H_\mathrm{CD}$")
plt.plot(datafig4a2[::,0],datafig4a2[::,1],marker="o",color="blue",label=r"$H$")
plt.plot(datafig4a3[::,0],datafig4a3[::,1],marker="o",color="red",label=r"$H+A_\mathrm{GS}$")

plt.xlabel(r"$N$ [system size]")
plt.ylabel(r"$\mathcal{F}$ [fidelity]")
plt.legend(frameon=True,)

plt.text(-95,1.0025, '(a)', ha='left', va='top', fontsize=18, )


#plt.show()
plt.savefig(save_dir + "LMG_plot1.pdf",dpi=300)


