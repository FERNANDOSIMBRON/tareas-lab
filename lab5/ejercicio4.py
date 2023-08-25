l1 = [("one", 1), ("two", 2),("three", 3),("four",4),("five",5)]
l2 = [("one", 1),("two",2),("six",6)]

s1 = set(l1)
s2 = set(l2)

s3 = s1.intersection(s2)

s4 = s1.symmetric_difference(s2)

l3 = sorted(list(s3.union(s4)), key=lambda x: x[1])

print("conjunto S1:", s1)
print("")
print("conjunto S2:", s2)
print("")
print("conjunto de elementos comunes:", s3)
print("")
print("conjunto de elementos unicos:", s4)
print("")
print("lista L3:", l3)

