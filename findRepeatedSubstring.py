def solution(s):
    # Your code here
    if len(s) == 0:
        return 0

    subString = s[0]
    count = 1
    done = False
    comparing = ""
    i = 0

    while not done:
        print("substring:",subString)
        print("count",count)
        i += 1
        comparing = s[i*len(subString):i*len(subString)+len(subString)]
        print("comparing:",subString,"to",s[i*len(subString):i*len(subString)+len(subString)])
        if subString == comparing:
            count += 1
        else:
            subString = s[0:len(subString)+1]
            count = 1
            i = 0
        if len(s) / len(subString) == count:
            done = True

    print(subString)

    if (len(s) == len(subString)):
        return 1

    return count


print(solution("aaaabaaaab"))
