import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.animation as animation

def f(x, y):
	return -1 * np.sin(0.5*x**2-0.25*y**2+3) * np.cos(2*x+1-np.exp(y))

def fdx(x, y):
	return 2 * np.sin(2 * x - np.exp(y) + 1) * np.sin(0.5 * x**2 - 0.25 * y**2 + 3) - x * np.cos(2 * x - np.exp(y) + 1) * np.cos(0.5 * x**2 - 0.25 * y**2 + 3)

def fdy(x, y):
	return -1 * np.exp(y) * np.sin(2 * x - np.exp(y) + 1) * np.sin(0.5 * x**2 - 0.25 * y**2 + 3) + 0.5 * y * np.cos(2 * x - np.exp(y) + 1) * np.cos(0.5 * x**2 - 0.25 * y**2 + 3)

lin_param = (-1, 1, 1000)
xx = np.linspace(*lin_param)
yy = np.linspace(*lin_param)

x, y = np.meshgrid(xx, yy)
z = f(x, y)
color_list = plt.rcParams['axes.prop_cycle'].by_key()['color']
levelsf = MaxNLocator(nbins=100).tick_values(z.min(), z.max())
levels = MaxNLocator(nbins=20).tick_values(z.min(), z.max())

fig, ax = plt.subplots()

x_est = -0.3
y_est = 0.4
r = 0.5  # Learning rate

x_list = []
y_list = []
colorbar_exist = False
def animate(i):

	global colorbar_exist
	global x_est
	global y_est
	global z_est

	ax.clear()
	cf = ax.contourf(x, y, z, levels=levelsf)
	cs = ax.contour(x, y, z, levels=levels, colors="white")
	ax.clabel(cs, fontsize=9, inline=1)
	if not colorbar_exist:
		fig.colorbar(cf)
		colorbar_exist = True
	
	z_est = f(x_est, y_est)
	ax.scatter(x_est, y_est, c="r")
	x_list.append(x_est)
	y_list.append(y_est)
	ax.plot(x_list, y_list, c="r")
	ax.text(-0.75, 0.6, "Value : %.4f" % z_est)

	x_est, y_est = x_est - fdx(x_est, y_est) * r, y_est - fdy(x_est, y_est) * r
	return ax


ani = animation.FuncAnimation(fig, animate, 30,
	interval=10, blit=False)

plt.show()
