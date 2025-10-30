

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\LaLaLa\ADY201m\Data\FastFoodNutritionMenuV2.csv")


sns.set(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 6)

while True:
    print('Chọn các mục sau đây')
    
    print('1.So sánh tổng thể năng lượng trung bình trong sản phẩm của mỗi công ty ')
    
    print('2.Kiểm định tỷ lệ các thành phần dinh dưỡng chính (chất béo, đường, năng lượng, v.v.) để đảm bảo tuân thủ tiêu chuẩn an toàn và chất lượng thực phẩm. ')
    
    print('3.Đánh giá mức độ ảnh hưởng của sản phẩm đến sức khỏe tim mạch, xác định thương hiệu có tỷ lệ sản phẩm tiềm ẩn nguy cơ cao đối với hệ tim mạch')
    
    print('4.Phân tích chất lượng dinh dưỡng của sản phẩm dựa trên tỷ lệ hàm lượng đạm so với tổng năng lượng, nhằm xác định mức độ cân đối và giá trị dinh dưỡng của từng công ty. ')
    
    print('5.Xác định món ăn tốt nhất theo tiêu chí dinh dưỡng.')

    print('6.Thoát chương trình')

    choice = input('Nhập lựa chọn của bạn : ')
    if choice == '1':
        calories_mean = df.groupby("Company")["Calories"].mean().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        sns.barplot(x=calories_mean.values, y=calories_mean.index)
        plt.title("Trung bình lượng Calories theo công ty", fontsize=14)
        plt.xlabel("Calories trung bình")
        plt.ylabel("Công ty")
        plt.tight_layout()
        plt.show()
    elif choice == '2':
        corr = df[["Calories", "TotalFat_g", "Sugars_g", "Protein_g", "Carbs_g", "WeightWatchers_Points"]].corr()

        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Ma trận tương quan giữa các thành phần dinh dưỡng", fontsize=14)
        plt.tight_layout()
        plt.show()
    elif choice == '3':
        req4 = df.groupby('Company')['SaturatedFat_g'].mean()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=req4.values, y=req4.index)
        plt.title("Trung bình lượng chất béo bão hòa theo công ty", fontsize=14)
        plt.xlabel("Chất béo bão hòa trung bình")
        plt.ylabel("Công ty")
        plt.tight_layout()
        plt.show()
    
    elif choice == '4':

        req7semi = df.loc[df['Calories'] > 0].copy()
        req7semi['ProteinPerCalo'] = req7semi['Protein_g'] / req7semi['Calories']
        req7 = req7semi.groupby('Company')['ProteinPerCalo'].mean()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=req7.values, y=req7.index)
        plt.title("Trung bình lượng đạm trên calo theo công ty", fontsize=14)
        plt.xlabel("Đạm trên calo trung bình")
        plt.ylabel("Công ty")
        plt.tight_layout()
        plt.show()

    elif choice == '5':
        req10b_semi = df.loc[df['Calories'] > 0].copy()
        req10b_semi['ProteinPerCalo'] = req10b_semi['Protein_g'] / req10b_semi['Calories']
        req10b = req10b_semi.groupby(['Item','Calories','Protein_g'])['ProteinPerCalo'].mean().sort_values(ascending=False).head(5).reset_index()

        plt.figure(figsize=(10, 6))
        sns.barplot(x='ProteinPerCalo', y='Item', data=req10b, palette='viridis')
        plt.title("Top 5 sản phẩm có lượng đạm trên calo cao nhất", fontsize=14)
        plt.xlabel("Đạm trên mỗi calo (ProteinPerCalo)")
        plt.ylabel("Sản phẩm")
        plt.tight_layout()
        plt.show()

    elif choice == '6': 
        print('Đã Thoát')
        break
    else: 
        print('hãy nhập giá trị hợp lệ !')


