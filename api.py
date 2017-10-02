def mine_data(in_file):
    stock_list = {}
    import numpy as np

    with open(in_file) as stocks:
        field = 0
        while True:
            field += 1
            stock = stocks.readline().split(',')
            if len(stock[0]) == 0:
                 break
            if field  % 7 == 1:
                 name = stock[0].strip()
            elif field  % 7 == 2:
                 close = [float(pt) for pt in stock]
            elif field % 7 == 3:
                 low = [float(pt) for pt in stock]
            elif field % 7 == 4:
                 high = [float(pt) for pt in stock]
            elif field % 7 == 5:
                 capacity = [float(pt) for pt in stock]
            elif field % 7 == 6:
                 open_p = [float(pt) for pt in stock]
            elif field % 7 == 0:
                 fluctuation = build_fluctuation(high, low)
                 candlestick = build_candlestick(open_p, low, high, close)
                 stock_data = np.array(open_p, low, high, close, capacity, fluctuation, candlestick)
                 stock_list[name] = stock_data
            else:
                 pass
    return stock_list

def build_fluctuation(high, low):
    return [(high[day] - low[day])/ low[day] for day in range(len(high))]

def build_candlestick(open_p, low, high, close):
    candlestick = []

    for day in range(len(open_p)):
        if open_p[day] == close[day] and open_p[day] > low[day] and open_p[day] < high[day]:  #cross
            candlestick.append(0)
        elif open_p[day] == close[day] and open_p[day] == low[day] and high[day] > low[day]: #tomb
            candlestick.append(1)
        elif open_p[day] == close[day] and open_p[day] == high[day] and low[day] <  high[day]: #opp. of tomb
            candlestick.append(2)
        elif open_p[day] == close[day] and close[day] == low[day] and low[day] == high[day]: #dash
            candlestick.append(3)
        elif open_p[day] == low[day] and open_p[day] < close_p[day] and close_p[day] < high[day]: #dagger up
            candlestick.append(4)
        elif open_p[day] == high[day] and open_p[day] > close_p[day] and close_p[day] > low[day]: #dagger down
            candlestick.append(5)
        elif high[day] == close[day] and open_p[day] == low[day] and close[day] > open_p[day]: #keep rising
            candlestick.append(6)
        elif low[day] == close[day] and open_p[day] == high[day] and close[day] < open_p[day]: #keep lowering
            candlestick.append(7)
        else:
            candlestick.append(8)
    return candlestick

def find_at_peak(stock_data, candidate=[], day = 10):
    #identify stock near the peak return list of index
    return

def find_dagger(stock_data, candidate=[], rise = .3, blade = .2):
    #find dagger
    return

def find_concordance(stock_data):
    #concordance of stock with global
    return

def visualize_trend(stock_data):
    #some stupid matplotlib shit
    import matplotlib.pyplot as plt
    pass

def decide_day_trade():
    #strategy
    return
