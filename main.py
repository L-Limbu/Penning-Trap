import numpy as np

'''Defining the constants and initial Conditions'''
#Constants
AM = 55
u = 1.6605390666e-27   
mass = AM * u
e = 1.6e-19
q_m = e/mass
#Initial Conditions
Electric_field_strength = 500000
B_field_strength =1
#positions and velocity vector
ini_conditions = np.array([1e-3,1e-3,1e-3,100,0,0]) 

def rk4(v_a, x0,dt): 
    ''' 4th order Runge Kutta method used to find the following positions and velocities'''
    tn = 0
    xn = x0
    while True:
        yield tn, xn
        k1 = v_a(tn, xn)
        k2 = v_a(tn + dt/2, xn + k1*dt/2)
        k3 = v_a(tn + dt/2, xn + k2*dt/2)
        k4 = v_a(tn + dt, xn + k3*dt)
        xn = xn + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt
        tn = tn + dt



def accn(position_velocity):   
    '''Function to find acceleration of ions with the provided initial conditions.
    DC electric field is applied along with magnetic field in z direction.'''
    
    x_position = position_velocity[0]
    y_position = position_velocity[1] 
    z_position = position_velocity[2]     

    #For penning traps, the electric vector is (x, y, -2z) by definition.
    E_vector = Electric_field_strength * np.array([x_position, y_position, -2*z_position])   
   
  

    B_vector = B_field_strength * np.array([0,0,1])      
                                                                    
    velocity_vector = position_velocity[3:6]
    acceleration_vector = q_m*(E_vector * 0.5 * 1/1e1**2 + np.cross(velocity_vector, B_vector))                              
    return acceleration_vector

def v_a(t, position_velocity):               
    ''' An empty array is created to append velocities and acceleration of the ion
    from array with position and velocity'''
    
    velocity_acceleration = np.zeros(6)                                                
    velocity_acceleration[0:3] = position_velocity[3:6]                                                
    velocity_acceleration[3:6] += accn(position_velocity)                                             
    return velocity_acceleration

def run():
    ''' Running the simulation with Runge Kutta method and the positions 
    measured in milimeters of the moving ion is stored in positions_vector.'''
    
    sim = rk4(v_a, ini_conditions, dt=10e-9)                                          
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for iterations in range(500000):
        t, position_velocity  = next(sim)

        x = np.append(x, position_velocity[0])
        y = np.append(y, position_velocity[1])
        z = np.append(z, position_velocity[2])   
        
    positions = np.array([x,y,z])*1e3
    return np.save('./data/positions', positions)


run()