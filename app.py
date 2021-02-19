from flask import Flask, render_template, request
import pickle
import sklearn
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('Flight.pkl' , 'rb'))


@app.route("/" , methods = ["GET" , "POST"])
def main():
    if request.method == "POST":
    #     ['Total_Stops', 'journey_day', 'journey_month', 'dep_hour', 'dep_mins',
    #    'Arrival_hour', 'Arrival_mins', 'duration_hours', 'duration_mins',
    #    'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
    #    'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
    #    'Vistara', 'Vistara Premium economy', 'Source_Chennai', 'Source_Delhi',
    #    'Source_Kolkata', 'Source_Mumbai', 'destination_Cochin',
    #    'destination_Delhi', 'destination_Hyderabad', 'destination_Kolkata',
    #    'destination_New Delhi']
        # Date_of_Journey
        date_dep = request.form["Departure_time"]
        datetime_dep = pd.to_datetime(date_dep, format="%Y-%m-%d %H:%M")
        journey_day = int(datetime_dep.day)
        journey_month = int(datetime_dep.month)

        # Departure
        dep_hour = int(datetime_dep.hour)
        dep_mins = int(datetime_dep.minute)

        # Arrival
        date_arr = request.form["Arr_time"]
        datetime_arr = pd.to_datetime(date_arr, format ="%Y-%m-%d %H:%M")
        Arrival_hour = int(datetime_arr.hour)
        Arrival_mins = int(datetime_arr.minute)

        if datetime_arr < datetime_dep:
            return render_template('index.html' , prediction = "Date and Time are wrong")


        sec =  (datetime_arr - datetime_dep).seconds
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        # Duration
        duration_hours = h
        duration_mins = m

        # Total Stops
        Total_Stops = int(request.form["stops"])

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
        elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        # ['Total_Stops', 'journey_day', 'journey_month', 'dep_hour', 'dep_mins',
    #    'Arrival_hour', 'Arrival_mins', 'duration_hours', 'duration_mins',
    #    'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
    #    'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
    #    'Vistara', 'Vistara Premium economy', 'Source_Chennai', 'Source_Delhi',
    #    'Source_Kolkata', 'Source_Mumbai', 'destination_Cochin',
    #    'destination_Delhi', 'destination_Hyderabad', 'destination_Kolkata',
    #    'destination_New Delhi']
        prediction = model.predict([[
            Total_Stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_mins,
            Arrival_hour,
            Arrival_mins,
            duration_hours,
            duration_mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output=round(prediction[0],2)
#         print("dur hours: ",duration_hours,"dur mins: ",duration_mins)


        return render_template('index.html' , prediction = "Fare is Rs. {}".format(output))


    return render_template('index.html', prediction = '' )

if __name__ == "__main__":
    app.run(debug = True)
