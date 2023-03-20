import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clean_and_process(csv_url):
    dta = pd.read_csv(csv_url)
    
    data = (dta.drop(['Gender', 'Age', 'Class', 'Seat comfort', 'Departure/Arrival time convenient', 'Food and drink',
                 'Online support', 'Ease of Online booking', 'On-board service', 'Leg room service', 'Baggage handling',
                 'Checkin service', 'Cleanliness','Online boarding', 'Gate location', 'Inflight wifi service',
                 'Inflight entertainment'], axis=1)
        .dropna(subset = ['satisfaction','Customer Type','Type of Travel','Flight Distance','Departure Delay in Minutes', 'Arrival Delay in Minutes'])
        .reset_index(drop =True)
            )
    DDoutliers = data['Departure Delay in Minutes'].mean() +(data['Departure Delay in Minutes'].std()*3)
    ADoutliers = data['Arrival Delay in Minutes'].mean() +(data['Arrival Delay in Minutes'].std()*3)
    FDoutliers = data['Flight Distance'].mean() +(data['Flight Distance'].std()*3)
    
    data1 = (data.assign(Total_Delay = (data['Departure Delay in Minutes']+data['Arrival Delay in Minutes']))
         .rename(columns={'Departure Delay in Minutes': 'Departure_Delay', 'Arrival Delay in Minutes' : 'Arrival_Delay',
                         'Customer Type': 'Loyalty', 'Flight Distance' : 'Flight_Distance', 'Type of Travel':'Travel_Type',
                         'satisfaction':'Satisfaction'})
         .loc[lambda x: x['Departure_Delay']<DDoutliers]     # removing the outliers in each row
         .loc[lambda x: x['Arrival_Delay']<ADoutliers]
         .loc[lambda x: x['Flight_Distance']<FDoutliers]
         .sort_values('Total_Delay', ascending=False)         # showing the largest total delay values at the top
         .reset_index(drop=True)
            )
    
    
    return data1