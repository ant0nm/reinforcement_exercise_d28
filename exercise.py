def cardinal_to_ordinal(num):
    ordianl_indicator = None
    quotient_10 = num // 10
    remainder_10 = num % 10
    if quotient_10 == 1:
        ordianl_indicator = "th"
    else:
        if remainder_10 == 1:
            ordianl_indicator = "st"
        elif remainder_10 == 2:
            ordianl_indicator = "nd"
        elif remainder_10 == 3:
            ordianl_indicator = "rd"
        else:
            ordianl_indicator = "th"
    num_string = str(num) + ordianl_indicator
    return num_string

# test it out
for num in range(1, 101):
    print("*", num, cardinal_to_ordinal(num))

# Examples
# 1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th
# 11th 12th 13th 14th 15th 16th 17th 18th 19th 20th
# 21st 22nd 23rd 24th 25th 26th 27th 28th 29th 30th
# 31st 32nd 33rd 34th 35th 36th 37th 38th 39th 40th
# and so on ...
