#Get two input values
num1 = float(input("Please input a number: "))
num2 = float(input("Please input a second number: "))

#Calculate addition
added_result = num1 + num2

#Calculate subtraction
subbed_result = num1 - num2

#Calculate multiplication
mult_result = num1 * num2

#Calculate division
div_result = num1 / num2

#Calculate modulo
mod_result = num1 % num2

#Sum up the results
print(num1, "+", num2, "=", added_result)
print(num1, "-", num2, "=", subbed_result)
print(num1, "*", num2, "=", mult_result)
print(num1, "/", num2, "=", div_result)
print(num1, "%", num2, "=", mod_result)

sumall = added_result + subbed_result + mult_result + div_result + mod_result
print("The sum of all of these results are", sumall)

#Average of the two numbers
average = added_result / 2
print("The average of", num1, "and", num2, "=", average)
