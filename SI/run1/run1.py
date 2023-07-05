import pencil_old as pc
import numpy as np
import matplotlib.pylab as plt

#read time series (average data over full box, function of time) 
'''
data=pc.read_ts()

#plot time series data; data.t divided by 2pi; uxm=mean velocity?
#use oz2m average of square of the vorticity (omega z^2)
plt.plot(data.t/(2*np.pi), data.oz2m)
plt.yscale('log')
plt.xlabel(r'P:$(2\pi/\Omega)$',fontsize=16)
plt.ylabel(r'$\langle \Omega_z^2\rangle$',fontsize=16)
plt.title('Time Series Data')
plt.tight_layout()
plt.show()
'''


#read var file (downloads data from particular var file from all processors; more detailed than time series; data at each grid point at particular time stamp)
#trimall means ...
#ivar=0 for initial conditions

ff=pc.read_var(trimall=True) # magic=['vort'])
#print(ff.vort.shape)
'''
#vorticity
plt.contourf(ff.x, ff.z, ff.vort) # np.transpose(ff.vort[2,0,...]), np.linspace(-1,1,256))
plt.axes().set_aspect('equal')
plt.colorbar()
plt.title("Vorticity")
plt.show()

#ss entropy
plt.contourf(ff.y, ff.x, np.transpose(ff.ss), 256)
plt.axes().set_aspect('equal')
plt.colorbar()
plt.title("Entropy")
plt.show()
'''
'''
fig, axs = plt.subplots(2,2)
#density
axs[0,0].contourf(ff.x, ff.z, ff.rho, 256)
#axs[0,0].axes().set_aspect('equal')
#axs[0,0].colorbar()
axs[0,0].set_title("Density")

#mean density
rho_avg = np.mean(ff.rho, axis=0)
axs[0,1].plot(ff.x, rho_avg)
axs[0,1].set_title("Mean Density")


#velocity uu
axs[1,0].contourf(ff.x, ff.z, ff.uu[0,...], 256)
#plt.axes().set_aspect('equal')
#plt.colorbar()
axs[1,0].set_title("Velocity")


plt.tight_layout()
plt.show()
'''

#velocity uu
plt.contourf(ff.x, ff.z, ff.uy, 256)
plt.colorbar()
plt.tight_layout()
plt.show()

