# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.


#Build a dollar cost avareging bot( DCA) that buys bitcoins from binance and recieves indicators analysis from trading view

import unittest

class TestDCABot(unittest.TestCase):
    def test_DCABot_get_binance_api():
        pass

    def test_DCABot_get_tradingview_api():
        pass

    def test_DCABot_get_binance_client():
        pass

    def test_DCABot_get_top_10_lowest_coins():
        pass

    def test_DCABot_get_ta_recommendations():
        pass

    def test_DCABot_buy_coin():
        pass

    def test_DCABot_sell_coin():
        pass

    def test_DCABot_record_trades():
        pass

    def test_DCABot_record_logs():
        pass







    

    

#establish a connection with binance 

#establish a connection wih trading view

#establish the top 10 coins

#establish coins with recommendation to buy from trading view

#place a buy order upon recommendatiion

# sell when the coin reaches a stop loss of 1% or a profit of 2%

#record trades in a json file for further analysis

#log how the code runs in a log file

