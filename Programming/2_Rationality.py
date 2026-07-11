# %%
# Computing utilities of all actions with Numpy
import numpy as np

M_r = np.array(
    (
        (0, -1, 1, 1, -1),
        (1, 0, -1, -1, 1),
        (-1, 1, 0, 1, -1),
        (-1, 1, -1, 0, 1),
        (1, -1, 1, -1, 0),
    )
)

sigma_2 = np.array((1 / 4, 0, 0, 3 / 4, 0))
print(f"Expected utility of each action: {M_r @ sigma_2}")
# %%
# Finding non zero entries of an array with Numpy
sigma_1 = np.array((1 / 3, 0, 1 / 3, 1 / 3, 0))
print(f"Indices of actions played: {sigma_1.nonzero()}")
# %%
# Checking the best response condition with Numpy
played_actions_maximise = (M_r @ sigma_2)[sigma_1.nonzero()] == (M_r @ sigma_2).max()
print(f"Each played action achieves the maximum utility: {played_actions_maximise}")

# %%
sigma_1 = np.array((1, 0, 0, 0, 0))
played_actions_maximise = (M_r @ sigma_2)[sigma_1.nonzero()] == (M_r @ sigma_2).max()
print(f"Each played action achieves the maximum utility: {played_actions_maximise}")

# %%
# Checking best response condition with Nashpy
import nashpy as nash

rpsls = nash.Game(M_r, - M_r)
print(f"Best response check (sigma_1, sigma_2): "
      f"{rpsls.is_best_response(sigma_r=sigma_1, sigma_c=sigma_2)}")
