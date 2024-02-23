import sympy as sp

# Define the symbol
x = sp.Symbol('x')

# Define the integrand
integrand = x**2 * sp.sin(x)

# Perform the integration
integral = sp.integrate(integrand, x)
print(integral)
