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



