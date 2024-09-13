def getKali(*numbers): 
    result = 1
    for number in numbers:
        result /= number
    return result

result = getKali(100, 10, 5)

print("jawabannya adalah:", result)
