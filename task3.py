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

corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)
plt.title("Correlation Heatmap (coolwarm)")
plt.show()

pairs = corr.unstack()
pairs = pairs[pairs.index.get_level_values(0) != pairs.index.get_level_values(1)]
print("Strongest negative correlation:", pairs.idxmin(), "=", round(pairs.min(), 2))

# Explanation :
# The blue cells show negative correlation. The pair printed above has the most negative value.
# In this data, a longer delivery time goes with a lower rating,
# because customers rate slow deliveries lower.