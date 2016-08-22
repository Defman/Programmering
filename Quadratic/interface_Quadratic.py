import Quadratic


while True:
    a, b, c = map(float, input("a, b, c: ").split(","))
    print(Quadratic.quadratic(a, b, c))

