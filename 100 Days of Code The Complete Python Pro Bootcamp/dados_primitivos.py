'''
# #Data Types

#strings

print("Hello"[4])

print("123" + "345")

#Integer

print(123 + 345)

123_456_789

#Float

3.14159

#Boolean

True
False

# exemplo 1 de conversão 

num_char = len(input("qual e o seu nome? "))
new_num_char = str(num_char) 
print("Seu nome tem " + new_num_char + " caracteres") 

# exemplo 2 de conversão

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
result = first_digit + second_digit

print(result)
19
print (3 * (3 + 3) / 3 - 3)


'''
'''
# calculadora de imc

peso = float(input("Digite o seu peso em Kg: "))
altura =float(input("Digite a sua altura m²: "))

imc = peso / (altura ** 2)

print(f"O IMC é: {imc:.2f}")


# Calculo do Imc correto

height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)


# Forma correta

# Recebe a altura e o peso do usuário
altura = input("Digite a sua altura em metros: ")
peso = input("Digite o seu peso em quilogramas: ")

# Seu código abaixo desta linha 👇
peso_como_inteiro = int(peso)
altura_como_float = float(altura)

# Usando o operador de exponenciação **
imc = peso_como_inteiro / altura_como_float ** 2
# ou usando multiplicação e PEMDAS
# imc = peso_como_inteiro / (altura_como_float * altura_como_float)

imc_como_inteiro = int(imc)
print(imc_como_inteiro)

## Lição 2

# Take the current age as input
current_age = int(input("Enter your current age: "))

# Calculate the number of weeks left until age 90
weeks_left = (90 - current_age) * 52

# Output the message with the calculated number of weeks
print(f"You have {weeks_left} weeks left.")

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years_left = 90 - int(age)
weeks_left = years_left * 52

print(f"You have {weeks_left} weeks left.")


'''



