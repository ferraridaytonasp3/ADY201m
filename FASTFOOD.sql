CREATE DATABASE FASTFOOD

USE FASTFOOD
CREATE TABLE FastFoodNutrition (
    Company NVARCHAR(100),
    Item NVARCHAR(255),
    Calories INT,
    TotalFat_g INT,
    SaturatedFat_g FLOAT,
    TransFat_g FLOAT,
    Cholesterol_mg INT,
    Sodium_mg INT,
    Carbs_g INT,
    Fiber_g INT,
    Sugars_g INT,
    Protein_g INT,
    WeightWatchers_Points FLOAT
);

select * from FastFoodNutrition

SELECT Company, Item,Calories
FROM FastFoodNutrition AS F1
WHere Calories = (SELECT MAX(Calories) 
					FROM FastFoodNutrition AS F2 
					WHERE F1.Company = F2.Company)

-- SKIBIDI DOP DOP YES YES --


SELECT Company, AVG(CAST((Protein_g*1.0)/ Calories AS decimal(18,4))) AS SKibididopdop
FROM FastFoodNutrition 
Where Calories > 0 
Group by Company


-- Cau 10 
SELECT TOP 5 
    Company,
    Item,
    Protein_g,
    Calories,
    CAST(Protein_g * 1.0 / Calories AS DECIMAL(10, 4)) AS ProteinPerCalorie
FROM FastFoodNutrition
WHERE Calories > 0
ORDER BY ProteinPerCalorie DESC;


