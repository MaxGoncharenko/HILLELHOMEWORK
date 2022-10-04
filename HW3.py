'''
Зформуйте строку, яка містить певну інформацію про символ по його індексу в відомому слові.
Наприклад "The [індекс символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
Слово та номер отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
'''



#1

userinput = input('Enter your word:')
num = 0
while num < len(userinput):
    for i in userinput:
        print(f'The {num} symbol in "{userinput}" is {i}')
        num +=1


'''
Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). 
Напишіть код, який визначить кількість слів, в цих даних.
'''

#2

words = input('Enter something:')
res = len(words.split())
print(res)

'''
Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
'''
#3

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum',0.9]

lst2 = []
for i in lst1:
    if type(i) == int or type(i) == float:
        lst2.append(i)
print(lst2)


