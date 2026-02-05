import json
import pandas as pd
import yfinance as yf
from datetime import datetime, timezone, timedelta

# ======================
# Config
# ======================
TICKER_GC = "GC=F"
TICKER_DXY = "DX-Y.NYB"
TICKER_TNX = "^TNX"
TICKER_VIX = "^VIX"

# 用于计算均线/关键位/雷达等（足够算 20 日）
PERIOD_CALC = "3mo"
INTERVAL = "1d"

# 页面表格展示条数
TABLE_ROWS = 30

OUT_FILE = "gold_data.json"

# 如果你想保留旧的 Real Yield driver（用 ^TNX 近似），改 True
KEEP_REAL_YIELD_DRIVER = False
