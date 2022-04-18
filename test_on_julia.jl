using DataFrames

x = 5
x^2

x ÷ 3
y = true
y * 2

y
A = [1,2,3]
2 .* A.^2 .+ sin.(A)
@. 2A^2+sin(A)

function sin_bias(x)
    return sin(x) + 1
end

sin_bias.(A)

# 比較大小
## NaN不等於任何數，包括自己
NaN == NaN
[1 NaN] == [1 NaN]
## 所以提供了其他的函式處理
isequal(NaN, NaN) # isequal判定NaN 和 NaN是一樣的
isequal([1 NaN], [1 NaN])

# 數值型別轉換
## T(X) 和 convert(T, X)相等
Int(2.0) == convert(Int, 2.0)
## 不能這樣轉換時回傳 InexactError
Int8(1)
Int8(128)

# round系列
round(1.4)
round(Int, 1.5)
round(-.9)
## 向-inf取整數
floor(1.4)
floor(Int, 1.4)
## 向inf取整數
ceil(1.4)
ceil(Int, 1.4)
## 向0取整數
trunc(1.4)
trunc(-.9)

# 除法系列
## 截斷除法; 商向0近似
10 / 3
div(10, 3)
10 ÷ 3
## 截斷除法; 商向-inf近似
fld(10, 3)
## 同上; 商向ing近似
cld(10, 3)
## 餘數  x == div(x, y)*y + rem(x, y)
rem(10, 3)
rem(-10, 3)
## 模數  x == fld(x, y)*y + mod(x, y)
mod(10, 3)
mod(-10, 3)
## 一口氣回傳商數 & 餘數 | 商數 & 模數
divrem(15, 4)
fldmod(15,2)
## 最大公約數 (greatest common divisor)
gcd
