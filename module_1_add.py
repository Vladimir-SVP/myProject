grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
a = dict(zip(students_sorted, grades))
sum1 = [sum(i) for i in a.values()]
b = dict(zip(students_sorted, sum1))
print(b)
