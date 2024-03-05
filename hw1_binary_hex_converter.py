def decimal_to_binary(decimal_number):
    binary_result = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_result = str(remainder) + binary_result
        decimal_number //= 2
    return binary_result

def decimal_to_hexadecimal(decimal_number):
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hex_result = hex_chars[remainder] + hex_result
        decimal_number //= 16
    return hex_result

def main():
    decimal_input = int(input("請輸入一個介於0到255之間的10進位數字: "))

    if 0 <= decimal_input <= 255:
        binary_result = decimal_to_binary(decimal_input)
        hex_result = decimal_to_hexadecimal(decimal_input)

        print(f"十進位數字 {decimal_input} 的二進位表示法為: {binary_result}")
        print(f"十進位數字 {decimal_input} 的十六進位表示法為: {hex_result}")
    else:
        print("輸入數字超出範圍，請輸入0到255之間的數字")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:26:38 2024

@author: jxc
"""

