def fizzbuzz(num:int):
    if num % 3 == 0: #Retorna "fizz" se num é divisível por 3 
        return 'fizz'
    elif num % 5 == 0: #Retorna "buzz" se num é divisível por 5
        return 'buzz'
    elif num % 3 == 0 and num % 5 == 0: #Retorna "fizzbuzz" se num é divisível por 
        return  'fizzbuzz'
    else: #Retorna o número se num é divisível por 3
        return num

