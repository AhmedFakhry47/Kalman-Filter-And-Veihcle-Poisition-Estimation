import numpy as np
'''
    Kalman filter
    X denotes vector for state variables
    F state transition model    --Fixed
    H observation transition model  --Fixed
    Q denotes process noise covarience  --Fixed
    R denotes measurement noise covarience --Fixed
    P denotes error covarience matrix ( a measure for accuracy of state estimate )
    Z denotes measurement matrix
'''
class KalmanFilter  :

    def __init__ (self,meta):
        #The four fixed matrices
        self.F = meta['F']
        n = self.F.shape[1]
        self.H = meta['H']
        m = self.H.shape[1]
        self.Q = meta['Q']
        self.R = meta['R']

        #Initialization of remaining matrices
        self.X = np.array([0.0 , 2.0]).reshape(n,1) if ('X' not in list(meta.keys())) else meta['X']
        self.P = np.eye(n) if ('P' not in list(meta.keys())) else  meta['P']
        self.Z = np.zeros(m).reshape(m,1)
        self.Y = np.zeros(m).reshape(m,1)
        self.K = 0 #Kalman Gain

    def predict(self,dt):
        self.F[0][1]=dt
        self.X = np.dot(self.F , self.X)
        self.P = np.dot(np.dot(self.F,self.P),self.F.T) + self.Q

    def update(self,measurements):
        self.Z=measurements
        self.Y = self.Z - np.dot(self.H , self.X)

        S = np.dot(np.dot(self.H , self.P) ,self.H.T) + self.R
        self.K =np.dot(np.dot(self.P ,self.H.T),np.linalg.inv(S))
        
        #Update X and P
        self.X = self.X + self.K*self.Y
        self.P = self.P - np.dot(np.dot(self.K , self.H),self.P)

    def eval(self,measurements,dt):
        self.predict(dt)
        self.update(measurements)
        return self.X
