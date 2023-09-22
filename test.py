def revText(demostr):
    file = open('demo.txt', 'w')
    file.write(demostr)
    file.close()
    newFile = open('demo.txt', 'r')
    txt = newFile.read()
    print(txt)

    list = txt.split()
    print(list)
    ans = ""
    for word in list:
        if (word[0] == txt[0]):
            word = ''.join(reversed(word))
        ans +=  word + " "

    print(ans)
    


revText("INDIA IS MY COUNTRY")