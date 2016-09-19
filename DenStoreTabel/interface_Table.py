from DenStoreTabel import Table, PartitionTable

#print("\n".join(
#    [
#        " ".join(
#            map(
#                lambda n: "{1:>{0}}".format(len(str(x * y)), n),
#                [i * j for i in range(1, x + 1)]))
#                 for j in range(1, y + 1)]))


try:
    x, y = map(int, input("x, y: ").split(","))
    if x < 0 or y < 0:
        raise Exception
    print("\n".join([" ".join(map(lambda n: "{1:>{0}}".format(len(str(x*y)), n), [i*j for i in range(1, x + 1)])) for j in range(1, y + 1)]))
    #print(Table(100, 100, 90, 90))
except Exception:
    print("Your input is not compliant")