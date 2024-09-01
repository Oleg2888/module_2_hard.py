def find_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                pairs.append((i, j))
    result = ''.join(f'{pair[0]}{pair[1]}' for pair in pairs)
    return result


n = int(input("Введите число: "))
password = find_password(n)
print("Нужный пароль: ", password)

for n in range(3, 21):
    password = find_password(n)
    print(f'{n} - {password}')
