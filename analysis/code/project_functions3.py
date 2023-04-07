import pandas as pd
import numpy as np

def load_and_process(file_path="../../data/raw/Invistico_Airline.csv"):
    df2 = (pd.read_csv("../data/raw/Invistico_Airline.csv")
       .dropna(subset=['Age', 'satisfaction','Seat comfort','Leg room service', 'On-board service'])
       .drop(['Gender','Customer Type','Class','Flight Distance',
              'Departure/Arrival time convenient', 'Food and drink','Baggage handling','Checkin service','Cleanliness',
              'Gate location','Inflight wifi service','Inflight entertainment',
              'Departure Delay in Minutes','Ease of Online booking','Online boarding','Online support','Type of Travel','Arrival Delay in Minutes'], axis=1))
    df2 = (df2
       .assign(Age=pd.cut(df2['Age'], bins=[0, 19, 29, 39, 49, 59, 69, 100], 
                          labels=['<19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']))
       [['Age', 'satisfaction','Seat comfort','Leg room service', 'On-board service']]
       .dropna().reset_index(drop=True))
    df2['Avg_Rating']= (df2['On-board service'] + df2['Seat comfort'] + df2['Leg room service']) / 3
    return df2