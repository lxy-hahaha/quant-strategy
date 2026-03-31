import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data\stock.csv")

df["ma5"]=df["close"].rolling(5).mean()
df["ma20"]=df["close"].rolling(20).mean()

df["signal"]=df["ma5"]>df["ma20"]
df["position"]=df["signal"].shift(1)

df["return"]=df["close"].pct_change()#市场收益率
df["strategy_ret"]=df["return"]*df["position"]#策略收益率
#df["strategy"]=(1+df["return"]).pct_change()
#df["strategy_ret"]=df["strategy"]*df["position"]
df["cum"]=(1+df["strategy_ret"]).cumprod()
#df["cum"]=(1+df["strategy_ret"]).pct_change()
df["market"]=(1+df["return"]).cumprod()
#df["market"]=(1+df["return"]).pct_change()

plt.figure(figsize=(12,6))

plt.plot(df["cum"],label="strategy")
plt.plot(df["market"],label="market")

plt.legend()
plt.show()