# QOC_FIGURE3.PY (MANY-BODY CONTROL)
# author: pmpoggi @ strath (april 2025)
# ------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#plt.style.use("../ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

path = "../../data/raw/Fig9/"

# General definitions
red_new = "#A52639"
blue_new = "#336EFF"

# FIGURE 3
# --------

cmap = mpl.colormaps['copper']
colors = cmap(np.linspace(0, 1, 5))[::-1]
symbols = ['o','^','*','v','s'][::-1]

N_vec = [6,8,10] # values of N considered (system size)

plt.figure(1,figsize=(10,3))

for kn in range(len(N_vec)):
    N = N_vec[kn]
    k_vec = np.arange(1,int(N/2) + 1) # number of excitations considered
    
    Ts = np.loadtxt(path+"N%d_timeT.txt"%N) # vector of evolution times T
    
    plt.subplot(1,3,kn+1) # one plot for each N value
    plt.title("$N=%d$"%N,size=13)
    for kv in range(len(k_vec)):
        k_exc = k_vec[kv]
        cost_min = np.loadtxt(path+"N%d_k%d_cost_min.txt"%(N,k_exc))
        plt.semilogy(Ts,cost_min,'-',color=colors[k_exc-1],marker=symbols[k_exc-1],label="$k=%d$"%k_exc)    
    
    plt.legend(loc='upper right',fontsize=12,frameon=False)
    plt.xlabel(r"$T/T_\beta$ [control time]",size=13)
    plt.ylabel(r"$J_{\mathrm{opt}}$ [optimized cost]",size=13)

plt.tight_layout()
plt.savefig(save_dir+"QOC-Fig3.png",dpi=300)
# ax[1]: Tmin (\sim QSL time) as a function of nu0