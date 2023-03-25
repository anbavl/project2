number = int(input("Введите количество билетов: "))
i = 0
price1 = 0
price2 = 990
price3 = 1390
sum = 0


if number>3:
   price2 = price2-(price2/100)*10
   price3 = price3-(price3/100)*10


while i<number:
   i=i+1
   age = int(input("Введите возраст: "))


   if age<18:
       print("Стоимость билета: ", price1)
   elif 18<=age<25:
       sum = price2+sum
       print("Стоимость билета: ", int(price2))
   else:
       sum = price3+sum
       print("Стоимость билета: ", int(price3))
print("Итоговая стоимость: ", int(sum))