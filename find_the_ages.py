def findAges(product, total):
    for i in range(1, product+1):
        for j in range(i, product+1):
            for k in range(j, product+1):
                if i * j * k == product and i + j + k == total:
                    if k > i and k > j:   # eldest daughter exists
                        return i, j, k

# Example
product = 36
sum_age = 13

ages = findAges(product, sum_age)
print("Ages are:", ages)
