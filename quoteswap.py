import re

# open PG text of Moby Dick and take a slice of only the text
source = open('mobydick.txt')
moby = source.read()
source.close()
moby = moby[12773:]

# open PG text of Pride and Prejudice and take a slice of only the text
source = open('pride.txt')
pride = source.read()
source.close()
pride = pride[629:]

# isolate the quotes in both Moby Dick and Pride and Prejudice into their own variables
mobyquotes = re.findall('"[^"]*\r\n\r\n|"[^"]*"', moby)
pridequotes = re.findall('"[^"]*\r\n\r\n|"[^"]*"', pride)

def quoteswap(quotes1, quotes2, text1):
    for i in range(len(quotes2[:1535])):
        text1 = text1.replace(quotes1[i], quotes2[i])
    return text1
    
# if you want to replace the quotes in Moby Dick with the quotes in Pride and Prejudice
print(quoteswap(mobyquotes, pridequotes, moby))
# if you want to replace the quotes in Pride and Prejudice with the quotes in Moby Dick
print(quoteswap(pridequotes, mobyquotes, pride))
