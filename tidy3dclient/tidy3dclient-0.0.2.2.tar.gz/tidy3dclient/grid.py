import numpy as np

from .structure import Structure
from .constants import fp_eps, int_, float_, C_0

class Grid(object):
    
    def __init__(self, span, res, symmetries=[0, 0, 0], courant=0.9, init_mesh=True):
        """
        Parameters
        ----------
        span : np.ndarray of shape (3, 2)
            Defines (xmin, xmax), (ymin, ymax), (zmin, zmax) of the simulation
            region, in micron.
        res : float or array of floats
            Resolution in x, y, and z, in micron.        
        """

        # Setting span also sets self.mesh, self.mesh_b, self.mesh_f
        self.span = np.array(span).astype(float_)
        self.size = self.span[:, 1] - self.span[:, 0]
        self.res = np.array(res).astype(float_)
        self.symmetries = symmetries

        self.tmesh = None # To be set when a total simulation time is given
        self.set_time_step(courant)

        def empty_mesh():
            return [np.array([]), np.array([]), np.array([])]

        # Grid size
        self.Nx, self.Ny, self.Nz, self.Nxyz = 0, 0, 0, (0, 0, 0)
        # Backward, centered, and forward meshes
        self.mesh_b, self.mesh, self.mesh_f = [empty_mesh() for i in range(3)]
        # Ex, Ey, and Ez meshes
        self.mesh_x, self.mesh_y, self.mesh_z = \
                                        [empty_mesh() for i in range(3)]
        if init_mesh==True:
            self.init_meshes()
            
    @property
    def res(self):
        """ Returns the (dx, dy, dz) resolution of the grid """
        return self._res

    @res.setter
    def res(self, new_res):
        restmp = np.array(new_res)
        if restmp.size==1:
            self._res = restmp*np.ones((3, ), dtype=float_)
        elif restmp.size==3:
            self._res = restmp
        else:
            raise ValueError("resolution must be a float or an array of 3 "
                                "floats.")

    def init_meshes(self):
        """ Initialize centered, forward, and backward mesh based on span and 
        res. Also initialize the meshes corresponding to the E- and H-field 
        locations on the Yee grid.
        """

        # Slightly increase span to assure pixels at the edges are included. 
        _span = self.span
        _span[:, 0] -= fp_eps*self.size
        _span[:, 1] += fp_eps*self.size

        # Initialize mesh points in x, y and z 
        self.Nxyz = [int_((_span[0][1]-_span[0][0])/self.res[0]),
                    int_((_span[1][1]-_span[1][0])/self.res[1]),
                    int_((_span[2][1]-_span[2][0])/self.res[2])]

        # Always take an even number of points if symmetry required
        for dim in range(3):
            if self.symmetries[dim]!=0 and self.Nxyz[dim]%2==1:
                self.Nxyz[dim]+=1
        self.Nx, self.Ny, self.Nz = self.Nxyz
        
        xcent = (_span[0][1] + _span[0][0])/2
        ycent = (_span[1][1] + _span[1][0])/2
        zcent = (_span[2][1] + _span[2][0])/2

        # Make simulation center coincide with beginning of Yee cell
        xgrid = xcent + self.res[0]*np.arange(-((self.Nx+1)//2), (self.Nx)//2)
        ygrid = ycent + self.res[1]*np.arange(-((self.Ny+1)//2), (self.Ny)//2)
        zgrid = zcent + self.res[2]*np.arange(-((self.Nz+1)//2), (self.Nz)//2)

        for dim, grid in enumerate([xgrid, ygrid, zgrid]):
            # Coordinates of the starting points of the mesh elements
            self.mesh_b[dim] = np.copy(grid).astype(float_)
            # Coordinates of the mesh centers 
            self.mesh[dim] = self.mesh_b[dim] + self.res[dim]/2
            # Coordinates of the ending points of the mesh elements
            self.mesh_f[dim] = self.mesh_b[dim] + self.res[dim]

        self.yee_meshes()

    def load_mesh(self, mesh):
        """ Load an externally-defined mesh.
        """
        for dim in range(3):
            self.mesh_b[dim] = mesh[dim] - self.res[dim]/2
            self.mesh[dim] = mesh[dim]
            self.mesh_f[dim] = mesh[dim] + self.res[dim]/2

        self.Nxyz = [m.size for m in mesh]
        self.Nx, self.Ny, self.Nz = self.Nxyz
        self.yee_meshes()

    def yee_meshes(self):
        # Meshes for the Ex, Ey, and Ez locations.
        self.mesh_ex = (self.mesh[0], self.mesh_b[1], self.mesh_b[2])
        self.mesh_ey = (self.mesh_b[0], self.mesh[1], self.mesh_b[2])
        self.mesh_ez = (self.mesh_b[0], self.mesh_b[1], self.mesh[2])
        self.mesh_hx = (self.mesh_b[0], self.mesh[1], self.mesh[2])
        self.mesh_hy = (self.mesh[0], self.mesh_b[1], self.mesh[2])
        self.mesh_hz = (self.mesh[0], self.mesh[1], self.mesh_b[2])

    def set_time_step(self, stability_factor=0.9):
        """ Set the time step based on the generalized Courant stability
                Delta T < 1 / C_0 / sqrt(1 / dx^2 + 1/dy^2 + 1/dz^2)
                dt = courant_condition * stability_factor, so stability factor 
                should be < 1.
        """

        dL_sum = np.sum([1/self.res[ir]**2 for ir in range(3)])
        dL_avg = 1 / np.sqrt(dL_sum)
        courant_stability = dL_avg / C_0
        self.dt = float_(courant_stability * stability_factor)

    def set_tmesh(self, T=0):
        """ Set the time mesh for a total simulation time T in seconds.
        """
        self.tmesh = np.arange(0, T, self.dt)