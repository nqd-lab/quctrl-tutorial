# QOC_FIGURE2-B.PY (UNITARY CONTROL)
# author: pmpoggi @ strath (november 2024)
# ------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

path = "../../data/processed/Fig8b/"

# General definitions
Omega = 1 # rabi frequency
M = 10 # number of timesteps
Tu = 2*np.pi/(Omega)
red_new = "#A52639"
blue_new = "#336EFF"

# FIGURE 1 - B
# ------------

phis = np.array([1/32,1/16,1/8,1/4,0.5,2/3,1])*np.pi
phis_plot = np.array([1/4,1/2,2/3,1])*np.pi
cmap = mpl.colormaps['copper']
colors = cmap(np.linspace(0, 1, len(phis_plot)))
symbols = ['o','^','*','v','s']

Ts_x = np.loadtxt(path+"unit_Tfs_x.txt")*Tu # vector of evolution times T (targets in x)
Ts_z = np.loadtxt(path+"unit_Tfs_z.txt")*Tu # vector of evolution times T (targets i z)

fig,ax = plt.subplots(2,1,figsize=(4.5,5),height_ratios=[1.5,1])

# ax[0]: Infidelities vs evolution time for different phis - Target Uz

axis_target = "z"

for kp in range(len(phis_plot)):
    phi = phis_plot[kp]
    final_cost = np.loadtxt(path+"/unit_final_cost_"+axis_target+"_phi%.2f.txt"%(phi/np.pi))    
    ax[0].semilogy(Ts_z/Tu,final_cost,'-',color=colors[kp],marker=symbols[kp],markersize=5,label=r"$\phi=%.2f\pi$"%(phi/np.pi))

ax[0].legend(loc='upper right',frameon=False)
ax[0].set_xlabel(r"$T/T_U$ [control time]",size=12)
ax[0].set_ylabel(r"$J(\alpha_\mathrm{opt})$ [optimized cost]",size=12)
ax[0].set_xticks([0,0.5,1,1.5])
ax[0].set_ylim( [1e-16,2])
ax[0].text(0.03, 0.01, '(e)', ha='left', va='top',fontsize=12)

plt.tight_layout()

# ax[1]: Tmin (\sim QSL time) as a function of phi

colore_ax = {'x':'k','z':'r'}

Tmin_x = np.loadtxt(path+"unit_Tmin_x.txt") # numerical Tmin
Tmin_z = np.loadtxt(path+"unit_Tmin_z.txt") # numerical Tmin
Tmin_analytic_x = np.loadtxt(path+"Tmin_analytic_x.txt")
Tmin_analytic_z = np.loadtxt(path+"Tmin_analytic_z.txt")
phis_cont = np.loadtxt(path+"Tmin_phis_vec.txt") # a denser vector of phis 

[err_bars_x,err_bars_z] = [np.ones(len(phis))*(Ts_x[1]-Ts_x[0])/2, np.ones(len(phis))*(Ts_z[1]-Ts_z[0])/2] # error bars

phis=phis/np.pi
phis_cont/=np.pi

ax[1].plot(phis,Tmin_x/Tu,ls='',marker='o',color='0.5',label=r"$T_\ast$ numerical")
ax[1].errorbar(phis,Tmin_x/Tu,yerr=err_bars_x,ls='',marker='o',color='k')
ax[1].plot(phis_cont,Tmin_analytic_x,'--',color='k',label=r"$\tau_{\mathrm{QSL}}^\ast$ analytic")
ax[1].errorbar(phis,Tmin_z/Tu,yerr=err_bars_z,ls='',marker='o',color=red_new)
ax[1].plot(phis_cont,Tmin_analytic_z,'--',color=red_new)
ax[1].set_xlabel(r"$\phi/\pi$ [parameter]",size=12)
ax[1].set_ylabel("$T/T_U$ [control time]",size=12)
ax[1].legend(loc=(0.075,0.65),frameon=False)
ax[1].set_ylim([-0.05,1.05])
ax[1].text(0.01,1, '(f)', ha='left', va='top',fontsize=12)
ax[1].text(2.6/np.pi,0.33,r'$U_x(\phi)$',ha='left', va='top',fontsize=13,color='k')
ax[1].text(2.6/np.pi,0.75,r'$U_z(\phi)$',ha='left', va='top',fontsize=13,color=red_new)
# This bit makes the legend gray so that it applies to both X and Z cases (no need to duplicate the legend)
leg = ax[1].get_legend()
leg.legend_handles[1].set_color('0.5')
# leg.legend_handles[1].set_array('0.5')


# ax[1].set_yticks([0.2,0.3,0.4,0.5])

plt.tight_layout()

#plt.show()
plt.savefig(save_dir + "QOC-Fig2-B.pdf",dpi=300,bbox_inches='tight')

