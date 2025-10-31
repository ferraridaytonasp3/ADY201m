# --- Phân tích thống kê mô tả (Descriptive Statistics) ---
COPYDATA <- read.csv("https://raw.githubusercontent.com/ferraridaytonasp3/ADY201m/refs/heads/main/FastFoodNutritionMenuV2.csv")
# 1. Tổng quan dữ liệu
summary(COPYDATA)

# 2. Trung bình, độ lệch chuẩn, phương sai cho các cột số
mean(COPYDATA$Calories, na.rm = TRUE)
sd(COPYDATA$Calories, na.rm = TRUE)
var(COPYDATA$Calories, na.rm = TRUE)

# Nếu muốn tính nhiều biến một lúc:
num_cols <- sapply(COPYDATA, is.numeric)
sapply(COPYDATA[, num_cols], mean, na.rm = TRUE)
sapply(COPYDATA[, num_cols], var, na.rm = TRUE)

# Ma trận tương quan giữa các biến số
cor(COPYDATA[, num_cols], use = "complete.obs")

# Vẽ heatmap tương quan 
library(ggplot2)
library(reshape2)
num_cols <- sapply(COPYDATA, is.numeric)
corr_matrix <- cor(COPYDATA[, num_cols], use = "complete.obs")
melted_corr <- melt(corr_matrix)

ggplot(data = melted_corr, aes(x=Var1, y=Var2, fill=value)) +
  geom_tile() +
  scale_fill_gradient2(low="blue", high="red", mid="white",
                       midpoint=0, limit=c(-1,1), space="Lab",
                       name="Hệ số tương quan") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=45, vjust=1, hjust=1))




