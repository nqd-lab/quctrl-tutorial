# QOC_FIGURE1-A.PY (STATE CONTROL - LEFT PLOT)
# author: pmpoggi @ strath (november 2024)
# ------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


#plt.style.use("../ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

path = "../../data/processed/Fig7a/"

# General definitions
Delta = 1 # LZ gap
T0 = np.pi/(2*Delta) 
[red_new, blue_new, orange_new] = ["#A52639","#336EFF","tab:orange"] #some colors

# FIGURE 1 - A - this is a 2x2 subplot array
# ------------------------------------------

t = np.loadtxt(path+"Time.txt") # time variable (common to all)

plt.figure(2,figsize=(5.5,5))
nu0s = [1,5]
subplot_ind = np.array([[1,2],[3,4]])
caption_ind = np.array([["(a)","(b)"],["(c)","(d)"]])
guesses = ['random','zero']
guess_lab = [r"random $\bm{\alpha}_0$", r"$\bm{\alpha}_0=0$"]
colors = [blue_new,orange_new]
for i in range(2):
    nu0 = nu0s[i]
    for j in range(2):
        guess = guesses[j]    
        
        plt.subplot(2,2,subplot_ind[i,j])
        plt.title(r"$\nu_0=%d.$ "%nu0 + guess_lab[j])
        [cost_ini,cost_opt] = np.loadtxt(path+"cost_values_nu0_%d_"%nu0+guess+".txt")
        field_ini=  np.loadtxt(path+"field_ini_nu0_%d_"%nu0+guess+".txt")
        field_opt = np.loadtxt(path+"field_opt_nu0_%d_"%nu0+guess+".txt")
        
        plt.stairs(field_ini,t/T0,baseline=None,linestyle='--',linewidth=1.7,color='0.6')
        plt.stairs(field_opt,t/T0,baseline=None,linewidth=2.2,color=colors[j])
        plt.ylim([-2,2])
        plt.xlabel(r"$t/T_0$ [time]",size=12)
        plt.ylabel(r"$\alpha(t)$ [field]",size=12)
        plt.text(-0.01,1.82, caption_ind[i,j], ha='left', va='top',fontsize=12)
        plt.text(-0.01,-1.45, "$J_0=%.2f$"%cost_ini, ha='left', va='top',fontsize=13,color='0.5')
        plt.text(0.5,1.82, "$J_\mathrm{opt}=$"+"${:.2e}$".format(cost_opt), ha='left', va='top',fontsize=13,color=colors[j])



plt.tight_layout()
#plt.show()
plt.savefig(save_dir + "QOC-Fig1-A.pdf",dpi=300)
