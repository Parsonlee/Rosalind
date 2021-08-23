def fibonacciRabbits(n, m):
    F = [0, 1, 1]
    for i in range(3, n + 1):
        if i <= m:
            total = F[i - 1] + F[i - 2]
        elif i == m + 1:
            total = F[i - 1] + F[i - 2] - 1
        else:
            total = F[i - 1] + F[i - 2] - F[i - m - 1]
        F.append(total)

    print(F[n])


fibonacciRabbits(84, 18)
