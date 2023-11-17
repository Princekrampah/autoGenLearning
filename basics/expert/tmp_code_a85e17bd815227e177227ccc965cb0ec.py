from sympy import symbols, Eq, solve

# Define the symbols
a, b, c, x, y = symbols('a b c x y')

# Define the equations
eq1 = Eq(a*x + b*y + c, x + 7)
eq2 = Eq(a + b*x + c*y, 2*x + 6*y)
eq3 = Eq(a*y + b + c*x, 4*x + y)

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (a, b, c))

# Print the solution
print(solution)