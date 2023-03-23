import pandas as pd
import numpy as np

def load_and_process(file_path="../../data/raw/Invistico_Airline.csv"):
    df1 = (pd.read_csv(file_path)
           .dropna(subset=['Age', 'satisfaction',
                           'Ease of Online booking', 'Online boarding', 'Online support', 'Type of Travel'])
           .drop(['Gender', 'Customer Type', 'Class', 'Flight Distance', 'Seat comfort',
                  'Departure/Arrival time convenient', 'Food and drink','On-board service',
                  'Leg room service', 'Baggage handling', 'Checkin service', 'Cleanliness',
                  'Gate location', 'Inflight wifi service', 'Inflight entertainment', 
                  'Departure Delay in Minutes', 'Arrival Delay in Minutes'], axis=1))
    df2 = (df1.assign(Age=pd.cut(df1['Age'], bins=[0, 19, 29, 39, 49, 59, 69, 100], 
                          labels=['<19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']))
       [['Age', 'Type of Travel', 'satisfaction', 
         'Ease of Online booking', 'Online boarding', 'Online support']]
       .dropna().reset_index(drop=True))
    return df2