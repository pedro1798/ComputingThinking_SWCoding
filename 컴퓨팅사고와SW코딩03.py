"""
섭씨온도(Celsius)를 화씨온도(Fahrenheit)로 변환하는 식은 아래와 같다.
Fahrenheit = (9/5) * Celsius + 32 이 식을 바탕으로 섭씨온도를 0도에서
50도까지 5도 단위로 증가시키면서 이에 해당하는 화씨온도를 계산하여,
섭씨온도와 화씨온도의 값을 보여주는 프로그램을 작성하시오.
"""
for i in range(0,51,5): # i는 섭씨온도
    fahrenheit = (9/5) * i + 32
    print(f"Fahrenheit : {fahrenheit}\nCelsius : {i}")

# a = 2 * 2 // 2  -> 2 곱하기 2 나누기 2의 몫이므로 2
# b = 3 // 2 * 3 -> 3 // 2의 몫은 1, 1 * 3 = 3 이므로 3
# 2 3

"""
10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 
이들의 총합은 23이다. 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하시오.
"""
sum = 0;
for i in range(3, 1000):
    if i % 3 == 0:
        sum += i
for j in range(5,1000):
    if j % 5 == 0:
        sum += j
for k in range(15, 1000):
    if k % 15 == 0:
        sum -= k
print(sum)
