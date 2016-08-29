from Quadratic import NormalQuadratic

while True:
    try:
        a, b, c = map(float, input("a, b, c: ").split(","))
        print(NormalQuadratic().result(a, b, c))
    except Exception:
        print("Your input is not compliant")

