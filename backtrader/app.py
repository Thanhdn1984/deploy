import streamlit as st
import backtrader as bt
import pandas as pd

st.title("Backtrader Integration")

# Upload dữ liệu CSV để backtest
uploaded_file = st.file_uploader("Upload CSV file for backtesting", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file, index_col=0, parse_dates=True)

    # Chuyển đổi dữ liệu thành Backtrader DataFeed
    class PandasData(bt.feeds.PandasData):
        params = (
            ('datetime', None),
            ('open', -1),
            ('high', -1),
            ('low', -1),
            ('close', -1),
            ('volume', -1),
        )

    bt_data = PandasData(dataname=data)

    # Cài đặt chiến lược đơn giản
    class TestStrategy(bt.Strategy):
        def next(self):
            if not self.position:
                self.buy(size=1)
            elif self.data.close[0] > self.data.close[-1]:
                self.sell(size=1)

    # Khởi tạo Backtrader
    cerebro = bt.Cerebro()
    cerebro.adddata(bt_data)
    cerebro.addstrategy(TestStrategy)

    # Chạy Backtest và hiển thị kết quả
    cerebro.run()
    st.pyplot(cerebro.plot()[0][0])
