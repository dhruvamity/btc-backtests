"""
BTC 5min OOS backtest – final production script
"""
import backtester
if __name__ == "__main__":
    backtester.run(oos_hours=3.5, save_report=True)
