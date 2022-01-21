from cgitb import small
import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_init(self):
         co = Checkout("Microsoft")
         self.assertEqual(co.customer,"microsoft")
         co = Checkout("")
         self.assertEqual(co.customer,'')
         
    def test_add(self):
        co = Checkout('')
        co.add("small pizza")
        self.assertEqual(co.item, ["small pizza"])
        co.add("Small Pizza")
        self.assertEqual(co.item, ["small pizza","small pizza"])
        co.add("small")
        self.assertEqual(co.item, ["small pizza","small pizza"])
        co.add("s")
        self.assertEqual(co.item, ["small pizza","small pizza"])
        co.add(0)
        self.assertEqual(co.item, ["small pizza","small pizza"])
        
    def test_total(self):
        co = Checkout('default')
        co.add('small pizza')
        co.add('medium pizza')
        co.add('large pizza')
        self.assertEqual(co.total(),49.97,"no discount")

        co = Checkout('Microsoft')
        co.add('small pizza')
        co.add('small pizza')
        co.add('small pizza')
        co.add('large pizza')
        self.assertEqual(co.total(),45.97,"small 3for2")

        co = Checkout('Microsoft')
        co.add('small pizza')
        co.add('small pizza')
        co.add('small pizza')
        co.add('large pizza')
        co.add('small pizza')
        self.assertEqual(co.total(),57.96,"small 3for2 with 1 additional small")

        co = Checkout('Microsoft')
        co.add('small pizza')
        co.add('small pizza')
        co.add('small pizza')
        co.add('small pizza')
        co.add('large pizza')
        co.add('small pizza')
        self.assertEqual(co.total(),69.95,"small 3for2 with 2 additional small")

        co = Checkout('Amazon')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        co.add('large pizza')
        self.assertEqual(co.total(),67.96,"$19.99 for large")

        co = Checkout('facebook')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        self.assertEqual(co.total(),63.96,"5 for 4 medium")

        co = Checkout('facebook')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        self.assertEqual(co.total(),79.95,"5 for 4 medium, 1 redundent")

        co = Checkout('facebook')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        co.add('Medium pizza')
        self.assertEqual(co.total(),95.94,"5 for 4 medium, 2 redundent")
if __name__ == '__main__':
    unittest.main()