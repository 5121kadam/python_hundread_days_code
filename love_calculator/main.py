def calculate_Love_Score(name1,name2):
    combined_string = name1 + name2
    t1 = 0
    t2 = 0
    for char in combined_string:
        if char == "t" or char == "r" or char == "u" or char == "e":
            t1 += 1
        if char == "l" or char == "o" or char == "v" or char == "e":
            t2 += 1
    love_score = int(str(t1) + str(t2))
    return love_score

def main():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    love_score = calculate_Love_Score(name1,name2)
    print(f"Your love score is {love_score}")

if __name__ == "__main__":
    main()