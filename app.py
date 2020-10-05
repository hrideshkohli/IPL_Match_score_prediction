from flask import Flask, request, render_template
import pickle
import numpy as np

filename='ipl_score_predictor.pkl'
reg_linear=pickle.load(open(filename, 'rb'))

app=Flask(__name__)



@app.route('/')

def root():
    
    return render_template('index.html')
    
    
@app.route('/predict',methods=['GET','POST'])    

def predict():
    temp_array=list()
    if request.method == 'POST':
        batting_team=request.form['Batting-team']
        if batting_team == "Mumbai Indians":
            temp_array=temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == "Kolkata Knight Riders":  
            temp_array=temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team =="Chennai Super Kings":
            temp_array=temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team =="Rajasthan Royals":   
            temp_array=temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team =="Kings XI Punjab":   
            temp_array=temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team =="Royal Challengers Bangalore":   
            temp_array=temp_array + [0, 0, 0, 0, 0, 1, 0, 0] 
        elif batting_team =="Delhi Daredevils":   
            temp_array=temp_array + [0, 0, 0, 0, 0, 0, 1, 0]     
        elif batting_team =="Sunrisers Hyderabad":   
            temp_array=temp_array + [0, 0, 0, 0, 0, 0, 0, 1]   
            
        bowling_team=request.form['Bowling-team']
        if bowling_team == "Mumbai Indians":
            temp_array=temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == "Kolkata Knight Riders":  
            temp_array=temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team =="Chennai Super Kings":
            temp_array=temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team =="Rajasthan Royals":   
            temp_array=temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team =="Kings XI Punjab":   
            temp_array=temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team =="Royal Challengers Bangalore":   
            temp_array=temp_array + [0, 0, 0, 0, 0, 1, 0, 0] 
        elif bowling_team =="Delhi Daredevils":   
            temp_array=temp_array + [0, 0, 0, 0, 0, 0, 1, 0]     
        elif bowling_team =="Sunrisers Hyderabad":   
            temp_array=temp_array + [0, 0, 0, 0, 0, 0, 0, 1]
            
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_5'])
        wickets_in_prev_5 = int(request.form['wickets_5'])    
        mean_venue_score=165
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5, mean_venue_score]
        
        data = np.array([temp_array])
        my_prediction = int(reg_linear.predict(data)[0])
        lower_value=my_prediction-10
        upper_value=my_prediction+5
        return render_template('index.html',results= "The Predict scores range between {} to {} ".format(lower_value, upper_value))
        
    else:
        return render_template('index.html')
    
    
if __name__=='__main__':
    app.run()