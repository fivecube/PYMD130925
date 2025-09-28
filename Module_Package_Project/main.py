from module1 import add, subtract
from module2 import multiply
from package1 import mango

output1 = add(2, 3)

output2 = subtract(3, 1)

output3 = multiply(4, 5)

print('output1', output1)

print('output2', output2)

print('output3', output3)


apple_obj = mango.Apple(50)
mango_obj = mango.Banana(100)

print(apple_obj.get_name(), apple_obj.number_of_apples)
print(mango_obj.get_name(), mango_obj.number_of_bananas)