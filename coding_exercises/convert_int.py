def convertRomanToInt(s):

    d  = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    x = 0
    total = 0
    while(x < len(s)):
        try:
            if(s[x] == 'I' and s[x+1] == 'V' or s[x] == 'I' and s[x+1] == 'X'):
                num = d[s[x+1]] - d[s[x]]
                total += num
                x += 2

            elif(s[x] == 'X' and s[x+1] == 'L' or s[x] == 'X' and s[x+1] == 'C' ):
                num = d[s[x+1]] - d[s[x]]
                total += num
                x += 2

            elif(s[x] == 'C' and s[x+1] == 'D' or s[x] == 'C' and s[x+1] == 'M'):
                num = d[s[x+1]] - d[s[x]]
                total += num
                x += 2

            else:
                num = d[s[x]]
                total += num
                x += 1

        except IndexError:
                num = d[s[x]]
                total += num
                x += 1

    return total

print(convertRomanToInt(input("Enter a Roman Numeral")))

        

