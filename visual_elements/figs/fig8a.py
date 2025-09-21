# QOC_FIGURE2-A.PY (UNITARY CONTROL)
# author: pmpoggi @ strath (november 2024)
# ------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

path = "../../data/processed/Fig8a/"

# General definitions
omega = 1 # Rabi freq
T0 = 2*np.pi/(omega)
[red_new, blue_new, orange_new] = ["#A52639","#336EFF","tab:orange"] #some colors

# FIGURE 2 - A - this is a 2x2 subplot array
# ------------------------------------------

t = np.loadtxt(path+"Time.txt") # time variable (common to all)

plt.figure(1,figsize=(5.5,5))
phi0s = np.array([0.5,1])*np.pi
subplot_ind = np.array([[1,2],[3,4]])
caption_ind = np.array([["(a)","(b)"],["(c)","(d)"]])
guesses = ['random','linear']
guess_lab = [r"random $\bm{\alpha}_0$", r"linear $\bm{\alpha}_0$"]
# guess_lab = [r"random $\bm{\alpha}_0$", r"$\bm{\alpha}_0=0$"]
colors = [blue_new,orange_new]
for i in range(2):
    phi = phi0s[i]
    for j in range(2):
        guess = guesses[j]    
        
        plt.subplot(2,2,subplot_ind[i,j])
        plt.title(r"$\phi=%.1f\pi$. "%(phi/np.pi) + guess_lab[j])
        [cost_ini,cost_opt] = np.loadtxt(path+"cost_values_phi_%.2f_"%(phi/np.pi)+guess+".txt")
        field_ini=  np.loadtxt(path+"field_ini_phi_%.2f_"%(phi/np.pi)+guess+".txt")
        field_opt = np.loadtxt(path+"field_opt_phi_%.2f_"%(phi/np.pi)+guess+".txt")
        
        plt.stairs(field_ini,t/T0,baseline=None,linestyle='--',linewidth=1.7,color='0.6')
        plt.stairs(field_opt,t/T0,baseline=None,linewidth=2.2,color=colors[j])
        plt.ylim([-4,4])
        plt.yticks([-np.pi,0,np.pi],[r'$-\pi$','$0$',r'$\pi$'])
        plt.xlabel(r"$t/T_U$ [time]",size=12)
        plt.ylabel(r"$\alpha(t)$ [field]",size=12)
        plt.text(-0.01,3.7, caption_ind[i,j], ha='left', va='top',fontsize=12)
        
        # Positions of the fidelity values got tricky here...
        if j == 0: # random guesses
            plt.text(-0.01,-2.9, "$J_0=%.2f$"%cost_ini, ha='left', va='top',fontsize=13,color='0.5')
            plt.text(0.35,3.5, "$J_\mathrm{opt}=$"+"${:.2e}$".format(cost_opt), ha='left', va='top',fontsize=13,color=colors[j])
        if j == 1: # linear
            plt.text(0.15,3.5, "$J_0=%.2f$"%cost_ini, ha='left', va='top',fontsize=13,color='0.5')
            plt.text(0.3,-2.9, "$J_\mathrm{opt}=$"+"${:.2e}$".format(cost_opt), ha='left', va='top',fontsize=13,color=colors[j])

plt.tight_layout()

#plt.show()
plt.savefig(save_dir + "QOC-Fig2-A.pdf",dpi=300)
