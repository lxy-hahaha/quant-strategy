import pandas as pd

df = pd.read_csv("stock.csv")

# 计算均线
df["ma5"] = df["close"].rolling(5).mean()
df["ma20"] = df["close"].rolling(20).mean()

# 使用shift避免未来数据
df["ma5_prev"] = df["ma5"].shift(1)
df["ma20_prev"] = df["ma20"].shift(1)

# 生成信号
df["signal"] = 0

df.loc[df["ma5_prev"] > df["ma20_prev"], "signal"] = 1
df.loc[df["ma5_prev"] < df["ma20_prev"], "signal"] = -1

print(df)

