def integerToRoman(num):
    mapping = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
        ]
    roman = ""
    for m in mapping:
        divisor, letter = m
            # Notice num is now set to remainder from divmod
        quotient, num = divmod(num, divisor)
        roman += quotient*letter
    return roman

print(integerToRoman(32))
