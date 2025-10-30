use FASTFOOD
--req1
select Company, avg(Calories) as AvgCalo
from FastFoodNutrition
group by Company
--req2
select Company, Item, Calories
from (select Company, Item, Calories, ROW_NUMBER() over (partition by Company order by Calories desc) rn
		from FastFoodNutrition) t
where rn <= 1
--req4
select Company, avg(SaturatedFat_g) as AvgSaturated
from FastFoodNutrition
group by Company
--req5
select top 10
	Item,
	Sodium_mg
from FastFoodNutrition
order by Sodium_mg desc
--req6
select WeightWatchers_Points, avg(Calories) AvgCalo
from FastFoodNutrition
group by WeightWatchers_Points
--req7
select Company, avg(cast(Protein_g*1.0 / Calories as decimal(18,4))) as ProPerCalo
from FastFoodNutrition
where Calories > 0
group by Company
--req10
select top 5
	Item,
	Protein_g,
	Calories,
	cast(Protein_g*1.0 / Calories as decimal(18,4)) as sth
from FastFoodNutrition
where Calories > 0
order by sth desc

-- Cau 10 (Mutiverse)
SELECT TOP 5 Item, Protein_g, Calories
FROM FastFoodNutrition 
ORDER BY Protein_g DESC,Calories ASC




SELECT Company, COUNT(Item) AS Quantity
FROM FastFoodNutrition
GROUP BY Company 


SELECT Company , AVG(Calories) AS MeanCalo, AVG(TotalFat_g) AS MeanTotalFat, AVG(Protein_g) AS MeanProtein
FROM FastFoodNutrition
GROUP BY Company 
ORDER BY  MeanProtein DESC


SELECT Item, Protein_g, Calories
FROM FastFoodNutrition
WHERE Calories > (SELECT AVG(Calories) FROM FastFoodNutrition) AND Protein_g < (SELECT AVG(Protein_g) FROM FastFoodNutrition)


SELECT Company ,Item, Sodium_mg
FROM (SELECT Company, Item, Sodium_mg,ROW_NUMBER() OVER (PARTITION BY Company order by Sodium_mg desc)rn
		FROM FastFoodNutrition
		) t
WHERE rn <= 3 


SELECT TOP 5 
	Item,
	AVG(CAST(Calories/Protein_g AS DECIMAL(18,4)))
FROM FastFoodNutrition
GROUP BY Item

