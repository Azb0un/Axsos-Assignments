def printInfo(some_dict):
    for key, value_list in some_dict.items():
        print(len(value_list), key.upper())
        for item in value_list:
            print(item)
        print()

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)