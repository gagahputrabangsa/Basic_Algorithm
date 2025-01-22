import pandas as pd #we're using pandas lib for sorting

data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 20]}) #this is example df
sorted_data = data.sort_values('Age')  # sorting df based on their age
print(sorted_data)
