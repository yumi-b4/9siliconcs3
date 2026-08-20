year_birth = int(input("Enter your birth year: "))

if year_birth < 1900:
    print("Invalid input, the year must be 1900 or newer")
else: 
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)" 
    ]

    zodiac_year = (year_birth - 1900) % 12
    zodiac = zodiac_signs[zodiac_year]

    print("Your Chinese Zodiac Sign is:", zodiac)
    