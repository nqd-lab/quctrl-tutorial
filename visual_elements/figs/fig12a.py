import numpy as np
import matplotlib.pyplot as plt

# fix seed
seed=0 
np.random.seed(seed)

# fix output array
np.set_printoptions(suppress=True,precision=2) 

path = "../../data/raw/Fig12a/"


plt.style.use("./ctrl_tutorial_plot_style.mplstyle")
plt.style.use("./ctrl_tutorial_plot_texstyle.mplstyle")
save_dir="./generated_figs/"

plt.rcParams["figure.figsize"] = [6.0, 6.0] 


############################################################

save=True


data = np.load(path+'PG-1_qubit_training.npz')


episodes=data['episodes'] 
mean_final_reward=data['mean_final_reward'] 
std_final_reward=data['std_final_reward'] 
min_final_reward=data['min_final_reward']
max_final_reward=data['max_final_reward']


plt.plot(episodes, mean_final_reward, '-k', label='batch average' )
plt.fill_between(episodes, 
                 mean_final_reward-0.5*std_final_reward, 
                 mean_final_reward+0.5*std_final_reward, 
                 color='k', 
                 alpha=0.25)

plt.plot(episodes, min_final_reward, '.b' , markersize=2, label='batch minimum' )
plt.plot(episodes, max_final_reward, '.r' , markersize=2, label='batch maximum' )

plt.xlabel('training episode')
plt.ylabel('$r_T{=}|\\langle\\psi_\\ast|\\psi(T)\\rangle|^2$ [final reward]')

plt.legend(loc='lower right', markerscale=4., )
plt.grid()

plt.text(-100,1.0, '(a)', ha='left', va='top', fontsize=16)


plt.tight_layout()

if save:
	plt.savefig(save_dir + 'RL-1q_training-curve.pdf')
	plt.savefig(save_dir + 'RL-1q_training-curve.png', dpi=300)
else:
	plt.show()




plt.close()








