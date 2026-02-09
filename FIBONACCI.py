
number1=1

number2=1

fiboncacci=[number1,number2]

for i in range(10):
    number1,number2=number2,number2+number1
    fiboncacci.append(number2)

print(fiboncacci)