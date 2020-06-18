def search_for_string(alist, astring):
    """
    Takes a list of strings `alist` and a string `astring`. Returns a list of all the indices
    at which the string is found.
    """

    indices_list = []
    for i in range(len(alist)):
        if astring == alist[i]:
            indices_list.append(i)
    return indices_list


# example
sample_list = [
    "artichoke",
    "turnip",
    "tomato",
    "potato",
    "turnip",
    "turnip",
    "artichoke",
]
print(search_for_string(sample_list, "turnip"))
