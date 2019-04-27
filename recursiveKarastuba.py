p = input("enter the first number")
q = input("enter the second number")


def recur_karastuba(p, q):
    len_p = len(p)
    len_q = len(q)
    n = min(len_p,len_q)//2

    if len_p == 1 or len_q == 1:
        return int(p) * int(q)

    else:
        a = int(p[:len_p-n])
        b = int(p[len_p-n:])


        c = int(q[:len_q-n])
        d = int(q[len_q-n:])

    n1 = recur_karastuba(str(a), str(c))
    n3 = recur_karastuba(str(b), str(d))
    n2 = recur_karastuba(str(a+b),str(c+d))-n1-n3
    result = (10 ** (2 * n)) * n1 + (10 ** n) * (
            n2) + n3

    return result


res = recur_karastuba(p, q)
print("result is {} and actual values is {}".format(res, int(p) * int(q)))
