# souhait.py

f = open('souhait.txt', 'r')
content = f.read()
newContent = content.replace('Hollande', 'Macron')
f.close()

f2 = open('souhait2.txt', 'w')
f2.write(newContent)
f2.close()
