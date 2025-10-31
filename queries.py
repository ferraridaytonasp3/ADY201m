import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ferraridaytonasp3/ADY201m/refs/heads/main/FastFoodNutritionMenuV2.csv')

req1 = data.groupby('Company')['Calories'].mean()
# print(req1)

req2 = data.groupby(['Company'])[['Calories','Item']].max()
# print(req2)

req3= data[['Calories','TotalFat_g']].corr()  
# print(req3)

req4 = data.groupby('Company')['SaturatedFat_g'].mean()
# print(req4)

req5= data[['Item','Sodium_mg']].sort_values(by='Sodium_mg', ascending=False).head(10)
# print(req5)

req6= data.groupby('WeightWatchers_Points')['Calories'].mean()
# print(req6)

req7semi = data.query('Calories > 0')
req7semi['ProteinPerCalo'] = req7semi['Protein_g'] / req7semi['Calories']
req7 = req7semi.groupby('Company')['ProteinPerCalo'].mean()
# print(req7)

req8 = data.groupby("Item")["Calories"].agg(["count", "mean", "min", "max", "std"])
# print(req8)

req9 =data[['Sugars_g','Calories']].corr()
# print(req9)

req10a = data.sort_values(['Protein_g','Calories'],ascending= [False,True]).head(5)
# print(req10a)

req10b_semi = data.query('Calories > 0')
req10b_semi['ProteinPerCalo'] = req10b_semi['Protein_g'] / req10b_semi['Calories']
req10b = req10b_semi.groupby(['Item','Calories','Protein_g'])['ProteinPerCalo'].mean().sort_values(ascending=False).head(5)
# print(req10b) 

