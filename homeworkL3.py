#1. Принтирайте следният текст на екрана:“23 4.5 False John”.
int1 = 23
int2 = 4.5
int3 = int1<=int2
first_name1 = "John"
print(f"{int1} {int2} {int3} {first_name1}")

#2. Попълнете празните полета, като използвате форматиращият метод format. Празните места запълнете с вашето име и любими активности.

my_name = "Denis"
sport = "Football"
program_lang = "Python"
print(f"{my_name}'s favorite sports is {sport}." "\n"f"{my_name} is working on {program_lang} programming!")

#3. Създайте променлива, paragraph, която да съдържа следното съдържание:"Python is a great language!", said Fred. "I don't ever remember having this much fun before. "
paragraph1 = "Python is a great language"
paragraph2 = "I don't ever remember having this much fun before."
print(f"{paragraph1}, said Fred.", f"{paragraph2}")

#4. Създайте стринг, който да се казва school и да съдържа името на вашето училище. Използвате методите, които научихте за да промените стринга. Ако е необходимо използвайте help функцията.
school = "neofit rilski high school"
#school = school.title()
#print(school)
school2 = school.replace("neofit rilski high school", "Neofit Rilski High School")
print(school2)

#5 Създайте стринг, който да се казва country и присвоете на него стойност “usa”. Създайте нов стринг, correct_country, чиято стойност да е държавата само с големи букви, като използвате някой от стринг методите.
country = "usa"
correct_country = country.upper()
print(correct_country)

#6 Създайте стринг,  filename и му присвоете стойност “hello.py”. Проверете дали стринга завършва на “.java”. Намерете индексът на ”py”. Проверете и дали думата започва с ”world”.
filename = "hello.py"
print(filename.endswith(".java"))

print(filename.find("py"))
print(filename.startswith("world"))

#7 Опитайте се да принтирате стринг изцяло с главни букви.
upper_case_string_only = "My name is Denis."
upper_case_string_only1 = upper_case_string_only.upper()
print(upper_case_string_only1)

#8 Напишете програма, която да премахва ”$$” от името ”$$John Smith”. Опитайте с .lstrip и .strip(). За да видите описанието на двете функции използвайте следното help(“ ”.strip).
first_name8 = "$$John"
last_name8 = "Smith"
print(first_name8.strip("$$"), last_name8)

#9  Да се напише програма, която да принтира следната информация:
string9 = "Coding Temple, Inc."
string10 = "283 Franklin St."
string11 = "Boston, MA"
string12 = "Thank you for shopping with us today!"
product_price = "Product Price"
books_price = "$49.50"
computer_price = "$579.99"
monitor_price = "#124.89"
total1 = "Total"
total2 = "$754.83"
print("******************************")
print(f"{string9:>24}\n{string10:>21}\n{string11:>15}")
print("==============================")
print(f"Product Name{product_price:>15}")
print(f"Books{books_price:>15}")
print(f"Computer{computer_price:>13}")
print(f"Monitor{monitor_price:>14}")
print("==============================")
print(f"{total1:>19} \n{total2:>21}")
print("==============================")
print(f"\n{string12:>10}")
print("\n******************************")


