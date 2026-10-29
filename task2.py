import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
n = 20
delivery_distance = np.random.uniform(1, 15, n).round(1)
delivery_time = (10 + delivery_distance * 2.5 + np.random.normal(0, 4, n)).round(0)
order_value = np.random.randint(150, 1200, n)
tip_amount = (order_value * 0.08 + np.random.normal(0, 8, n)).round(0)
rating = (5 - delivery_time * 0.03 + np.random.normal(0, 0.3, n)).clip(1, 5).round(1)

df = pd.DataFrame({
    "delivery_time": delivery_time,
    "order_value": order_value,
    "tip_amount": tip_amount,
    "rating": rating,
    "delivery_distance": delivery_distance
})

sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap - Food Delivery Data")
plt.show()