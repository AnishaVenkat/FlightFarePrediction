# FlightFarePrediction
In this project i have built an end to end application which predicts the flight fare on various dates based on location source and destination

Libraries used:

Matplotlib,Seaborn,Pandas,Sklearn

Based on the features the Airline	Date_of_Journey	Source	Destination	Route	Dep_Time	Arrival_Time	Duration	Total_Stops	Additional_Info	Filght_Price the price of the flight for particular date is predicted.

Firstly various data preprocessing methods have been applied to dataset for better understanding of the features and feature importance techniques is also applied to retain the Importance features alone.

For model building i have applied trial and error methods where ensemble methods like GradientBoosting and RandomForest have given better accuracy than other models.

For furthermore Optimization of models i have used Hyperparameter Tuning which reduced overfitting of models as well.

Below are the results of R2 score for various models:
Linear Regression:61%
Ridge :61%
Lasso:61%
GradientBoosting:79%
RandomForest:71%

App buidling : Basic HTML and CSS is applied for the Front end.

For the backend i have used Flask and Postman for testing end to end application.

![image](https://user-images.githubusercontent.com/26068822/187887838-7e8ff223-f4ad-478f-919b-ef78720bb3d8.png)


