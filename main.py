def match(words):
    ctr = 0
    lst = []
    for i in words:
        if len(i)>1 and i[0] == i[-1]:
            ctr += 1
            lst.append(i)
    print("List is : ",lst)
    return ctr
count = match(["wow","nice","mum","dad","uncle"])
print(count)


