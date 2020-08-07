# stock-portfolio-ml-model
Predict stock prices using a Keras LSTM neural network.

# Overview

This module was part of a group project for the Vanderbilt Fintech Bootcamp (summer 2020). In this project we created a tool for 
choosing an investment portfolio from a selection of stocks provided by a chat bot. The user (e.g., a portfolio manager) 
interacts with the bot to filter stocks from the New York Stock Exchange & NASDAQ and select a number ofstocks that match 
the user's investment preferences (i.e. avg. daily volume and P/E ratio). 

Upon selection of the portfolio, the list of stock tickers is sent to the module herein, which implements a LSTM (long short-term
memory) neural network for each stock.
