#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Мама', 'Папа', 'Я']


# список списков приблизителного роста членов вашей семьи
my_family_height = [['Мама', 172], ['Папа', 175], ['Я', 182]]
    # ['имя', рост],
    



print('Рост отца -', my_family_height[1][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
family_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моей семьи -', family_height, 'см')
