# Детский сад — штаны на лямках
# В продолжение темы детского сада давайте и там что-нибудь автоматизируем.
# За каждым ребёнком закреплён шкафчик и кровать. Номер шкафчика состоит из трёх цифр:

# номер группы в саду;
# номер кроватки закреплённой за ребёнком;
# порядковый номер ребёнка в списке группы.
# Воспитатель просит сделать программу, которая по имени ребенка и номеру его шкафчика формирует «красивую» карточку для личного дела.

# Формат ввода
# В первой строке записано имя ребенка.
# Во второй строке записан номер шкафчика.

# Формат вывода
# Карточка в виде:

# Группа №<номер группы>.
# <номер ребёнка в списке>. <имя ребенка>.
# Шкафчик: <номер шкафчика>.
# Кроватка: <номер кроватки>.

name = input()
numberClosed = int(input())
group = numberClosed // 100
numberChild = numberClosed % 10
bed = numberClosed // 10 % 10
print(
    f'Группа №{group}.\n{numberChild}. {name}.\nШкафчик: {numberClosed}.\nКроватка: {bed}.')
