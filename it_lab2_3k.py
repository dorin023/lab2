import math

height=float(input('Введите рост: '))
weight=float(input('Введите ваш вес: '))
k_s=float(input('Введите кол-во шагов:'))
t=float(input('Введите время активности:'))
S_s=height/4+0.37
s=S_s*k_s
v=s/(t*60)
Kkal=0.035*weight+(v**2/height)*0.029*weight
print(f'Пройденная дистанция: {s} Кол-во сожженных калорий:{Kkal}')
km=s/1000
print("кол-во пройденных км:"+str(km))
if km<2:
    print("Вы прошли меньше 2 км, необходимо работать усерднее")
elif km<4:
    print("Вы прошли меньше 4 км, достойный результат!")
else:
    print("Вы прошли больше 4 км, отличный результат!")
    
