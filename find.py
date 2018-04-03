def count_smileys(arr):
    import re
    count = 0
    for string in arr:
        print(string)
        if re.match('(:|;)(~|-)?(D|\))', string, flags = 0):
            count += 1
    return count