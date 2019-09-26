import datetime
from contextlib import contextmanager


@contextmanager
def open_lib_and_creat_dict(myfile):
    try:
        print(datetime.datetime.now())
        now = datetime.datetime.now()
        file = open(myfile)
        yield file
    finally:
        file.close()
        print(datetime.datetime.now())
        then = datetime.datetime.now()
        delta = then - now
        print(delta.microseconds)

def get_shop_list_by_dishes(menu, dishes, person_count):
    ee = {}
    for name in dishes:
        for ingridient in menu[name.strip()]:
            # ingridient = dict[name]
            # print(ingridient)
            if ingridient['ingridient_name'] in ee.keys():
                ee[ingridient['ingridient_name']]['quantity'] += ingridient['quantity'] * person_count
            else:
                ee[ingridient['ingridient_name']] = {
                    'measure': ingridient['measure'],
                    'quantity': ingridient['quantity'] * person_count
                }
    return ee

def read_you_cbook(name_of_file):
    menu = {}
    with open_lib_and_creat_dict(name_of_file) as f:
        while True:
            title = f.readline().strip()
            # print(type(line))
            if not title:
                break
            menu[title] = []
            num = f.readline()
            n = int(num)

            for i in range(n):
                [ingridient_name, quantity, measure] = f.readline().split('|')
                menu[title].append({
                    'ingridient_name': ingridient_name.strip(),
                    'quantity': int(quantity.strip()),
                    'measure': measure.strip()
                })

            f.readline()

    return menu


def main():
    menu = read_you_cbook('cookbook')

    names = input('введите название блюд').split(',')
    number = int(input('введите колличество гостей'))
    print(menu)

    shop = get_shop_list_by_dishes(menu, names, number)
    print(shop)
    print(datetime.datetime.now())
    then = datetime.datetime.now()
    delta = then - now
    print(delta.microseconds)

if __name__ == '__main__':
    main()
