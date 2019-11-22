# Kalman-Filter-And-Veihcle-Poisition-Estimation
Testing the kalman filter with a very simple example which is : <br/>
-A veihcle that is moving on straight rails, it's initially stationary at position zero <br/>
-There are two state variables ( Position x , Velocity x ) and this simplification is for having a linear system <br/>

# Dependencies
-Numpy <br/>
-Matplot Library <br/> 

Project is divided into two files: <br/>
1-Kalman Filter Code <br/>
2-Test code  <br/>

Test Code is meant to do three main things : <br/>
1-Generat GroundTruth Data for the above scenario <br/>
2-Test Kalman Filter ( Determine estimated values of position by Kalman Filter) <br/>
3-Determine RMSE between estimated states and ground truth values <br/>

# Plot
## GroundTruth Data Vs Sensor Measurements
![SensorsVsGT-DATA](https://user-images.githubusercontent.com/44531149/69463045-579ceb80-0d83-11ea-846f-5651b2f89622.png)

## Estimated positions by Kalman filter Vs Ground Truth positions at each discrete time step
![EstimatedStatesVsGT-](https://user-images.githubusercontent.com/44531149/69463046-58358200-0d83-11ea-814f-0996c0dde87b.png)
