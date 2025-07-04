land = 80
seg = 5
seg_area = land // seg

t1_area = 0.30*seg_area
t2_area = 0.70*seg_area

t1_yieldperacre_tonnes = 10
t2_yieldperacre_tonnes = 12
potato_yieldperacre_tonnes = 10
cabbage_yieldperacre_tonnes = 14
sunflower_yieldperacre_tonnes = 0.7
sugarcane_yieldperacre_tonnes = 45

tomato_price_perkg = 7
potato_price_perkg = 20
cabbage_price_perkg = 24
sunflower_price_perkg = 200
sugarcane_price_pertonne = 4000

t1_sales = t1_area * t1_yieldperacre_tonnes * tomato_price_perkg * 1000
t2_sales = t2_area * t2_yieldperacre_tonnes * tomato_price_perkg * 1000
potato_sales = seg_area * potato_yieldperacre_tonnes * potato_price_perkg * 1000
cabbage_sales = seg_area * cabbage_yieldperacre_tonnes * cabbage_price_perkg * 1000
sunflower_sales = seg_area * sunflower_yieldperacre_tonnes * sunflower_price_perkg * 1000
sugarcane_sales = seg_area * sugarcane_yieldperacre_tonnes * sugarcane_price_pertonne

total_sales = t1_sales + t2_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
print("Total Sales: Rs.",total_sales)
