# Шарики и ручки
# Иногда ребята в детском саду скучают, поэтому они постоянно придумывают себе не очень сложные,
# но веселые, по их мнению, игры.
# В группе есть ящик с шариками, количество которых детям заранее неизвестно, следующих цветов:

# красный;
# зеленый;
# синий.
# Игра заключается в том, что каждый ребенок подходит к ящику и, не глядя, вытаскивает один шарик,
# победителем считается тот, кто первым вытащит зелёный шарик.
# Как вы думаете, через какое максимальное количество ходов дети выяснят победителя игры?

# Формат ввода
# Три натуральных числа, каждое на новой строке (количество красных, зеленых и синих шаров соответственно).

# Формат вывода
# Одно число — максимальное количество ходов, которое потребуется для определения победителя.

red = int(input())
geen = int(input())
blue = int(input())
print(red + blue + 1)
