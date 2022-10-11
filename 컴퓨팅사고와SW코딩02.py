base = int(input('정사각형의 밑변을 입력하시오 : '))
print(base * base,'\n')

#fahrenheit = (9/5) * celsius + 32
cel = int(input('섭씨온도를 입력하세요 : '))
print(f'섭씨 {cel}는 화씨 {(9/5 * cel + 32)}도 입니다.\n')

print(2<<0, 2<<1, 2<<2, 2<<3,2<<4,2<<5,2<<6,2<<7,2<<8,2<<9,'\n')

integer = int(input('정수를 입력하세요 : '))
print('이 수가 짝수인가요? ', end='')
if(integer % 2 == 0):
    print('True \n')
else:
    print('False \n')

td = int(input('세 자리 정수를 입력하세요 : ')) # 342
n1 = td // 100 # 3
n2 = td // 10 - 10 * n1 # 34
n3 = td - (100 * n1 + 10*n2)
print(f'백의 자리 : {n1}\n십의 자리 : {n2}\n일의자리 : {n3}')