def find_password(n):
    pairs = []

    for i in range(1, n):
        for j in range(i, n):
            if (i + j) % n == 0:
                pairs.append(str(i) + str(j))

    result = ''.join(pairs)

    return result


n = int(input("Введите число (от 3 до 20): "))
if 3 <= n <= 20:
    result = find_password(n)
    print("Результат:", result)
else:
    print("Введите число в диапазоне от 3 до 20.")
