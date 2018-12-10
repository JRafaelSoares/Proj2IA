from numpy import load

data = load('traj2.npz')
lst = data.files
for item in lst:
    print(item)

    print(data[item])
    
    for i in range(0, len(data[item])):
    	if(data[item][i][0] == 3 and data[item][i][1] == 3):
    		print(data[item][i])
    