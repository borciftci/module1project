words = []
final = []
test = []
terms = []
i = 0
k = 0
m = 0

txt = "No I didn't. Wrote about it in my book. Basically you have only #so many games and I didn't feel sitting feel out a gatwitter.com/i/web/status/1â€¦Xn23At"
blacklist = ["I", "in", "you"]
symbols = ["#"]
x = txt.split(" ")

while i < len(x):
    j = 0
    blacklisted = False

    while j < len(blacklist) and blacklisted == False:
        if blacklist[j] == x[i]:
            blacklisted = True
        j += 1    

    if blacklisted == False:
        words.append(x[i])    
    i += 1  

while k < len(words):
    l = 0
    blacklisted = False
    while l < len(symbols) and blacklisted == False:
        if any(symbols[l] in str for str in words[k]):
            blacklisted = True
        l += 1
    if blacklisted == False:
        final.append(words[k])
    k += 1       

def count(test, c):
    return test.count(c)

while m < len(final):
    y = (final[m].split(" "))
    
    test.append(y[0])
    z = count(test, y[0])

    if (y[0], z-1) in terms:
        terms.remove((y[0], z-1))
        terms.append((y[0], z))
    else:
        terms.append((y[0], z))
    m += 1

print(terms)

