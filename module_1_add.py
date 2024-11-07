# 1 вариант

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)

a = list(map(sum, grades[0:]))
b = list(map(len, grades[0:]))
average = list(map(lambda x, y: x/y, a, b))
stud_dict = dict(zip(students_sorted, average[0:]))
print(stud_dict)

# 2 вариант

students_dict = dict(zip(students_sorted, grades))
average_score = [sum(i)/len(i) for i in students_dict.values()]
result_dict = dict(zip(students_sorted, average_score))
print(result_dict)

#Первым получился вариант с циклами, конечно все проще. Но решил поупорствовать и наткнулся на функцию map().
#Конечно не уверен, что правильно, относительно полученных знаний в рамках курса.