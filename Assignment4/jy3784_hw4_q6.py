def appearances(s, low, high):

    if (low == high):
        dic = {}

        dic[s[low]] = 1
        return dic


    dic = appearances(s, low + 1, high)
    if (s[low] not in dic):

        dic[s[low]] = 1

    elif s[low] in dic:
        dic[s[low]] = dic[s[low]] + 1

    return dic









