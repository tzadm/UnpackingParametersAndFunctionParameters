# 1
def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(c=False)
print_params(c=True, a=34, b=6)
print_params(a=43, c='string')
print_params(a='efihs')

print_params(b=25)
print_params(c=[1, 2, 3])

# 2
values_list = ['string', 87686, (5, 6, 7)]
values_dict = {'a': 677, 'b': "word", 'c': 686}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [123, 'string']
print_params(*values_list_2, 42)
