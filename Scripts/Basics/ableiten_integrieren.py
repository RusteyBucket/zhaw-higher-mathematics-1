from sympy import diff, integrate, sympify


# noinspection PyShadowingNames
def ableiten(funktion: str, symbol = None):
	funktion = sympify(funktion)

	if symbol is None:
		return diff(funktion)

	return diff(funktion, symbol)


# noinspection PyShadowingNames
def integrieren(funktion: str, symbol = None):
	funktion = sympify(funktion)

	if symbol is None:
		return integrate(funktion)

	return integrate(funktion, symbol)


########################################################################################

# Funktion definieren
funktion = "sqrt(1 - x)"

print(f"Ableitung: {ableiten(funktion)}")
# print(f"Ableitung: {ableiten(funktion, 'x')}") # Für Ableitung nach x (bei mehreren freien Variablen
# print(f"Integral: {integrieren(funktion)}")

# Werte für Unbekannte definieren
# werte = {"x": 0.8}

# print(f"Ergebnis von Ableitung: {ableiten(funktion).subs(werte).evalf()}")
# print(f"Ergebnis von Funktion: {sympify(funktion).subs(werte).evalf()}")