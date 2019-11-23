import numpy as np
from kalmanfiler import KalmanFilter
import matplotlib.pyplot as plt

'''
Testing the kalman filter with a very simple example which is :
-A veihcle that is moving on straight rails, it's initially stationary at position zero
-The veihcle is accelerated with a zero mean acceleration and (sigma a standard deviation) (ak)
-There are two state variables ( Position x , Velocity x ) and this simplification is for having a linear system
'''
def generate_data():
    num_states = 2

    px_start =0.0
    vx_start =2.0

    pi = np.pi

    #define time interval ( timestep )
    base_time = 1477010443000000
    delta_t_us = .5*1e5
    delta_t_sec = delta_t_us/1e6
    round_time_sec = 25

    num_measurements = int(round_time_sec /delta_t_sec)

    #Ground Truth Matrices Initialization
    GT = np.zeros((num_states+1,num_measurements),dtype = np.double)

    GT[0][0] = px_start
    GT[1][0] = vx_start
    GT[2][0] = base_time

    #Sensor Data Matrices Initialization
    sens_meas = np.zeros((num_states+1,num_measurements),dtype = np.double) #Zero mean
    snoise_stdv =.15 #Sensor noise stdev for position and velocity

    sens_meas[0][0]= GT[0][0] + np.random.normal(0,snoise_stdv,size=None)
    sens_meas[1][0]= GT[1][0] + np.random.normal(0,snoise_stdv,size=None)
    sens_meas[2][0]= GT[2][0]

    #Generate Ground Truth Data and sensor measurements
    for count in range(1,num_measurements):
        GT[1][count] =2.0

        #Update time
        current_time = base_time+(count*delta_t_us)
        GT[2][count] = current_time
        sens_meas[2][count]= current_time

        #Ground Truth updated position
        current_delta_t = (count*delta_t_us)/1e6
        GT[0][count] = GT[0][count]+(GT[1][count] * current_delta_t) #Transition function which is about previous value plus delta time * constant velocity

        #Sensor measured position and velocity
        sens_meas[0][count] = GT[0][count]+np.random.normal(0,snoise_stdv,size=None)
        sens_meas[1][count] = GT[1][count]+np.random.normal(0,snoise_stdv,size=None)


    plt.plot(range(len(sens_meas[0][:])),sens_meas[0][:],label='Meas')
    plt.plot(range(len(GT[0][:])),GT[0][:],label='GT')
    plt.legend()
    plt.show()

    return GT,sens_meas

def RMSE(lst1,lst2):
    if len(lst1) != len(lst2):
        print("Length of two lists must be equal")
        return

    length = len(lst1)
    sum=0.0
    for i,(x,y) in enumerate(zip(lst1,lst2)):
        sum+= (x-y)
        sum = sum **2

    return np.sqrt(sum/length)

def test(GT,sens_meas):
    meta = dict()
    dt = .5*1e5/1e6
    meta['F']  = np.array([[1, dt],[0,1]],dtype = np.double)
    meta['H']  = np.array([1 , 0]).reshape(1,2)
    meta['Q']  = np.array([[0.5 , 0.0],[0.0,0.5]]) #It's set with random value
    meta['R']  = np.array([0.15]).reshape(1,1) #Sensor measurement noise covarience
    meta['X']  = np.array([0.0,2.0]).reshape(2,1)

    filter = KalmanFilter(meta)
    estimated_states = []

    for i,dtime in enumerate(sens_meas[2][:]):
        measurements = np.array([[sens_meas[0][i]],[sens_meas[1][i]]]) #This part is a little bit hardcoded
        dt=i*dt
        estimated_states.append(filter.eval(measurements,dt))

    estimated_states = np.array(estimated_states).T.reshape(GT.shape[0]-1,GT.shape[1])

    plt.plot(GT[2][0:100],GT[0][0:100],'.-r',label='GroundTruth',linestyle='dashed')
    plt.plot(GT[2][0:100],estimated_states[0][0:100],'.-b',label='Estimated_states')
    plt.legend()
    plt.show()

    #Print RMSE value of kalman filter state estimations
    print('RMSE value when using kalman filter : ',RMSE(GT[0][:],estimated_states[0][:]))
    print('RMSE value wihtout kalman filter : ',RMSE(GT[0][:],sens_meas[0][:]))
if __name__ == "__main__":
    GT,Z= generate_data()
    test(GT,Z)
