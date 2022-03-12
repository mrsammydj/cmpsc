paragraph = '''CMPSC 131 - Introduction to Programming Techniques
This course will feature the following information:
Design and implementation of algorithms.  
Structured programming.  
Problem solving techniques.  
Introduction to a high-level language, including arrays, procedures, and recursion.'''

escapeParagraph = '''CMPSC 131 features:\n

\tProblem solving techniques.\n

\tIntroduction to a "high-level" language, including arrays, procedures, and recursion.\n'''

tenHello = 'Hello ' * 10 + '\n'

firstLine = paragraph[0:50:1]

paraLen = len(paragraph)

highLevel = paragraph.find('high-level')



print(paragraph)

print(escapeParagraph)

print(tenHello)

print(firstLine)

print(paraLen)

print(paragraph.replace('.','_PERIOD_'))

print(highLevel)
