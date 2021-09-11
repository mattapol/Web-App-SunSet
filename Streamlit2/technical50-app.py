import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import cufflinks as cf
from plotly import graph_objs as go

st.set_page_config(
    page_title="SUNSET50 - Technical",
    page_icon="favicon.ico",
)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://color-hex.org/colors/115380.png")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.subheader('SUNSET50 🌞')

# Retrieving tickers data
ticker_list = pd.read_csv("https://raw.githubusercontent.com/mattapol/Web-App-SunSet/main/Streamlit2/set50.csv")
symbols = ticker_list['Symbol'].sort_values().tolist()
ticker = st.sidebar.selectbox('Choose a SET50 Stock 📈', ticker_list) # Select ticker symbol

infoType = st.sidebar.radio(
        "Choose an info type",
        ('Fundamental', 'Statistics', 'Technical', 'Short Note')
    )

if(infoType == 'Fundamental'):
    stock = yf.Ticker(ticker)
    info = stock.info 
    st.title('Company Profile 🎢')
    string_logo = '<img src=%s>' % info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)
    st.subheader(info['longName']) 
    st.markdown('** Sector **: ' + info['sector'])
    st.markdown('** Industry **: ' + info['industry'])
    st.markdown('** Phone **: ' + info['phone'])
    st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
    st.markdown('** Website **: ' + info['website'])
    st.markdown('** Information Summary **')
    st.info(info['longBusinessSummary'])

elif(infoType == 'Statistics'):
    n_days = st.sidebar.number_input("Stock Prices Over Past... (1-365) days📅", 
                                                value=30,
                                                min_value=1, 
                                                max_value=365, 
                                                step=1)
    past_y = n_days * 1 + 1

    #show years 
    show_days = int(n_days)
    stock = yf.Ticker(ticker)
    info = stock.info 
    st.title('Statistics 📊')
    st.subheader(info['longName']) 
    st.markdown('** Previous Close **: ' + str(info['previousClose']))
    st.markdown('** Open **: ' + str(info['open']))
    st.markdown('** 52 Week Change **: ' + str(info['52WeekChange']))
    st.markdown('** 52 Week High **: ' + str(info['fiftyTwoWeekHigh']))
    st.markdown('** 52 Week Low **: ' + str(info['fiftyTwoWeekLow']))
    st.markdown('** 200 Week Days **: ' + str(info['twoHundredDayAverage']))

#The Past Of Price Stock 
    start = dt.datetime.today()-dt.timedelta(past_y)
    end = dt.datetime.today()
    df = yf.download(ticker,start,end)
    df = df.reset_index()
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'], 
                    high=df['High'], 
                    low=df['Low'], 
                    close=df['Close'])])
    st.write('Stock Prices Over Past ', show_days,' Days')
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.layout.update(width=800, 
                    height=500, 
                    yaxis_title='Price', 
                    xaxis_title='Date', 
                    xaxis_rangeslider_visible=True)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month",                                        
                    stepmode="backward"),
                dict(count=6, label="6m", step="month",  
                    stepmode="backward"),
                dict(count=1, label="YTD", step="year", 
                    stepmode="todate"),
                dict(count=1, label="1y", step="year", 
                    stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    st.plotly_chart(fig, use_container_width=True)

    if n_days < 365 :
        st.success("success 🎉🎊")
    elif n_days == 365 :
        st.success("success 🎉🎊, Limited to the past 1 years")

#Details Stock    
    fundInfo = {
            'Enterprise Value (TH฿)': info['enterpriseValue'],
            'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
            'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
            'Net Income (TH฿)': info['netIncomeToCommon'],
            'Profit Margin Ratio': info['profitMargins'],
            'Forward PE Ratio': info['forwardPE'],
            'PEG Ratio': info['pegRatio'],
            'Price to Book Ratio': info['priceToBook'],
            'Forward EPS (TH฿)': info['forwardEps'],
            'Beta ': info['beta'],
            'Book Value (TH฿)': info['bookValue'],
            'Dividend Rate (%)': info['dividendRate'], 
            'Dividend Yield (%)': info['dividendYield'],
            'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
            'Payout Ratio': info['payoutRatio']
        }
    
    fundDF = pd.DataFrame.from_dict(fundInfo, orient='index')
    fundDF = fundDF.rename(columns={0: 'Value'})
    st.subheader('Stock Info') 
    st.table(fundDF)

#Details Stock  
    marketInfo = {
            "Volume": info['volume'],
            "Average Volume": info['averageVolume'],
            "Market Cap": info["marketCap"],
            "Float Shares": info['floatShares'],
            "Regular Market Price (USD)": info['regularMarketPrice'],
            'Bid Size': info['bidSize'],
            'Ask Size': info['askSize'],
            "Share Short": info['sharesShort'],
            'Short Ratio': info['shortRatio'],
            'Share Outstanding': info['sharesOutstanding']
        }
    
    marketDF = pd.DataFrame(data=marketInfo, index=[0])
    st.table(marketDF)

elif(infoType == 'Technical'):  
    from datetime import date
    today = date.today()
    start_date = st.sidebar.date_input("Start date", date(2021, 1, 1))
    end_date = st.sidebar.date_input("End date", max_value=today)

    # Retrieving tickers data
    tickerData = yf.Ticker(ticker) # Get ticker data
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

    st.title('Indicator 🔬')

    #Level Of MACD, VOLUME
    st.subheader('Trend Following Indicators 🌊') 
    qf = cf.QuantFig(tickerDf, legend='top', name='GS')
    #qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
    qf.add_macd()
    qf.add_volume() 
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    #Level Of ADX, DMI
    qf = cf.QuantFig(tickerDf, legend='top', name='GS')
    qf.add_adx()
    qf.add_dmi() 
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    #Level Of SMA, EMA
    qf = cf.QuantFig(tickerDf, legend='top', name='GS')
    qf.add_sma([10,20],width=2,color=['green','lightgreen'],legendgroup=True)
    qf.add_ema()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    #Level Of RSI, CCI
    st.subheader('Momentum indicators 🌀')
    qf = cf.QuantFig(tickerDf, name='GS')
    qf.add_rsi(periods=20,color='java')
    qf.add_cci()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    #Level Of BOLLINGER, ATR 
    st.subheader('Volatility indicators 🌈')
    qf = cf.QuantFig(tickerDf, legend='top', name='GS')
    qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
    qf.add_atr()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    #qf.add_sma([10,20],width=2,color=['green','lightgreen'],legendgroup=True)
      #It adds Simple Moving Average (SMA) study to the figure.
    #qf.add_rsi(periods=20,color='java')
      #It adds Relative Strength Indicator (RSI) study to the figure.
    #qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
      #It adds Bollinger Bands (BOLL) study to the figure.
    #qf.add_macd()
      #It adds Moving Average Convergence Divergence (MACD) to the figure.
    #qf.add_volume() 
      #It adds volume bar charts to the figure.
    #qf.add_adx() 
      #It adds Average Directional Index (ADX) study to the figure.
    #qf.add_cci()
      #It adds Commodity Channel Indicator study to the figure.
    #qf.add_ema()
      #It adds Exponential Moving Average (EMA) to the figure.
    #qf.add_atr()
      #It adds Average True Range (ATR) study to the figure.
    #-qf.add_ptps()
      #It adds Parabolic SAR (PTPS) study to the figure.
    #-qf.add_resistance()
      #It adds resistance line to the figure.
    #-qf.add_trendline()
      #It adds trend line to the figure.
    #-qf.add_support()
      #It adds support line to the figure.
    #qf.add_dmi() 
      #It adds Directional Movement Index (DMI) study to the figure.

elif(infoType == 'Short Note'):
    def show():
        st.title('✅ Short Note')
        # Define initial state.
        if "todos" not in st.session_state:
            st.session_state.todos = [
                {"description": "Delete", "done": True},
                {
                    "description": "Test 🕹",
                    "done": False,
                },
            ]

        # Define callback when text_input changed.
        def new_todo_changed():
            if st.session_state.new_todo:
                st.session_state.todos.append(
                    {
                        "description": st.session_state.new_todo,
                        "done": False,
                    }
                )

        # Show widgets to add new TODO.
        st.write(
            "<style>.main * div.row-widget.stRadio > div{flex-direction:row;}</style>",
                    unsafe_allow_html=True,
        )
        st.sidebar.text_input("What do you need to remember?", on_change=new_todo_changed, key="new_todo")
                
        # Show all TODOs.
        write_todo_list(st.session_state.todos)

    def write_todo_list(todos):
        "Display the todo list (mostly layout stuff, no state)."
        st.sidebar.write("")
        col1, col2, _ = st.columns([0.05, 0.8, 0.15])
        all_done = True
        for i, todo in enumerate(todos):
            done = col1.checkbox("", todo["done"], key=str(i))
            if done:
                format_str = (
                        '<span style="color: grey; text-decoration: line-through;">{}</span>'
                )
            else:
                format_str = "{}"
                all_done = False
            col2.markdown(
                format_str.format(todo["description"]),
                unsafe_allow_html=True,
            )
            
        if all_done:
            st.success("Nice job on finishing all NOTE items! Good Luck 🎇")

    if __name__ == "__main__":
            show()