import pandas as pd
pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)

P1=[]
P2=[]
P3=[]

file1=open('P1.txt',"r")
for line in file1:
    P1.append(int(line.strip('\n')))
file2=open('P2.txt',"r")
for line in file2:
    P2.append(int(line.strip('\n')))
file3=open('P3.txt',"r")
for line in file3:
    P3.append(int(line.strip('\n')))

A1 = []
A2 = []
A3 = []
A1.append(P1[0])
A1.append(P2[0])
A1.append(P3[0])
A2.append(P1[1])
A2.append(P2[1])
A2.append(P3[1])
A3.append(P1[2])
A3.append(P2[2])
A3.append(P3[2])

minA1 = min(A1)
minA2 = min(A2)
minA3 = min(A3)
maxA1 = max(A1)
maxA2 = max(A2)
maxA3 = max(A3)

list1 = []
list2 = []
list3 = []
list11 = []
list22 = []
list33 = []

valda = []
maximum = []
laplasa = []
gulcvina = []
baes = []

#Valda
valda.append(minA1)
valda.append(minA2)
valda.append(minA3)
maxv = max(valda)
if valda.index(maxv) == 0:
    print("Критерій Вальда - Обираємо стратегію N=1")
if valda.index(maxv) == 1:
    print("Критерій Вальда - Обираємо стратегію N=2")
if valda.index(maxv) == 2:
    print("Критерій Вальда - Обираємо стратегію N=3")
    
#Maximum
maximum.append(maxA1)
maximum.append(maxA2)
maximum.append(maxA3)
maxm = max(maximum)
if maximum.index(maxm) == 0:
    print("Максимальний критерій - Обираємо стратегію N=1")
if maximum.index(maxm) == 1:
    print("Максимальний критерій - Обираємо стратегію N=2")
if maximum.index(maxm) == 2:
    print("Максимальний критерій - Обираємо стратегію N=3")

#Laplasa
for i in A1:
    j = i*0.33
    list1.append(j)
    sum1 = sum(list1)
for o in A2:
    q = o*0.33
    list2.append(q)
    sum2 = sum(list2)
for w in A3:
    e = w*0.33
    list3.append(e)
    sum3 = sum(list3)
    
laplasa.append(sum1)
laplasa.append(sum2)
laplasa.append(sum3)
maxl = max(laplasa)

if laplasa.index(maxl) == 0:
    print("Критерій Лапласа - Обираємо стратегію N=1")
if laplasa.index(maxl) == 1:
    print("Критерій Лапласа - Обираємо стратегію N=2")
if laplasa.index(maxl) == 2:
    print("Критерій Лапласа - Обираємо стратегію N=3")

#Gulcvina
mid1 = (minA1+maxA1)/2
mid2 = (minA2+maxA2)/2
mid3 = (minA3+maxA3)/2

gulcvina.append(mid1)
gulcvina.append(mid2)
gulcvina.append(mid3)
maxg = max(gulcvina)

if gulcvina.index(maxg) == 0:
    print("Критерій Гурвіца - Обираємо стратегію N=1")
if gulcvina.index(maxg) == 1:
    print("Критерій Гурвіца - Обираємо стратегію N=2")
if gulcvina.index(maxg) == 2:
    print("Критерій Гурвіца - Обираємо стратегію N=3")

#Baes-Laplas
for i in P1:
    j = 0
    j = i*0.5
    list11.append(j)
for o in P2:
    q = 0
    q = o*0.35
    list22.append(q)
for w in P3:
    e = 0
    e = w*0.15
    list33.append(e)
    
sum11 = list11[0]+list22[0]+list33[0]
sum22 = list11[1]+list22[1]+list33[1]
sum33 = list11[2]+list22[2]+list33[2]

baes.append(sum11)
baes.append(sum22)
baes.append(sum33)
maxb = max(baes)

if baes.index(maxb) == 0:
    print("Критерій Байеса-Лапласа - Обираємо стратегію N=1\n\n")
if baes.index(maxb) == 1:
    print("Критерій Байеса-Лапласа - Обираємо стратегію N=2\n\n")
if baes.index(maxb) == 2:
    print("Критерій Байеса-Лапласа - Обираємо стратегію N=3\n\n")
    


df = pd.DataFrame({'Можливі альтернативні рішення': ['Продовжити роботу в звичному режимі', 'Активувати рекламну діяльність', 'Активувати рекламу і знизити ціну'],
                   'Конкуренція на тому ж рівні': P1,
                   'Конкуренція трішки посилилась': P2,
                   'Конкуренція різко посилилась': P3,
                   'Вальда': valda,
                   'Максимальний': maximum,
                   'Лапласа': laplasa,
                   'Гульвіца': gulcvina,
                   'Байеса-Лапласа': baes})
print(df)
