Here is the part of Sensor Data simulation. The purpose is to simulate people's movement in a day. In this part, 30 days of data are simulated. And through different time series analysis models to predict, on this basis, expand to 180 days of data, and then use Prophet pakage to train the model.

GeneOneDay.py:
The simulation generates data for each day's activities.

segmentProb.py:
Calculate the probability of people exercising over a period of time.

reSampleConstruct.py:
Construct data of different lengths on the basis of certain data.