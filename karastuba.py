p = input("enter first number")
q = input("enter the second number")

len_p = len(p)
len_q = len(q)

if len_p % 2 == 0:
    a = int(p[:len_p // 2])
    b = int(p[len_p // 2:])
    n = len_p // 2
else:
    a = int(p[:(len_p + 1) // 2])
    b = int(p[(len_p + 1) // 2:])

    n = len_p - (len_p + 1) // 2
if len_q % 2 == 0:
    c = int(q[:len_q // 2])
    d = int(q[len_q // 2:])
else:
    c = int(q[:(len_q + 1) // 2])
    d = int(q[(len_q + 1) // 2:])

result = (10 ** (2 * n)) * (a * c) + (10 ** n) * (a * d + b * c) + b * d
print("result is {} and actual values is {}".format(result, int(p) * int(q)))
