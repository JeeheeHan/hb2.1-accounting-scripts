melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

nest_melons = {}
for names in melon_names.values():
    nest_melons[names] = {}
    for n in melon_prices.values():
        nest_melons[names]['melon_prices'] = n
        for seeds in melon_seedlessness.values():
            nest_melons[names]['melon_seedlessness'] = seeds


print(nest_melons)




