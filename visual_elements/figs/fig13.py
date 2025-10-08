import os, sys

import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.use('Qt5Agg')

path = "../../data/raw/Fig13/"

plt.style.use("./ctrl_tutorial_plot_style_widetextfig_3x1.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"


save=True # 
#save=False #


data = np.load(path+'PG-STA_protocol.npz')

times=data['times'] 
fidelity_inst_t=data['fidelity_inst_t']
fidelity_t=data['fidelity_t'] 
RL_field_t=data['RL_field_t']
CD_protocol_t=data['CD_protocol_t']
exact_CD_protocol=data['exact_CD_protocol']
reward_RL=data['reward_RL']
reward_CD_approx=data['reward_CD_approx']


fig, ax = plt.subplots(figsize=(7,6))

ax.step(times, CD_protocol_t, '.-b', where='pre', label='discretized CD, $r_T={0:0.3f}$'.format(reward_CD_approx) )
ax.step(times, RL_field_t, '.-g', where='pre', label='RL agent, $r_T={0:0.3f}$'.format(reward_RL) )
ax.plot(times, exact_CD_protocol,'--r', label='exact CD, $r_T=\\infty$' )
ax.legend()

ax.set_xlabel('$t$ [time]')
ax.set_ylabel('drive protocol')

#plt.tight_layout()
plt.grid()

plt.text(-0.25,-0.26, '(b)', ha='left', va='top', fontsize=20)

if save:
	plt.savefig(save_dir + 'PG-STA_protocols.pdf')
else:
	plt.show()

plt.close()


##########################


fig, ax1 = plt.subplots(figsize=(7,6))

plt.text(-0.245,1.04, '(c)', ha='left', va='top', fontsize=20)


# These are in unitless percentages of the figure size. (0,0 is bottom left)
left, bottom, width, height = [0.6, 0.2, 0.38, 0.3]
ax2 = fig.add_axes([left, bottom, width, height])


#ax1.axhline(y=1.0, color='k', linestyle='-', linewidth=1.0)
ax1.step(times, fidelity_t, '.-g', where='pre',label='$|\\langle\\psi_\\ast|\\psi(T)\\rangle|^2$')
ax1.step(times, fidelity_inst_t, '.-',color='brown', where='pre',label='$|\\langle\\mathrm{GS}(t)|\\psi(t)\\rangle|^2$',)
ax2.step(times, np.log10(1-fidelity_t), '.-g', where='pre',)
ax2.step(times, np.log10(1-fidelity_inst_t), '.-',color='brown', where='pre',)
#ax2.set_yscale('log')

ax1.legend(loc='upper left')

ax1.set_xlabel('time $t$')
ax1.set_ylabel('$\mathcal{F}$ [fidelity]', )

ax2.set_xlabel('$t$ [time]')
ax2.set_ylabel('$\\log_{10}$-infidelity', )

ax1.grid()
ax2.grid()



#plt.tight_layout()

if save:
	plt.savefig(save_dir + 'PG-STA_fidelity.pdf')
else:
	plt.show()

plt.close()


#exit()

############################################################




data = np.load(path+'PG-STA_training.npz')


episodes=data['episodes'] 
mean_final_reward=data['mean_final_reward'] 
std_final_reward=data['std_final_reward'] 
min_final_reward=data['min_final_reward']
max_final_reward=data['max_final_reward']


fig, ax = plt.subplots(figsize=(7,6))


ax.plot(episodes, mean_final_reward, '-k', label='batch average' )
ax.fill_between(episodes, 
                 mean_final_reward-0.5*std_final_reward, 
                 mean_final_reward+0.5*std_final_reward, 
                 color='k', 
                 alpha=0.25)

ax.plot(episodes, min_final_reward, '.b' , markersize=1, label='batch minimum' )
ax.plot(episodes, max_final_reward, '.r' , markersize=1, label='batch maximum' )

ax.set_xlabel('training episode')
ax.set_ylabel('$r_T{=}{-}\\log_{10}\\left(1{-}\\mathcal{F}\\right)$ [final reward]')

ax.legend(loc='best', markerscale=4.,)
ax.grid()

#fig.tight_layout()

plt.text(-2400,9.8, '(a)', ha='left', va='top', fontsize=20)

if save:
	plt.savefig(save_dir + 'PG-STA_training-curve.pdf')
	plt.savefig(save_dir + 'PG-STA_training-curve.png', dpi=300)
else:
	plt.show()

plt.close()








