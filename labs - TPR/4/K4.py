import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)
init(autoreset=True) 

with open('phones.txt') as filephone:
    phones = []
    phones = filephone.readlines()
    phones = [line.rstrip('\n') for line in phones]

print(Style.BRIGHT + Fore.BLUE + "Телефони:",*phones,sep="\n")
print("\n")

with open('parameters.txt') as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print(Style.BRIGHT + Fore.BLUE + "Параметри:",*parameters,sep="\n")
print("\n")
print(Style.BRIGHT + Fore.MAGENTA + "Шкала оцінювання: 1-5")
print("\n")

with open('importance.txt') as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (phone):
    price = float(importance[0]) * (float(exp1[phone][0])+float(exp2[phone][0])+float(exp3[phone][0])+float(exp4[phone][0]))
    return price

def Display (phone):
    display = float(importance[1]) * (float(exp1[phone][1])+float(exp2[phone][1])+float(exp3[phone][1])+float(exp4[phone][1]))
    return display

def Design (phone):
    design = float(importance[2]) * (float(exp1[phone][2])+float(exp2[phone][2])+float(exp3[phone][2])+float(exp4[phone][2]))
    return design

def Memory (phone):
    memory = float(importance[3]) * (float(exp1[phone][3])+float(exp2[phone][3])+float(exp3[phone][3])+float(exp4[phone][3]))
    return memory

def Battery (phone):
    battery = float(importance[4]) * (float(exp1[phone][4])+float(exp2[phone][4])+float(exp3[phone][4])+float(exp4[phone][4]))
    return battery

def Camera (phone):
    camera = float(importance[5]) * (float(exp1[phone][5])+float(exp2[phone][5])+float(exp3[phone][5])+float(exp4[phone][5]))
    return camera

def Thick (phone):
    thick = float(importance[6]) * (float(exp1[phone][6])+float(exp2[phone][6])+float(exp3[phone][6])+float(exp4[phone][6]))
    return thick

#iPhone 13 Pro Max
priceIphone = Price(0)
displayIphone = Display(0)
designIphone = Design(0)
memoryIphone = Memory(0)
batteryIphone = Battery(0)
cameraIphone = Camera(0)
thickIphone = Thick(0)

#Samsung Galaxy Z Fold3 F926
priceSamsung = Price(1)
displaySamsung = Display(1)
designSamsung = Design(1)
memorySamsung = Memory(1)
batterySamsung = Battery(1)
cameraSamsung = Camera(1)
thickSamsung = Thick(1)

#HUAWEI Mate Xs Interstellar
priceHuawei = Price(2)
displayHuawei = Display(2)
designHuawei = Design(2)
memoryHuawei = Memory(2)
batteryHuawei = Battery(2)
cameraHuawei = Camera(2)
thickHuawei = Thick(2)

#Xiaomi Mi 11 Ultra
priceXiaomi = Price(3)
displayXiaomi = Display(3)
designXiaomi = Design(3)
memoryXiaomi = Memory(3)
batteryXiaomi = Battery(3)
cameraXiaomi = Camera(3)
thickXiaomi = Thick(3)

#Sony Xperia 1 III 12
priceSony = Price(4)
displaySony = Display(4)
designSony = Design(4)
memorySony = Memory(4)
batterySony = Battery(4)
cameraSony = Camera(4)
thickSony = Thick(4)

#Sum

sumIphone = priceIphone + designIphone + displayIphone + cameraIphone + batteryIphone + thickIphone + memoryIphone
sumSamsung = priceSamsung + designSamsung + displaySamsung + cameraSamsung + batterySamsung + thickSamsung + memorySamsung
sumHuawei = priceHuawei + designHuawei + displayHuawei + cameraHuawei + batteryHuawei + thickHuawei + memoryHuawei
sumXiaomi = priceXiaomi + designXiaomi + displayXiaomi + cameraXiaomi + batteryXiaomi + thickXiaomi + memoryXiaomi
sumSony= priceSony + designSony + displaySony + cameraSony + batterySony + thickSony + memorySony

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', '6', '7', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   phones[0]: [priceIphone, displayIphone, designIphone, memoryIphone, batteryIphone, cameraIphone, thickIphone, sumIphone],
                   phones[1]: [priceSamsung, displaySamsung, designSamsung, memorySamsung, batterySamsung, cameraSamsung, thickSamsung, sumSamsung],
                   phones[2]: [priceHuawei, displayHuawei, designHuawei, memoryHuawei, batteryHuawei, cameraHuawei, thickHuawei, sumHuawei],
                   phones[3]: [priceXiaomi, displayXiaomi, designXiaomi, memoryXiaomi, batteryXiaomi, cameraXiaomi, thickXiaomi, sumXiaomi],
                   phones[4]: [priceSony, displaySony, designSony, memorySony, batterySony, cameraSony, thickSony, sumSony]})

print(Style.BRIGHT + Fore.GREEN + "Результат:")
print(df)
print('\n')

winer = ''
points = ''

if sumIphone > sumSony and sumIphone > sumHuawei and sumIphone > sumSamsung and sumIphone > sumXiaomi:
    winer = phones[0]
    points = sumIphone
elif sumSamsung > sumSony and sumSamsung > sumHuawei and sumSamsung > sumIphone and sumSamsung > sumXiaomi:
    winer = phones[1]
    points = sumSamsung
elif sumHuawei > sumSony and sumHuawei > sumSamsung and sumHuawei > sumIphone and sumHuawei > sumXiaomi:
    winer = phones[2]
    points = sumHuawei
elif sumXiaomi > sumSony and sumXiaomi > sumSamsung and sumXiaomi > sumIphone and sumXiaomi > sumHuawei:
    winer = phones[3]
    points = sumXiaomi
elif sumSony > sumXiaomi and sumSony > sumSamsung and sumSony > sumIphone and sumSony > sumHuawei:
    winer = phones[4]
    points = sumSony
else:
    print("Щось пішло не так при обличсленнях переможця, або переможець не один!")

print(Fore.YELLOW + "Найкращим варіантом вийшов -",winer, '-', points)
print('\n')