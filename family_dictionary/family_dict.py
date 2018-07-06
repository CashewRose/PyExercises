my_family = {
    'mother': {
        'name': 'Debra',
        'age': '54'
    },
    'father': {
        'name': 'Giancarlo',
        'age': '67'
    }
}

def family():
    for keys in my_family.keys():
        print(f'My family consists of my {keys} who\'s name is {my_family[keys]["name"]}. They are {my_family[keys]["age"]} years old.')

family()