'''val = 5
if val % 2 == 0:

    print("The value is even")

else:

    print("The value is odd")

for i in range(10):
    print("yo")'''

n1 = 0
n2 = 1
count = 0

print("Fibonacci sequence up to 10:")
while count < 10:
       print(n1, end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

def doubleNumber(number):

    number *= 2

    return number

print(doubleNumber(3))

j = 3

while j < 20:

    print(j, "Tripled= ", j*3)

    j += 3

sentence = "Hi my name is Sam"
def first_word(sentence):

    first = sentence.split()[0]
    return first

first = first_word(sentence)
print(first)

