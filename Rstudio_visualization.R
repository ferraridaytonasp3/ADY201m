data <- read.csv("https://raw.githubusercontent.com/ferraridaytonasp3/ADY201m/refs/heads/main/FastFoodNutritionMenuV2.csv")
head(data)
#avg calories of each company
library(ggplot2)
avg_cal <- aggregate(Calories ~ Company, data = data, FUN = mean)
ggplot(avg_cal, aes(x = Company, y = Calories, fill = Company)) +
  geom_col() +
  theme_minimal() +
  labs(title = "Trung bình Calories của từng công ty",
       x = "Công ty",
       y = "Calories trung bình")
#correlation
library(ggplot2)
cor(data$Calories, data$TotalFat_g, use = "complete.obs")
ggplot(data, aes(x = TotalFat_g, y = Calories)) +
  geom_point(color = "blue") +   # Vẽ các điểm dữ liệu
  geom_smooth(method = "lm", se = TRUE, color = "red") +  # Thêm đường hồi quy tuyến tính
  theme_minimal() +
  labs(title = "Mối quan hệ giữa Calories và Total Fat",
       x = "Total Fat (g)",
       y = "Calories")
#propercalo
library(ggplot2)
data$Protein_Ratio <- data$Protein_g / data$Calories
avg_ratio <- aggregate(Protein_Ratio ~ Company, data = data, FUN = mean)
ggplot(avg_ratio, aes(x = Company, y = Protein_Ratio, fill = Company)) +
  geom_col() +
  theme_minimal() +
  labs(title = "Trung bình tỉ lệ Protein/Calories của từng công ty",
       x = "Công ty",
       y = "Tỉ lệ Protein / Calories")
#avg saturated fat of each calories
library(ggplot2)
avg_saturatedfat <- aggregate(SaturatedFat_g ~ Company, data = data, FUN = mean)
ggplot(avg_saturatedfat, aes(x = Company, y = SaturatedFat_g, fill = Company)) +
  geom_col() +
  theme_minimal() +
  labs(title = "Trung bình chất béo bão hòa của từng công ty",
       x = "Công ty",
       y = "Trung bình chất béo bão hòa")
#top 5
library(ggplot2)
library(dplyr)
top5 <- data %>%
  filter(Calories > 0) %>%
  mutate(ProteinPerCalories = Protein_g / Calories) %>%
  select(Company, Item, Protein_g, Calories, ProteinPerCalories) %>%  # Giữ lại cột Company
  arrange(desc(ProteinPerCalories)) %>%
  slice_head(n = 5)
ggplot(top5, aes(x = reorder(Item, ProteinPerCalories),
                 y = ProteinPerCalories,)) +
  geom_col() +
  coord_flip() +
  theme_minimal() +
  labs(title = "Top 5 món ăn có tỉ lệ Protein/Calories cao nhất theo công ty",
       x = "Món ăn",
       y = "Tỉ lệ Protein / Calories")


