import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
          self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2 ), msg = "Fail => test_getDataPoint_calculatePrice() Expected value does not match actual value")
          self.assertTrue(True, "test_getDataPoint_calculatePrice() => Testcase passed successfully")
                            
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    
    for quote in quotes:
          self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2) ,msg = "Fail => test_getDataPoint_calculatePriceBidGreaterThanAsk() Expected value does not match actual value")
          self.assertTrue(True, "test_getDataPoint_calculatePriceBidGreaterThanAsk() => Testcase passed successfully")
              
  """ ------------ Add more unit tests ------------ """
  
  def test_getRatio_calculateRatio(self):
        stockPrices = [
            {'price_a': 118.24, 'price_b': 120.09},
            {'price_a': 119.84, 'price_b':121.17},
            {'price_a': 0, 'price_b':121.17},
        ]

        for price in stockPrices:
              self.assertEqual( getRatio(price['price_a'], price['price_b']) , price['price_a']/price['price_b'] )
             
  def test_getRatio_divideByZero(self):
        self.assertIsNone(getRatio(10,0))
        
  '''
        stockPrices = [
            {'price_a': 118.24, 'price_b':0},
        ]

        for price in stockPrices:
              self.assertEqual( getRatio(price['price_a'], price['price_b']) , price['price_a']/price['price_b'] )
'''

if __name__ == '__main__':
    unittest.main()
