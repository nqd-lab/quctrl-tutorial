# Jupyter Notebooks to "Taming quantum systems: A tutorial for using shortcuts-to-adiabaticity, quantum optimal control, and reinforcement learning"

This repository contains the `python` notebooks accompanying the paper *"Taming quantum systems: A tutorial for using shortcuts-to-adiabaticity, quantum optimal control, and reinforcement learning"*, [arXiv:2501.16436](https://arxiv.org/abs/2501.16436).

## 📂 Repository Structure

```
src_code/
├── notebooks/                          # Tutorial notebooks organized by topic
│   ├── shortcuts_to_adiabaticity/      # Shortcuts-to-adiabaticity tutorials
│   ├── quantum_optimal_control/        # Quantum optimal control tutorials
│   └── reinforcement_learning/         # Reinforcement learning for quantum control
└── src/                                # Supporting Python libraries
    └── Bloch_sphere_lib/               # Bloch sphere visualization utilities
```

## � Quick Start

1. **Install dependencies:**
```bash
# Create virtual environment
python -m venv .quctrl
source .quctrl/bin/activate  # On Windows: .quctrl\Scripts\activate

# Install all dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

2. **Launch Jupyter Lab:**
```bash
jupyter lab
```

3. **Choose a tutorial** from the sections below and execute cells sequentially.

## 📚 Tutorial Sections

### ⚡ Section II: Shortcuts-to-Adiabaticity

| Notebook | Description | Key Topics |
|----------|-------------|------------|
| [`Landau_Zener_and_Ising_Models.ipynb`](notebooks/shortcuts_to_adiabaticity/Landau_Zener_and_Ising_Models.ipynb) | STA protocols for Landau-Zener and Ising models | Counter-diabatic driving, STA design |
| [`LMG_Model.ipynb`](notebooks/shortcuts_to_adiabaticity/LMG_Model.ipynb) | Shortcuts-to-adiabaticity for Lipkin-Meshkov-Glick model | Many-body STA, collective spin systems |

### 🔬 Section III: Quantum Optimal Control

| Notebook | Description | Key Topics |
|----------|-------------|------------|
| [`lz_qoc_notebook.ipynb`](notebooks/quantum_optimal_control/lz_qoc_notebook.ipynb) | Quantum optimal control for two-level systems | Landau-Zener transitions, GRAPE algorithm |
| [`spinj_state_qoc_notebook.ipynb`](notebooks/quantum_optimal_control/spinj_state_qoc_notebook.ipynb) | State preparation in spin-j systems | Multi-level quantum control, state targeting |
| [`unit_grape_tls_notebook.ipynb`](notebooks/quantum_optimal_control/unit_grape_tls_notebook.ipynb) | Unitary evolution control for two-level systems | GRAPE for unitary gates, pulse optimization |

### 🤖 Section IV: Reinforcement Learning for Quantum Control

| Notebook | Description | Key Topics |
|----------|-------------|------------|
| [`PG_quant-env_qubit.ipynb`](notebooks/reinforcement_learning/PG_quant-env_qubit.ipynb) | Policy gradient for quantum-stochastic qubit control | RL agents, quantum environments, noise modeling |
| [`PG-STA.ipynb`](notebooks/reinforcement_learning/PG-STA.ipynb) | Policy gradient for shortcuts-to-adiabaticity | RL-optimized STA protocols, adiabatic shortcuts |
| [`PG_state_prep.ipynb`](notebooks/reinforcement_learning/PG_state_prep.ipynb) | RL for quantum state preparation | State targeting with RL, fidelity optimization |

Remarks:
  * all RL notebooks are inherently stochastic. The seed of the random number generator is fixed for reproducibility within a given session, but not across different platforms or compute architectures. Therefore, the plots are not expected to look as in the tutorial paper; 
  * `PG-STA.ipynb` may take long to train the model. 

## 🛠️ Supporting Libraries

### Bloch Sphere Visualization ([`src/Bloch_sphere_lib/`](src/Bloch_sphere_lib/))

Adapted visualization tools based on [`QuTip`](https://qutip.org/) functionality.

**Key Components:**

- **`Bloch`** class ([`qutip_bloch.py`](src/Bloch_sphere_lib/qutip_bloch.py)): Core Bloch sphere visualization
  - `add_states()`: Add quantum states as vectors
  - `add_points()`: Add trajectory points  
  - `add_annotation()`: Add text annotations

- **`Bloch_plots()`** ([`Bloch_lib.py`](src/Bloch_sphere_lib/Bloch_lib.py)): Static plot generation
- **`Bloch_movie()`** ([`Bloch_lib.py`](src/Bloch_sphere_lib/Bloch_lib.py)): Animation creation

## � Learning Path

**Recommended sequence for newcomers:**

1. **Start with Section II** (Shortcuts-to-Adiabaticity) for fundamental concepts
2. **Proceed to Section III** (Quantum Optimal Control) for optimization techniques  
3. **Explore Section IV** (Reinforcement Learning) for advanced methods

Each notebook provides:
- **Mathematical background** and theoretical foundations
- **Practical implementations** using JAX, NumPy, and scientific computing libraries
- **Interactive visualizations** including Bloch sphere animations
- **Exercise questions** to deepen understanding

For detailed theoretical background, refer to the accompanying tutorial paper. 


