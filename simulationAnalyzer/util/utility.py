import glob
import os

__author__ = 'smcho'

def listToCountList(ls):

    result = []
    if len(ls) <= 1: return ls

    prev = None
    count = 1
    for l in ls:
        if l == prev:
            count += 1
        else: # different one
            if count == 1: result.append(prev)
            else: result.append((prev, count))
            count = 1
        prev = l

    if ls[-1] == ls[-2]:
        result.append((l, count))
    else:
       result.append(l)

    return result[1:]

# def getJsonFilesInDirectory(directory):
#     result = []
#     files = glob.glob(directory + os.sep + "*.json")
#     for file in files:
#         file_name = file.split(os.sep)[-1]
#         result.append((file_name, file))
#     return result
