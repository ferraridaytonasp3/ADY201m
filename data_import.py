import pandas as pd
import pyodbc


data = pd.read_csv('https://raw.githubusercontent.com/ferraridaytonasp3/ADY201m/refs/heads/main/FastFoodNutritionMenuV2.csv')

sever = '' #<-- Server's name
datatabase ='FASTFOOD'  


numeric_cols = ['Calories','TotalFat_g','SaturatedFat_g','TransFat_g',
                'Cholesterol_mg','Sodium_mg','Carbs_g','Fiber_g','Sugars_g',
                'Protein_g','WeightWatchers_Points']
def to_number(val):
    try:
        return float(str(val).replace('g','').replace('mg','').replace('Pnts','').strip())
    except:
        return None

for col in numeric_cols:
    data[col] = data[col].apply(to_number)

data = data.dropna(subset=numeric_cols)

lst = []
for driver in pyodbc.drivers:
    lst.append(driver)
print(lst[2])


cnxn = pyodbc.connect('DRIVER='+lst[2]+';SERVER='+sever+';DATABASE='+datatabase+';Trusted_Connection=yes;')


cursor = cnxn.cursor()
insert_query = '''INSERT INTO FastFoodNutrition (Company,Item, Calories, TotalFat_g,SaturatedFat_g,TransFat_g,Cholesterol_mg,Sodium_mg,Carbs_g,Fiber_g,Sugars_g,Protein_g,WeightWatchers_Points)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)  '''


for row in data.itertuples(index=False):
    values = (
        row.Company,
        row.Item,
        float(row.Calories) if pd.notnull(row.Calories) else None,
        float(row.TotalFat_g) if pd.notnull(row.TotalFat_g) else None,
        float(row.SaturatedFat_g) if pd.notnull(row.SaturatedFat_g) else None,
        float(row.TransFat_g) if pd.notnull(row.TransFat_g) else None,
        float(row.Cholesterol_mg) if pd.notnull(row.Cholesterol_mg) else None,
        float(row.Sodium_mg) if pd.notnull(row.Sodium_mg) else None,
        float(row.Carbs_g) if pd.notnull(row.Carbs_g) else None,
        float(row.Fiber_g) if pd.notnull(row.Fiber_g) else None,
        float(row.Sugars_g) if pd.notnull(row.Sugars_g) else None,
        float(row.Protein_g) if pd.notnull(row.Protein_g) else None,
        float(row.WeightWatchers_Points) if pd.notnull(row.WeightWatchers_Points) else None
    )
    cursor.execute(insert_query, values)


cnxn.commit()
cursor.execute ('SELECT * FROM FastFoodNutrition')


for row in cursor:
    print(row)