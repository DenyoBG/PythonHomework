#1.Принтирайте Вашето име на конзолата:
print("Denis")

#2.Тествайте всички примери от слайдовете до сега.

print(3)
print(3.14)
print(-3.14)
print(3,14)
print(+3.14)

print("♫")
print(10%7) 
print(10//1)

a = 3 
b = a
a = 5 
print(a) 
user_age = 19
print(user_age+18) 
print(user_age>18) 
print(user_age<18) 
print(user_age==18)
#print(user_age=18) 
print(user_age!=18) 
print(user_age>=18)

user_age = 19
user_language = "en"
#if user is adult AND user speaks english:
if user_language=="en" and user_age>=18:
   print("Welcome")

if user_language=="fr" or user_age<=19:
   print("True")

   print(not False)# True
   print(not True)# False

if user_language=="fr" and not user_age>=18: 
   print("False")

#increment user_age with 1
#user_age = user_age+1
user_age+=1

print(user_age)#20 

x=5
x%=3
print(x)

#3. Проверете типа на данните на всеки един от типовете данни, които разгледахме. Използвайте вградената функция type().

if type(x) == bool:
   print(True)# False the type is Integer.

if type(user_language) == bool:
   print(True)# False, the type is String.

if type(x) == int:
   print(True)

#4. Да се присвои стойност 3 на променлива ‘x’ и стойност 10 на променлива наречена ‘y’. Да се запази стойността от x * y в отделна променлива, която да се казва ‘result’. Накрая изходната информация трябва да изглежда: 3 + 10 = 13
x = 3
y = 10
resutl = x+y
resutll = x*y
print(resutl)
print(resutll)

#5. Да се изчисли лицето на триъгълник, като неговата височина е 13.66, а срещуположната страна 245.54 см.
a = 245.54
ha = 13.66
s = a*ha/2
print(round(s))


#6. Фирма, занимаваща се с маркетинг, иска да пази запис с данни на нейните служители. Всеки запис трябва да има следната характе­ристика – първо име, фамилия, възраст, пол (‘м’ или ‘ж’) и уникален номер на служителя (27560000 до 27569999). Декларирайте необходи­мите променливи, нужни за да се запази информацията за един служи­тел, като използвате подходящи типове данни и описателни имена.

first_name1 = "Adam"
last_name1 = "White"
gender1 = "M"
work_number1 = 27560000
result1 = (f"{first_name1} {last_name1} {gender1} {str(work_number1)}")
print(result1)

#7. Декларирайте две променливи, които да са цели числа. Задайте им стойности съответно 5 и 10. Разменете стойностите им и ги отпечатайте.

number1 = 5
number2 = 10
print(number2, number1)

#8. Напишете програма, която за дадени дължина и височина на успоредник, пресмята и отпечатва на конзолата неговия периметър и лице.
a = 15
ha = 15
b = 15
hb = 15
p = 2*(a+b)
s = a*ha==b*hb
print(p)
print(s)


#9. Да се пресметне питагоровата теорема a2 + b2 = c2  при зададени стойности на a, b и c.
a = 3
b = 4
c = 5
result9 = (a**2 + b**2) == c**2
print(result9)

#10. Да се напише програма, която да пресмята лицето на кръг при зададен радиус r. A = π r²
radius = 10
area = 3.14*radius**2
print(area)


#11. Да се напише програма, която пресмята от inches в centimeters. Един inches е 2.54 centimeters.
inches = 6
cm = inches * 2.54
print(cm)