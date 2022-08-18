def find_not_repeating_character(string):
    fail = []
    result = []

    for i in range(len(string)):
        err = 0
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                err += 1
                fail.append(string[i])
        if err == 0 and string[i] not in fail:
            result.append(string[i])

    if result:
        return result[0]
    else:
        return "_"
