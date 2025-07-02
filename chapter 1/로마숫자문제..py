# 아라비아 숫자    1   5   10   50   100   500   1000
# 로마 숫자        I   V   X    L    C     D     M

# 로마 숫자는 1~3999 까지만 만등 수 있는데, 이유는 같은 문자를 4개 사용할 수 없기 때문이다.
# 예를 들어 4는 IIII가 아니라 IV로 표현한다.
# 아라비아 숫자를 로마숫자로 표현하는 함수
# 
def int_to_roman(num): 
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syms[i]
            num -= val[i]
    return roman_num    

print(int_to_roman(1))    # I
print(int_to_roman(4))    # IV  
print(int_to_roman(9))    # IX
print(int_to_roman(58))   # LVIII
print(int_to_roman(1994)) # MCMXCIV
print(int_to_roman(3999)) # MMMCMXCIX


result = []
for j in range(1, 4000) :
    result.append(int_to_roman(j))

print(result[10])
print(f'result의 열번째 요소의 길이는 {len(result[10])}입니다.')
    
count = 0 
for k in result :
    if len(k) == 12 :
        count += 1
print(f'로마 숫자의 길이가 12 이상인 경우는 {count}개입니다.')