a = 'A'
b = 2
c = 1.20

string = 'a={nome1}, b={nome2}, c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)