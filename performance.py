import pandas as pd 
import matplotlib.pyplot as plt 
import tushare as ts 

ts.set_token("76ab766e3042d471789d4af2b4163ee1975a490ad24d631270b872e0")

pro = ts.pro_api()

df = pro.daily(
    ts_code="600519.SH",
    start_date="20240101",
    end_date="20250101"
)
df = df.sort_values("trade_date").reset_index(drop=True)

df["ma5"]=df["close"].rolling(5).mean()
df["ma20"]=df["close"].rolling(20).mean()

df["signal"]=df["ma5"]>df["ma20"]

df["position"]=df["signal"].shift(1)

df["market_ret"]=df["close"].pct_change()
df["market_cum"]=(1+df["market_ret"]).cumprod()

df["strategy_ret"]=df["market_ret"]*df["position"]
df["strategy_cum"]=(1+df["strategy_ret"]).cumprod()

df["sharpe"]=df["strategy_ret"].mean()/df["strategy_ret"].std()*(252**0.5)

df["drawdown"]=df["strategy_cum"]/df["strategy_cum"].cummax()-1
df["max_drawdown"]=df["drawdown"].min()

plt.figure(figsize=(12,6))
plt.plot(df["market_ret"],label="market_curve")
plt.plot(df["strategy_cum"],label="strategy_curve")
plt.plot(df["drawdown"],label="drawdown")

plt.legend()
plt.show()
