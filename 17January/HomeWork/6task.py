n = int(input("введите число n "))
x = n
y = 0
for i in range(1, n):
       n = int(n / 10)
       y += 1;
       if n < 1:
           break

        
(print(f" Количество цифр в записи числа {x} = {y}"))
