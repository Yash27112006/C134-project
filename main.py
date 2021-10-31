import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('star_with_gravity.csv')

temp_distance=[]
for distance in df.Distance:
  if distance <= 100:
    temp_distance.append(True)
  else:
    temp_distance.append(False) 


filtered_distance=pd.Series(temp_distance)
star_with_filtered_distance=df[filtered_distance]


star_with_filtered_distance.reset_index(inplace=True,drop=True)
star_with_filtered_distance.shape


temp_gravity=[]
for gravity in star_with_filtered_distance.Gravity:

  if gravity>=150 and gravity<=350:
    temp_gravity.append(True)
  else:
    temp_gravity.append(False)

filtered_gravity=pd.Series(temp_gravity)
final_stars_list=star_with_filtered_distance[filtered_gravity]
final_stars_list.shape
final_stars_list.reset_index(inplace=True,drop=True)
final_stars_list.to_csv("filtered_data.csv")