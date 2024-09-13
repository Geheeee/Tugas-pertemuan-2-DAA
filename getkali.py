def getKali(*numbers):  
    result = 1
    for number in numbers:
        result *= number
    return result
result = getKali(5, 10, 2)


print("jawabannya adalah:", result)
