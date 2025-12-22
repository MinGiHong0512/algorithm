while True:
    value = input()

    if int(value) == 0:
        break

    asdf = False
    for i in range(len(value) // 2):
        if value[i] != value[len(value)- i - 1]:
            asdf = False
            break
        else:
            asdf = True

    if len(value) == 1:
        asdf = True

    if asdf:
        print("yes")
    else:
        print("no")