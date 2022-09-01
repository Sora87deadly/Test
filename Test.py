# Test
#Testing python in Termux
from colorama import init
init()
from colorama import Fore, Back, Style

name=input(Back.BLACK+Fore.GREEN+"Имя:")
print(Fore.MAGENTA+"Привет,"+name)
number=18
age=int(input(Fore.GREEN+"Лет:"))
if age == number:
 print(Fore.MAGENTA+name+", тебе:"+str(age))
elif age >= number:
 print(Fore.MAGENTA+'Тебе больше 18 лет:'+str(age)+"лет")
elif age <= number:
print(Fore.MAGENTA+name+", тебе:"+str(age))
elif age >= number:
 print(Fore.MAGENTA+'Тебе больше 18 лет:'+str(age)+"лет")
elif age <= number:
 print(Style.DIM+Back.RED+"Вам не исполнилось 18 лет.\t Приходите после исполнения 18 лет")
else:
 print(Back.YELLOW+Fore.RED+"No command")
verify=input(Fore.GREEN+"Данные верны? -")
if verify == "Да":
 print("Вы прошли верификацию")
elif verify == "Нет":
 print(Style.DIM+Back.YELLOW+Fore.RED+"Вы не прошли верификацию")
else:
print(Style.NORMAL+Back.YELLOW+Fore.RED+"Not verify user")
(((Очень тупая верификация которая в любом случае не остановит программу.)))

what=str(input( Back.BLACK+Fore.GREEN+"Что сделать(-,+,*):"))
a=float(input(Fore.YELLOW+"первое число:"))
b=float(input("второе число:"))
if what == "+":
 result=a+b
elif what == "-":
 result=a-b
elif what == "*":
 result=a*b
print(Style.NORMAL+Back.GREEN+Fore.RED+"Результат:"+str(result))
#тупой калькулятор.

number1=5
social=int(input(Style.NORMAL+Back.BLACK+Fore.GREEN+"Как вам программа от 0 до 5:"))
if  social == number1:
 print("Очень здорово что вы  цените ейо выше 0 на"+Back.WHITE+str(number1))
elif social <= number1:
 print(Back.WHITE+Fore.BLACK+' [<>_<>"]~ You real?\n[<>-<>]~ Ты самый худший оценщик в мире')
elif social >= number1:   print(Style.NORMAL+Back.YELLOW+Fore.BLACK+"\$_$/~\tСупер оценка:"+str(social))
