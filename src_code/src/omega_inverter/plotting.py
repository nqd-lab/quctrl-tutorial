import numpy as np
import matplotlib.pyplot as plt

def plot_omega_and_inverse(inverter, h_test, num_points=50):
    """
    Plot the function Ω(E, h) and its inverse E(Ω, h) for a given value of h.

    Parameters
    ----------
    inverter : OmegaInverter
        An instance of OmegaInverter.
    h_test : float
        The value of h to fix for plotting.
    num_points : int
        Number of points in the sampling grid.
    """
    E_GS = -(1 + h_test**2) if abs(h_test) < 1.0 else -2.0 * abs(h_test)
    E_range = np.linspace(E_GS + 1E-13, 5, num_points)
    Omega_range = [inverter.omega_function(E, h_test) for E in E_range]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(E_range, Omega_range, 'b-', linewidth=2, label=f'Ω(E, h={h_test})')
    ax1.axvline(-2*h_test, color='k', linestyle='-.', alpha=0.7, label='E = -2h')
    ax1.set_xlabel('E')
    ax1.set_ylabel('Ω')
    ax1.set_title('Ω(E, h)')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    Omega_range_inv = np.linspace(min(Omega_range), max(Omega_range), num_points)
    E_range_inv_brent = [inverter.invert_omega(Omega, h_test, method='brent') for Omega in Omega_range_inv]
    E_range_inv_newton = [inverter.invert_omega(Omega, h_test, method='newton') for Omega in Omega_range_inv]

    ax2.plot(Omega_range_inv, E_range_inv_brent, 'r-', linewidth=2, label=f'E(Ω, h={h_test}) [Brent]')
    ax2.plot(Omega_range_inv, E_range_inv_newton, 'g--', linewidth=1.5, label=f'E(Ω, h={h_test}) [Newton]')
    ax2.axhline(-2*h_test, color='k', linestyle='-.', alpha=0.7, label='E = -2h')
    ax2.set_xlabel('Ω')
    ax2.set_ylabel('E')
    ax2.set_title('E(Ω, h)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.show()