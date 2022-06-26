#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("data.txt", names=["population", "profit"])
# %%
## Split population and profit into X and y
x = df.population.to_numpy()
y = df.profit.to_numpy()

## Length, or number of observations, in our data
m = len(y)
# %%
plt.figure(figsize=(10, 8))
plt.plot(x, y, "kx")
plt.xlabel("Population of City in 10,000s")
plt.ylabel("Profit in $10,000s")

# %%
a = 2
b = 25

# Compute loss for single a,b or a full grid of them
def compute_loss(a_est, b_est):
    return np.mean(np.square(y - (a_est * x + b_est)), 2)


# Some tricky matrix manipulations in this cell. The main goal is to visualize the loss function for all values of a and b.
a_explore_range = 20
a_explore_step = 0.1

# Since b has less impact on loss function, moving to larger values
b_explore_range = 200
b_explore_step = 1

# We can chnage above values to see how the parameters impact the model

# Get full ranges of a and b
a_est_range = np.arange(a - a_explore_range, a + a_explore_range, a_explore_step)
b_est_range = np.arange(b - b_explore_range, b + b_explore_range, b_explore_step)

# Make them into a grid. b first, as we want a to change along rows
bgrid, agrid = np.meshgrid(b_est_range, a_est_range)

# I absolutely hate for loops and I know linear algebra, hence this bit of code
# We are doing this is because the x and y are vectors
size_x = np.int(a_explore_range / a_explore_step * 2)
size_y = np.int(b_explore_range / b_explore_step * 2)
agrid_tiled = np.tile(np.reshape(agrid, [size_x, size_y, 1]), [1, 1, x.shape[0]])
bgrid_tiled = np.tile(np.reshape(bgrid, [size_x, size_y, 1]), [1, 1, x.shape[0]])

# Whoosh! Loss for the full grid at once
loss_full_grid = compute_loss(agrid_tiled, bgrid_tiled)

# Change these values and move around the plot to look at it from different angles
azimuth_angle = 25.0
elevation_angle = 35

fig = plt.figure(figsize=[12, 8])
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=elevation_angle, azim=azimuth_angle)
ax.plot_surface(agrid, bgrid, loss_full_grid)
ax.set_xlabel("a", fontsize=15)
ax.set_ylabel("b", fontsize=15)
ax.set_zlabel("Loss", fontsize=15)

ax.set_title("Visualization of the loss function", fontsize=15)
# ax.set_aspect('equal')
# %%
