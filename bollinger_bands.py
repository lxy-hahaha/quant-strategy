import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock.csv")

df["ma20"] = df["close"].rolling(20).mean()
df["std"] = df["close"].rolling(20).std()

df["upper"] = df["ma20"] + 2 * df["std"]
df["lower"] = df["ma20"] - 2 * df["std"]

'''
plt.figure(figsize=(12,6))

plt.plot(df["close"], label="price")
plt.plot(df["ma20"], label="MA20")
plt.plot(df["upper"], label="Upper")
plt.plot(df["lower"], label="Lower")

plt.legend()
plt.show()
'''
plt.figure(figsize=(12,6))

plt.plot(df["close"], label="price")
plt.plot(df["ma20"], label="MA20",marker="s")

plt.plot(df["upper"], linestyle="--",label="Upper")
plt.plot(df["lower"], linestyle="--")

plt.fill_between(df.index, df["upper"], df["lower"], alpha=0.2)

plt.legend()
plt.show()