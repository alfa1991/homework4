# Создание переменной immutable_var и присвоение ей кортежа из разных типов данных
immutable_var = 1, "hello", 3.14, True
immutable_var_2 =(1, "hello", 3.14, True)
immutable_var_3 = tuple([1, "hello", 3.14, True])
#Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var )
print(immutable_var_2)
print(immutable_var_3)
# Попытка изменения элементов кортежа immutable_var
#immutable_var[0] = 2
#Это приведет к ошибке, так как кортежи являются неизменяемыми структурами данных в Python. Это означает, что после создания кортежа нельзя изменить его элементы.
# Создание переменной mutable_list и присвоение ей списка из нескольких элементов
mutable_list = [1, 2, 3, 4, 5]

# Изменение элементов списка mutable_list
mutable_list[0] = 10
mutable_list[2] = "urban"

# Вывод измененного списка mutable_list на экран
print(mutable_list)