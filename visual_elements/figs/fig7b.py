# QOC_FIGURE1-B.PY (STATE CONTROL)
# author: pmpoggi @ strath (november 2024)
# ------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

path = "../../data/raw/Fig7b/"

# General definitions
Delta = 1 # LZ gap
M = 10 # number of timesteps
T0 = np.pi/(Delta)
red_new = "#A52639"
blue_new = "#336EFF"

# FIGURE 1 - B
# ------------

nu0s = [0.5,0.75,1,1.5,2,3,5,7,10] # every value of nu0 considered
nu0s_plot = [0.5,1,2,5,10] # values to show in top plot
cmap = mpl.colormaps['copper']
colors = cmap(np.linspace(0, 1, len(nu0s_plot)))
symbols = ['o','^','*','v','s']

Ts = np.loadtxt(path+"LZ_Tfs.txt")*T0 # vector of evolution times T

fig,ax = plt.subplots(2,1,figsize=(4.5,5),height_ratios=[1.5,1])

# ax[0]: Infidelities vs evolution time for different nu0s

for kn in range(len(nu0s_plot)):
    nu0 = nu0s_plot[kn]
    final_cost = np.loadtxt(path+"LZ_state_final_cost_nu%.2f.txt"%nu0)    
    ax[0].semilogy(Ts/T0,final_cost,'-',color=colors[kn],marker=symbols[kn],markersize=5,label=r"$\nu_0=$%.1f"%nu0)

ax[0].legend(loc='upper right',frameon=False)
ax[0].set_xlabel(r"$T/T_0$ [control time]",size=12)
ax[0].set_ylabel(r"$J(\alpha_\mathrm{opt})$ [optimized cost]",size=12)
ax[0].set_xticks([0,0.5,1,1.5,2])
ax[0].set_ylim( [1e-16,2])
ax[0].text(0.03, 0.01, '(e)', ha='left', va='top',fontsize=12)

plt.tight_layout()

# ax[1]: Tmin (\sim QSL time) as a function of nu0

Tmin = np.loadtxt(path+"LZ_state_Tmin.txt") # numerical Tmin
Tmin_analytic = np.loadtxt(path+"LZ_Tmin_analytic.txt")


dT = (Ts[1]-Ts[0])/2
err_bars = np.ones(len(nu0s))*(Ts[1]-Ts[0])/(2*T0) # error bars
ax[1].errorbar(nu0s,Tmin/T0,yerr=err_bars,ls='',marker='o',color=red_new,label=r"$T_*$ numerical")
ax[1].plot(nu0s,Tmin_analytic/T0,'--',color=red_new,label=r"$\tau_{\mathrm{QSL}}^\ast$ analytic")
ax[1].set_xlabel(r"$\nu_0$ [parameter]",size=12)
ax[1].set_ylabel("$T/T_0$ [control time]",size=12)
ax[1].legend(loc='lower right',frameon=False)
ax[1].set_yticks([0.2,0.3,0.4,0.5])
plt.text(0.25,0.52, '(f)', ha='left', va='top',fontsize=12)
plt.tight_layout()

#plt.show()
plt.savefig(save_dir + "QOC-Fig1-B.pdf",dpi=300)
# 
