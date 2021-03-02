"""Print out all the melons in our inventory."""


from melons import nest_melons #my nested dictionary for melon + properties


def print_melon(nest_melons):
    """Print each melon with corresponding attribute information."""
    
    for melon in nest_melons:
        if nest_melons[melon]['melon_seedlessness']:
            print(f"{melon}s have seeds and are ${nest_melons[melon]['melon_prices']}")
        else: 
            print(f"{melon}s do not have seeds and are ${nest_melons[melon]['melon_prices']}")

#def print_melons(nest_melons):
    #for melons in nest_melons:
        #print("nest_melons[melons])