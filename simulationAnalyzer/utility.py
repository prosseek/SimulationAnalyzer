__author__ = 'smcho'

def listToCountList(ls):
    def lastItem(index, ls):
        return index + 1 == len(ls)

    result = []
    if len(ls) <= 1: return ls
    if len(ls) == 2:
        if ls[0] == ls[1]: return [(ls[0],2)]
        else: return [(ls[0],1), (ls[1],1)]

    for index, l in enumerate(ls):
        # first case
        if index == 0:
            prev = l
            count = 1
            continue

        # normal case
        if l == prev:
            count += 1
            if lastItem(index, ls):
                result.append((l, count))
        else: # different one
            if lastItem(index, ls):
                result.append((l, 1))
            else:
                result.append((prev, count))
            count = 1

        prev = l

    return result
