def count_lowercase(s, low, high):

    letter = None

    if (low == high):
        if s[low].isupper() == True:
            return 0
        else:
            return 1

    if s[low].isupper() == True:
        letter = 0
    else:
        letter = 1

    return letter + count_lowercase(s, low + 1, high)


def is_number_of_lowercase_even(s, low, high):

    letter = None

    if (low == high):
        if s[low].isupper() == True:
            return True
        else:
            return False

    even = is_number_of_lowercase_even(s, low + 1, high)

    if s[low].isupper() == True:
        return even
    else:
        return not even








