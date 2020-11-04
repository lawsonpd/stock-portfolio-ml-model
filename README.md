# stock-portfolio-ml-model
Predict stock prices using a Keras LSTM neural network.

# Overview

This module was part of a group project for the Vanderbilt Fintech Bootcamp (summer 2020). In this project we created a tool for 
choosing an investment portfolio from a selection of stocks provided by a chat bot. The user (e.g., a portfolio manager) 
interacts with the bot to filter stocks from the New York Stock Exchange & NASDAQ and select a number ofstocks that match 
the user's investment preferences (i.e. avg. daily volume and P/E ratio). 

## How to use

The code can be imported as a module or run stand-alone from the command line. 
When run from the command line, it accepts the flag `--portfolio` followed by a 
string of stock tickers, for example:

```
#prompt> python predict.py --portfolio 'AAPL, NFLX, GOOGL, TSLA'
```

This will return (log to the console) a dictionary of keys 'predicted_return', 
'sharpe_ratio' and 'predicted_date'.

The module can also be imported. `import predict` to load, then 

```
my_results = predict.get_portfolio_predictions(list_of_tickers)
```

to get prediction results.

### Testing

To show the running time at the command line, set `--test` to `True`, e.g.

```
#prompt> python predict.py --portfolio 'AAPL, NFLX, GOOGL, TSLA --test=True
```

(I considered doing more with this but couldn't think of what else might be needed.)

