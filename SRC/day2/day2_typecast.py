# Typecasting examples
num = 3.14
complex_num = complex(num)
print("Original number:", num)
print("Complex number:", complex_num)

# Converting complex to integer (taking the real part)
complex_num = 2 + 3j
int_num = int(complex_num.real)
print("Original complex number:", complex_num)
print("Integer part:", int_num)
