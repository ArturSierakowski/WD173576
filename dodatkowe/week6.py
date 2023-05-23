# ZADANIE 1
def mystery():
    results = {'sanity': 'Hello'}
    return results


print(mystery())


# ZADANIE 2
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


print(create_array(2))
