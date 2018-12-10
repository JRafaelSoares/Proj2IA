import numpy as np
import RL as RL

r = 200
for i in range(25, 500, 25):

	avg_Q = 0

	for j in range(r):
		J, traj = fmdp.runPolicy(i, 3, poltype = "exploration")
		Qr = fmdp.traces2Q(traj)

		if np.sqrt(sum(sum((data['Q1'] - Qr)**2))) < 1:
		    avg_Q += 1

	print(str(i) + ";" + str(avg_Q/r) + ";")