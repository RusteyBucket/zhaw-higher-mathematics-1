from typing import Any

import numpy as np


def spektrum(matrix: np.ndarray[Any, Any], debug: bool = False):
	eigenwerte = np.linalg.eigvals(matrix)

	if debug:
		print(f"Eigenwerte: {eigenwerte}")
		print()

	return eigenwerte.size


########################################################################################

# Matrix definieren
matrix = np.array([[1, 0, 0], [2, 3, 0], [0, 1, 2]])

print(f"Spektrum: {spektrum(matrix, True)}")