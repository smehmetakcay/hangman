print("CALCULATE YOUR LOVE WITH YOUR NAMES! IF YOU CAN'T SCORE WELL, FIND SOMEONE ELSE!")
name1 = input("What is your name? ")
name2 = input("What is your partner's name? ")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lover_names = combined_names.lower()

    t = lover_names.count("t")
    r = lover_names.count("r")
    u = lover_names.count("u")
    e = lover_names.count("e")

    total_true = t + r + u + e

    l = lover_names.count("l")
    o = lover_names.count("o")
    v = lover_names.count("v")
    e = lover_names.count("e")

    total_love = l + o + v + e

    love_score = int(str(total_true) + str(total_love))
    new_love_score = love_score * 2
    # print(new_love_score)

    if new_love_score > 50:
        if new_love_score > 100:
            new_love_score = 100
        print(f"SUCCESS! You love score is {new_love_score}%!")
    else:
        print(f"Your love score is {new_love_score}%! FIND SOMEONE ELSE!")

calculate_love_score(name1,name2)