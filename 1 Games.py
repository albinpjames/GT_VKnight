# %%
# 1 Using NumPy to Compute Expected Utilities
import numpy as np

M_r = np.array(
    (
        (1, -1),
        (-1, 1),
    )
)
M_c = -M_r

sigma_r = np.array((0.2, 0.8))
sigma_c = np.array((0.6, 0.4))
print(f"Column player expected utility: {sigma_r @ M_c @ sigma_c}")
print(f"Row player expected utility: {sigma_r @ M_r @ sigma_c}")

# %%
# 2 Using Nashpy to Create Games and Compute Utilities
import nashpy as nash

matching_pennies = nash.Game(M_r, M_c)
print(matching_pennies)

# %%
# 3 Creating a 3 player game using Gambit
import pygambit as gbt

g = gbt.Game.new_table([2, 2, 2], title="3 player game")
p1, p2, p3 = g.players

g[(0, 0, 0)][p1] = 1
g[(0, 0, 0)][p2] = 1
g[(0, 0, 0)][p3] = 1

g[(0, 0, 1)][p1] = 2
g[(0, 0, 1)][p2] = 1
g[(0, 0, 1)][p3] = -1

g[(0, 1, 0)][p1] = 2
g[(0, 1, 0)][p2] = 1
g[(0, 1, 0)][p3] = -1

g[(0, 1, 1)][p1] = 2
g[(0, 1, 1)][p2] = 1
g[(0, 1, 1)][p3] = -1

g[(1, 0, 0)][p1] = 2
g[(1, 0, 0)][p2] = 1
g[(1, 0, 0)][p3] = -1

g[(1, 0, 1)][p1] = 2
g[(1, 0, 1)][p2] = 1
g[(1, 0, 1)][p3] = -1

g[(1, 1, 0)][p1] = 2
g[(1, 1, 0)][p2] = 1
g[(1, 1, 0)][p3] = -1

g[(1, 1, 1)][p1] = 1
g[(1, 1, 1)][p2] = 1
g[(1, 1, 1)][p3] = 1
print(g)
