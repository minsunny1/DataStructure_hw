def notation(base, n):
    if n < base:
        print(num[n], end=' ')
    else:
        notation(base, n//base)
        print(num[n % base], end=' ')


num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num += ['A', 'B', 'C', 'D', 'E', 'F']

number = int(input('10진수 입력-->'))
print('\n2진수:', end=' ')
notation(2, number)
print('\n8진수:', end=' ')
notation(8, number)
print('\n16진수:', end=' ')
notation(16, number)