if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    l2 = []

    for i in range(x + 1):
        l3 = []
        for j in range(y + 1):
            for k in range(z + 1):
                l3 = [i, j, k]
                sum = 0
                for l in l3:
                    sum += l

                if sum != n:
                    l2.append(l3)

    print(l2)

