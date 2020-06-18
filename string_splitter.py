def string_splitter(a_string):
    """
    Replicates string type's split() method and splits at spaces.
    Takes in `a_string` and returns a list of individual words from the string.
    string_splitter("Hello world") -> ['Hello', 'world']
    """

    new_str = ""
    new_list = []

    for char in a_string:
        if char != " ":
            new_str += char
        else:
            new_list.append(new_str)
            new_str = ""
    new_list.append(new_str)
    return new_list


string_splitter("Hello world")
