# Código do dev aqui
def sum_numbers(*args):
    return sum(args)

sum_numbers(1, 2, 3, 4, 5, 6)

def get_multiplied_amount(multiplier, *args):
    return sum(args) * multiplier

get_multiplied_amount(2,1, 2, 3)


def word_concatenator(*args):
    return " ".join(args).rstrip()

def inverted_word_factory(*args):
    res = []
    for word in args:
        res.append(word[::-1])
    reversedRes = list(reversed(list(res)))
    return word_concatenator(" ".join(reversedRes))

def dictionary_separator(**kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    return (keys, values)

def dictionary_creator(*change_keys, **user):
    if(len(change_keys) < len(user)):
        return None
    else:
        new_dict = {}
        for index,key in enumerate(user):
            new_dict[change_keys[index]] = user.get(key)
        return new_dict

def purchase_logger(**kwargs):
    return f"Product {kwargs['name']} costs {kwargs['price']} and was bought {kwargs['quantity']}"

def world_cup_logger(country, *year_list):
    year_list = sorted(year_list)
    return f"{country} - {', '.join(str(n) for n in year_list[:-1:])} e {''.join(str(n) for n in year_list[len(year_list)-1::])}"


