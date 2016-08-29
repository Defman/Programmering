import numpy as np

precision = np.random.randint(1, 10, 10)
floats = np.random.rand(10)

for p, f in zip(precision, floats):
    print("Printing {1} with {0} floating points = {1:.{0}f}".format(p, f))