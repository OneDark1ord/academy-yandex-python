# Дед Мороз и конфеты
# Настало самое главное событие в детском саду — новогодний утренник.
# Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так,
# чтобы каждому досталось поровну. Напишите для робоняни алгоритм, который поможет распределить конфеты.

# Формат ввода
# В первой строке указано количество детей на утреннике.
# Во второй строке — количество конфет в конфетном отсеке робоняни.

# Формат вывода
# Сначала выведите количество конфет, которое выдано каждому ребенку,
# а затем количество конфет, что осталось в конфетном отсеке.

child = int(input())
candy = int(input())
given = candy // child
b = candy % child
print(given)
print(b)
