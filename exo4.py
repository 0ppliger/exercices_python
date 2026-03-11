# Etant donné un nombre n, affichez
# "Fizz" si le nombre est divisible par 3
# "Buzz" si le nombre est divisible par 5
# "FizzBuzz" si le nombre est divisible par 3 et 5
# Parcourez tous les nombres de 1 à 100

for n in range(1, 101):
    result = ""
    if n % 3 == 0:
        result = result + "Fizz" 
    if n % 5 == 0:
        result = result + "Buzz" 

    print(n, result)