import numpy as np
import pandas as pd

# a = np.array([[5, 7, 9], [2, 5, 6], [3, 5, 7]])
# print(a)
# print(np.transpose(a))
# # print(a[:, 1])
# # print(a[1, :])
# print(np.matmul(a, a))
# print(np.matmul(a, np.transpose(a)))
# print(np.dot(a, a))
# print(np.dot(a, np.transpose(a)))
# print(a * a)

series = pd.Series([2, 7, 9, 15, 4, 15, 4, 15, 15, 15])
# print(series)

df = pd.DataFrame(data={"v1": series, "v2": [7, 8, 5, 6, 2, 22, 7, 12, 7, 16]}, columns=["v1", "v2"])
# print(df)

# print(df[(df["v1"] >= 2) &  (df["v1"] <= 4)])

print(df.sort_values(by=["v1", "v2"], ascending=False))
print(df.sort_values(by=["v1"], ascending=False))
