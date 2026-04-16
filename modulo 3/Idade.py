



while True:
 
 idade = int(input('Digite sua idade: '))

 if idade >= 18 and idade < 60:
    print('Você é maior de idade.')
 elif idade >= 14 and idade < 18:
    print('Você é adolescente.')
 elif idade >= 60:
    print('Você é idoso.')
 elif idade <= 0:
    print('Idade invalida, tente novamente.')
 else:
    print('Você é criança.')
 break
 
   

