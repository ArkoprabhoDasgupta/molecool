
import molecool
import numpy as np
from molecool.molecules import compute_molecular_mass

def test_compute_molecular_mass():

    symbols = ["C", "H", "H", "H", "H"]
    calculated_mass = compute_molecular_mass(symbols)

    expected_mass = 16.01

    assert np.isclose(expected_mass, calculated_mass, rtol=1e-2)
