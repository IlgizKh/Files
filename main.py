

from pprint import pprint

with open('recipes.txt', 'rt',  encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline().strip())
        dish = []
        for _ in range(ingredients_count):
            name, qty, meas = file.readline().strip().split(' | ')
            dish.append({
                'ingredient_name': name,
                'quantity': qty,
                'measure': meas
            })
        file.readline()
        cook_book[dish_name] = dish

    pprint(cook_book, sort_dicts=False)
    print('\n')
def get_shop_list_by_dishes(dishes, person_count):
   full_ingr = {}
   sum = 0
   for dish_from in dishes:
      for dish_name, ingr in cook_book.items():
          if dish_name == dish_from:
             for ingr_1 in ingr:
                 if ingr_1['ingredient_name'] in full_ingr.keys():
                     full_ingr[ingr_1['ingredient_name']]['quantity'] += int(ingr_1['quantity'])*person_count
                 else:
                  full_ingr[ingr_1['ingredient_name']] = {'measure': ingr_1['measure'],'quantity': int(ingr_1['quantity'])*person_count}

   return full_ingr

pprint (get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5))

list_files = []
list_count = []
with open('1.txt', 'rt',  encoding='utf-8') as file:
    count1 = 0
    text1 = ''
    dict1 ={}
    for line in file:
        text1 +=line
        count1 += 1
    list_files.append([file.name, text1])
    list_count.append(count1)
with open('2.txt', 'rt', encoding='utf-8') as file:
    count2 = 0
    text2 = ''
    dict2 = {}
    for line in file:
        text2 += line
        count2 += 1
    list_files.append([file.name, text2])
    list_count.append(count2)
with open('3.txt', 'rt', encoding='utf-8') as file:
    count3 = 0
    text3 = ''
    dict3 = {}
    for line in file:
        text3 += line
        count3 += 1
    list_files.append([file.name, text3])
    list_count.append(count3)

    list_all = zip(list_count, list_files)
    list_all_s = sorted(list_all)

with open ('4.txt', 'a', encoding='utf-8') as file:
    for count, list in list_all_s:
        file.write(list[0])
        file.write('\n')
        file.write(str(count))
        file.write('\n')
        file.write(list[1])
        file.write('\n')