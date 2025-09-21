import numpy as np
import matplotlib.pyplot as plt
 
plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

path = "../../data/processed/Fig5/"

fig, axs = plt.subplots(3,1, sharex=True)
fig.subplots_adjust(wspace=1)

npzfile = np.load(path+'N2timeloop.npz')
overlap = npzfile['bare']
overlapCD1 = npzfile['CD1']
overlapCD2 = npzfile['CD2']
times = npzfile['times']

axs[0].scatter(times,1-overlap,s=10,marker='h',c='blue')
axs[0].scatter(times,1-overlapCD1,s=10,marker='s',c='red')
axs[0].scatter(times,1-overlapCD2,s=10,marker='o',c='black')
axs[0].set_ylim(1e-9,1)
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].text(8e2,2e-1, '(a)', ha='left', va='top', fontsize=16)

npzfile = np.load(path+'N3timeloop.npz')
overlap = npzfile['bare']
overlapCD1 = npzfile['CD1']
overlapCD2 = npzfile['CD2']
times = npzfile['times']

axs[1].scatter(times,1-overlap,s=10,marker='h',c='blue')
axs[1].scatter(times,1-overlapCD1,s=10,marker='s',c='red')
axs[1].scatter(times,1-overlapCD2,s=10,marker='o',c='black')
axs[1].set_ylabel(r"$1-\mathcal{F}$ [fidelity]")
axs[1].set_ylim(1e-9,1)
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].text(8e2,2e-1, '(b)', ha='left', va='top', fontsize=16)

npzfile = np.load(path+'N4timeloop.npz')
overlap = npzfile['bare']
overlapCD1 = npzfile['CD1']
overlapCD2 = npzfile['CD2']
times = npzfile['times']

axs[2].scatter(times,1-overlap,s=10,marker='h',c='blue')
axs[2].scatter(times,1-overlapCD1,s=10,marker='s',c='red')
axs[2].scatter(times,1-overlapCD2,s=10,marker='o',c='black')
axs[2].set_xlabel(r"$\tau J$ [protocol time]")
axs[2].set_ylim(1e-9,1)
axs[2].set_xscale('log')
axs[2].set_yscale('log')
axs[2].text(8e2,2e-1, '(c)', ha='left', va='top', fontsize=16)

plt.savefig(save_dir + 'IsingVarCDPlots.pdf',dpi=300)


fig1, axs1 = plt.subplots(1,1)
fig1.subplots_adjust(wspace=1)

Ns = [2,3,4,5,6,7,8,9,10] 
overlap = []
overlapCD1 = []
overlapCD2 = []
Nsp = []
for i in range(len(Ns)):
  npzfile = np.load(path+'Nplot_' + str(Ns[i]) + '.npz')
  overlap.append(npzfile['bare'])
  overlapCD1.append(npzfile['CD1'])
  overlapCD2.append(npzfile['CD2'])
  Nsp.append(npzfile['Ns'])
overlap = np.array(overlap)
overlapCD1 = np.array(overlapCD1)
overlapCD2 = np.array(overlapCD2)


axs1.scatter(Ns,1-overlap,s=26,marker='h',c='blue', label='no control term')
axs1.scatter(Ns,1-overlapCD1,s=26,marker='s',c='red', label='one-body local CD')
axs1.scatter(Ns,1-overlapCD2,s=26,marker='o',c='black',clip_on=False, label='two-body local CD')
axs1.set_ylabel(r"$1-\mathcal{F}$ [fidelity]")
axs1.set_xlabel(r"$N$ [system size]")
axs1.set_ylim(0,1)
axs1.text(1.8,0.98, '(d)', ha='left', va='top', fontsize=16)
axs1.legend()

#plt.show()
plt.savefig(save_dir + 'IsingNPlot.pdf',dpi=300)
