import sys
import math
import random
import statistics

print(math.cos(math.pi/4))
print(math.log(1024, 2))

print(random.choice(['kale', 'celery', 'milk']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(10, 45))

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
mean = statistics.mean(data)
median = statistics.median(data)
variance = statistics.variance(data)
print("Mean: {}, Median: {}, Variance: {}".format(mean, median, variance))
