# disaster_alert_system



****Problem Statement
Design a security and aid system that utilizes technology to enhance the safety and well-being of individuals living in disaster-prone areas. The system should include features such as real-time monitoring and alerts for potential hazards, a means for individuals to quickly and easily request aid, and secure communication channels for emergency responders and aid workers. The system should also be designed to be easily deployable in emergency situations and be able to function in low-connectivity areas.


**Tech Used:-**
1.Machine learning for training model.
2.Flask used for deploying the machine learning model.
3.Web Development used for designing and developing the site.

**Setup**
1. Setup Flask 
2. Also set virtual environment on your local computer.
The project can be deployed at flask server by using the command run flask

**Approach used by us:-**
In order to enhance the safety and well being of individuals living in disaster prone areas, we have decided to deploy three machine learning models which will help in predicting the occurrences of three natural disasters i.e. earthquake, hailstorm and flood.
After predicting the occurrences, alert will be send through sms to all the individuals if there is risk in any case of natural disaster.

**Earthquake Prediction**
 The dataset for the earthquake prediction is taken from kaggle. In this we have used the linear regression model.
 There are four attributes used in this dataset:-
 1.Date
 2.Longitude
 3.Latitude
 4.Depth
 
 Taking these attributes as input values from the user we get the prediction as safe or risky on the basis of magnitude value received as output from the user input values.
 
 The Root Mean Square Error (RMSE) we get in this is 0.68
 
 **Flood Prediction**
 The dataset for the earthquake prediction is taken from kaggle. In this we have used the Decision Tree Classifier.
 There are four attributes used in this dataset:-
 1.Jan
 2.Feb
 3.Mar
 4.Apr
 5.May
 6.June
 7.July
 8.August
 9.September
 10.October
 11.November
 12.December
 13.Annual Rainfall
 
 Taking these attributes as input values from the user we get the prediction as safe or risky on the basis of yees or no received as output from the user input values.
 
 **Hailstorm Prediction**
 The dataset for the earthquake prediction is taken from kaggle. In this we have used the linear regression model.
 There are four attributes used in this dataset:-
 1.LON
 2.LAT
 3.RANGE
 4.AZIMUTH
 
 Taking these attributes as input values from the user we get the prediction as safe or risky on the basis of probability value received as output from the user input values.
 
 
 **Future Scope**
 In future we can strengthen our model by :-
 1.Sending Alert SMS to individuals residing in disaster prone areas.
 2.Creating an emergency responder in the same SMS via link so that people can get immediate help.
 



