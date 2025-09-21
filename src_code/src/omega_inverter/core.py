import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, fsolve

class OmegaInverter:
    """
    Class to compute and invert the function Ω(E, h), defined by two regions.

    Region 1 (E > -2h):
        Ω(E,h) = 2π + 2 * ∫₀^π [(E + cos²q) / (h + √(h² + E cos²q + cos⁴q))] dq

    Region 2 (E < -2h and h < 1):
        Ω(E,h) = 8 * ∫₀^{q_max} [√(h² + E cos²q + cos⁴q) / cos²q] dq

    with q_max = arccos(√((-E + √(E² - 4h²))/2))

    Provides high-precision numerical integration and root-finding utilities.
    """

    def __init__(self, integration_tolerance=1e-10, root_tolerance=1e-10):
        self.int_tol = integration_tolerance
        self.root_tol = root_tolerance

    def omega_function_region_1(self, E, h):
        def integrand(q):
            cos2_q = np.cos(q)**2
            cos4_q = cos2_q**2
            numerator = E + cos2_q
            denominator = h + np.sqrt(h**2 + E * cos2_q + cos4_q)
            return numerator / denominator
        integral, _ = quad(integrand, 0, np.pi, epsabs=self.int_tol, epsrel=self.int_tol, limit=100)
        return 2 * np.pi + 2 * integral

    def _compute_qmax(self, E, h):
        discriminant = E**2 - 4*h**2
        if discriminant < 0:
            raise ValueError(f"Invalid parameters: E²-4h² = {discriminant} < 0")
        inner_expression = -E + np.sqrt(discriminant)
        if inner_expression < 0:
            raise ValueError(f"Expression -E + √(E²-4h²) = {inner_expression} < 0")
        return np.arccos(np.sqrt(inner_expression) / np.sqrt(2))

    def omega_function_region_2(self, E, h):
        q_max = self._compute_qmax(E, h)
        def integrand(q):
            cos2_q = np.cos(q)**2
            cos4_q = cos2_q**2
            under_sqrt = h**2 + E * cos2_q + cos4_q
            return np.sqrt(under_sqrt) / cos2_q if abs(cos2_q) > 1e-14 else np.inf
        integral, _ = quad(integrand, 0.0, q_max, epsabs=self.int_tol, epsrel=self.int_tol, limit=100)
        return 8 * integral

    def omega_function(self, E, h):
        if E > -2.0 * h:
            return self.omega_function_region_1(E, h)
        elif E < -2.0 * h and h < 1.0:
            return self.omega_function_region_2(E, h)
        else:
            raise ValueError("E and/or h value out of range.")

    def omega_derivative_region_1(self, E, h):
        def integrand(q):
            cos2_q = np.cos(q)**2
            cos4_q = cos2_q**2
            denominator = h + np.sqrt(h**2 + E * cos2_q + cos4_q)
            return 1.0 / denominator
        integral, _ = quad(integrand, 0, np.pi, epsabs=self.int_tol, epsrel=self.int_tol)
        return 2 * integral

    def omega_derivative_region_2(self, E, h):
        q_max = self._compute_qmax(E, h)
        def integrand(q):
            cos2_q = np.cos(q)**2
            cos4_q = cos2_q**2
            return np.sqrt(h**2 + E * cos2_q + cos4_q)
        integral, _ = quad(integrand, 0.0, q_max, epsabs=self.int_tol, epsrel=self.int_tol)
        return 4 * integral

    def invert_omega_brent(self, Omega_target, h):
        def f(E):
            return self.omega_function(E, h) - Omega_target
        E_min = -(1 + h**2) if abs(h) < 1.0 else -2.0 * abs(h) + 1e-10
        E_test = max(0, -h)
        while self.omega_function_region_1(E_test, h) < Omega_target:
            E_test += max(1, abs(h))
        E_max = E_test + max(1, abs(h))
        f_min, f_max = f(E_min), f(E_max)
        if f_min * f_max > 0:
            delta = 0.1 * abs(h)
            if f_min > 0:
                while f_min > 0 and E_min > -50 * abs(h):
                    E_min -= delta
                    f_min = f(E_min)
            else:
                while f_max < 0:
                    E_max += delta
                    f_max = f(E_max)
        return brentq(f, E_min, E_max, xtol=self.root_tol, rtol=self.root_tol)

    def invert_omega_newton(self, Omega_target, h, E_initial=None):
        if E_initial is None:
            guess_func = self.omega_function
            try:
                guess = guess_func(-2*h + 1e-6, h)
                E_initial = max(-2 * h + 0.1, 0) if Omega_target > guess else min(-2*h - 0.1, -1)
            except:
                E_initial = 0
        return fsolve(lambda E: self.omega_function(E, h) - Omega_target,
                      E_initial,
                      xtol=self.root_tol)[0]

    def invert_omega(self, Omega_target, h, method='brent'):
        if method == 'brent':
            return self.invert_omega_brent(Omega_target, h)
        elif method == 'newton':
            return self.invert_omega_newton(Omega_target, h)
        else:
            raise ValueError("Method must be 'brent' or 'newton'")

    def verify_inversion(self, Omega_target, h, E_result):
        Omega_computed = self.omega_function(E_result, h)
        return abs(Omega_computed - Omega_target), Omega_computed