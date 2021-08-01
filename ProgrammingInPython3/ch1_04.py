import sys
import random

print(sys.argv)
x = random.randint(1,6)
y = random.choice(['apple', 'banana', 'cherry', 'durian'])
print(x, y)