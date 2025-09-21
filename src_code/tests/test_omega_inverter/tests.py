import unittest
from ..core import OmegaInverter

class TestOmegaInverter(unittest.TestCase):
    """
    Unit tests for the OmegaInverter class.
    """

    def test_inversion_accuracy(self):
        """
        Test that the inverted value E gives back the original Omega within tolerance.
        """
        inverter = OmegaInverter()
        h_test = 0.1
        for Omega in [1.5, 6.0, 8.0, 9.5]:
            E = inverter.invert_omega(Omega, h_test)
            error, Omega_check = inverter.verify_inversion(Omega, h_test, E)
            self.assertLess(error, 1e-8)

    def test_derivative_region_1(self):
        """
        Test that the computed derivative dΩ/dE in region 1 is positive.
        """
        inverter = OmegaInverter()
        E, h = 0.5, 0.1
        dOmega = inverter.omega_derivative_region_1(E, h)
        self.assertTrue(dOmega > 0)