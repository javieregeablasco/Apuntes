# # Sort a list of tuples by the second element
# tuples_list = [(1, 3), (2, 1), (3, 2)]
# sorted_list = sorted(tuples_list, key=lambda x: x[1])
# print("Sorted List of Tuples:", sorted_list)


 

# (lambda a, b, c=3: print(a + b + c))(1, 2)


# (lambda *args: print(sum(args)))(1, 2, 3) 
# (lambda **kwargs: print(sum(kwargs.values())))(a=1, b=2, c=3) 


def calc_factorielle(nb):
    if nb == 1:
        return 1
    else:
        return nb * calc_factorielle(nb - 1)

# Programme principal.
print(calc_factorielle(4))