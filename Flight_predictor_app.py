from flask import Flask,request,render_template

import pandas as pd

import pickle

pickle_in = open("Gradient_boosting.pkl", 'rb')
model = pickle.load(pickle_in)

app=Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route("/flight_pred",methods=['POST'])

def flight_pred():

    if request.method == 'POST':
        Dep_Time = request.form['Dep_Time']

        journey_date=int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").day)
        journey_month=int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").month)


        dep_hour=int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").hour)
        dep_min=int(pd.to_datetime(Dep_Time,format="%Y-%m-%dT%H:%M").minute)


        Arrival_Time = request.form['Arrival_Time']
        arrival_hour=int(pd.to_datetime(Arrival_Time,format="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(Arrival_Time,format="%Y-%m-%dT%H:%M").minute)


        dur_hour=abs(arrival_hour-dep_hour)
        dur_min=abs(arrival_min-dep_min)


        airline = request.form['airline']
        airline_list=["Airline_Air Asia" ,"Airline_Air India" ,"Airline_GoAir","Airline_IndiGo","Airline_Jet Airways","Airline_Jet Airways Business","Airline_Multiple carriers","Airline_Multiple carriers Premium economy","Airline_SpiceJet","Airline_Trujet","Airline_Vistara","Airline_Vistara Premium economy"]
        air_val=[]
        for i in airline_list:
            if i == airline:
                val=1
                air_val.append(val)
            if i!=airline:
                val=0
                air_val.append(val)

        airline_df = pd.DataFrame(air_val, index=airline_list).T

        Source = request.form['Source']
        source_list = ["Banglore","Chennai","Delhi","Kolkata","Mumbai"]
        source_val = []
        for j in source_list:
            if j == Source:
                val = 1
                source_val.append(val)
            if j != Source:
                val = 0
                source_val.append(val)

        source_df = pd.DataFrame(source_val, index=source_list).T


        Destination = request.form['Destination']

        destination_list = ["Banglore", "Cochin", "Delhi", "Hyderabad", "Kolkata","New Delhi"]
        dest_val = []
        for k in destination_list:
            if k == Destination:
                val = 1
                dest_val.append(val)
            if k != Destination:
                val = 0
                dest_val.append(val)

        dest_df = pd.DataFrame(dest_val, index=destination_list).T



        Stopage = int(request.form['stops'])

        data_list = [Stopage,arrival_hour,arrival_min,dep_hour,dep_min,journey_date,journey_month,dur_hour,dur_min]
        data = pd.DataFrame(data_list, index=["Stopage","arrival_hour","arrival_min","dep_hour","dep_min","journey_date","journey_month","dur_hour","dur_min"]).T

        df = pd.concat([data, airline_df, source_df,dest_df], axis=1)


        prediction = model.predict(df)
        print(prediction)
        output = round(prediction[0], 2)

        if output < 0:
            return render_template('home.html', prediction_text="Input invalid")
        else:
            return render_template('home.html', prediction_text="The Flight price is: {}".format(output))

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run()