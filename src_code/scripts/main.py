import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from omega_inverter import core, plotting
from omega_inverter.plotting import plot_omega_and_inverse
import unittest

if __name__ == '__main__':
    inverter = core.OmegaInverter()
    plotting.plot_omega_and_inverse(inverter, h_test=0.1)
    unittest.TestLoader().discover('../tests/test_omega_inverter')