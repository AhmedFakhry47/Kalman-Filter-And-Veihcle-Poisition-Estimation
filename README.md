# Kalman-Filter-And-Veihcle-Poisition-Estimation

The Kalman Filter is the optimal linear estimate for linear system models with additive independent white noise in both<br/>
the transition and the measurement systems<br/>

 
The code is meant to Test the kalman filter in the following scenario : <br/>
-A veihcle moves on straight rails and it's initially stationary at position zero <br/>
-There are two state variables ( Position x , Velocity x ) and this simplification is for having a linear system <br/>

# Dependencies
-Numpy <br/>
-Matplot Library <br/> 

# Project
Project is divided into two files: <br/>
1-Kalman Filter Code <br/>
2-Test code  <br/>

Test Code is meant to do three main things : <br/>
1-Generat GroundTruth Data for the above scenario <br/>
2-Test Kalman Filter ( Determine estimated values of position by Kalman Filter) <br/>
3-Determine RMSE between estimated states and ground truth values <br/>

# Plot
# GroundTruth Data Vs Sensor Measurements
![SensorsVsGT-DATA](https://user-images.githubusercontent.com/44531149/69463045-579ceb80-0d83-11ea-846f-5651b2f89622.png)

# Estimated positions by Kalman filter Vs Ground Truth positions at each discrete time step
![EstimatedStatesVsGT-](https://user-images.githubusercontent.com/44531149/69463046-58358200-0d83-11ea-814f-0996c0dde87b.png)
