import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://raw.githubusercontent.com/ferraridaytonasp3/ADY201m/refs/heads/main/FastFoodNutritionMenuV2.csv")


numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns


X = df[numeric_cols].drop(columns=['Protein_g'])
y = df['Protein_g']


model = LinearRegression()
model.fit(X, y)

print("\nNhập thông tin món ăn để dự đoán Protein_g:")
Calories = float(input("Calories: "))
TotalFat_g = float(input("TotalFat_g: "))
SaturatedFat_g = float(input("SaturatedFat_g: "))
TransFat_g = float(input("TransFat_g: "))
Cholesterol_mg = float(input("Cholesterol_mg: "))
Sodium_mg = float(input("Sodium_mg: "))
Carbs_g = float(input("Carbs_g: "))
Fiber_g = float(input("Fiber_g: "))
Sugars_g = float(input("Sugars_g: "))
WeightWatchers_Points = float(input("WeightWatchers_Points: "))

sample_data = pd.DataFrame([{
    'Calories': Calories,
    'TotalFat_g': TotalFat_g,
    'SaturatedFat_g': SaturatedFat_g,
    'TransFat_g': TransFat_g,
    'Cholesterol_mg': Cholesterol_mg,
    'Sodium_mg': Sodium_mg,
    'Carbs_g': Carbs_g,
    'Fiber_g': Fiber_g,
    'Sugars_g': Sugars_g,
    'WeightWatchers_Points': WeightWatchers_Points
}])

predicted_protein = model.predict(sample_data)[0]
print(f"\nDự đoán Protein_g cho món mẫu: {predicted_protein:.2f} ")