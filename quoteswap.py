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

def quoteswap(mobyquotes, pridequotes, moby):
    for i in range(len(pridequotes[:1535])):
        moby = moby.replace(mobyquotes[i], pridequotes[i])
    return moby
    
print(quoteswap(mobyquotes, pridequotes, moby))
