# Product_Checkout
the Checkout class is in charge of the initize, add and calc of the order

inti initialize the order with the customer company, the pizza price is set when initialize, this allows for easy modification whenever the price is referred.

the add function add item by its name to the order, allow for upper/lower case differences.
if the item ordered does not exist, a string "No such type of pizza" will be printed. In a more complex environment, this can be replaced with a Exception. And handled later on.

in the total function, the price is calculated with the function. I'm aware of all the caculations can be isolated into individual functions, but with the small data size and relatively simple calculation i was given, this is more straight forward.

run main_test.py for unit test
