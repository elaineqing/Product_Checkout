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
        assert(co.total(),49.97)

        co = Checkout('Microsoft')
        co.add('small pizza')
        co.add('Small pizza')
        co.add('small pizza')
        co.add('large pizza')
        assert(co.total(),45.97)

        co = Checkout('Amazon')
        co.add('Medium pizza')
        co.add('medium pizza')
        co.add('medium pizza')
        co.add('large pizza')
        assert(co.total(),67.69)

if __name__ == '__main__':
    unittest.main()