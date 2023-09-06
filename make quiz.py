# make quiz

print("""

        ████████████████████████████████████████████████
        █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─█
        ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█
        ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀
        
    - in quiz there is four question you can add or remove - 
                    make by || yossefsabry

""")


def start_game():
    guess = []
    count_anwser = 0
    index_option = 0
    for key in questions:
        print("*"*50)
        print(key)
        for j in option[index_option]:
            print(j)
        index_option += 1
        guess_input = str(input("Enter (A, B, C, D): ")).upper().split()
        guess.append(guess_input)
        count_anwser += check_answer(questions.get(key), guess_input)
    score(guess, count_anwser)
    reset_game()


def check_answer(answer, user_input):
    # * here check for the user if answer == guess_input but, @why: i use [0] becuse the output for user_input[["A"]] is like this
    if answer == user_input[0]:
        print("  CORRECT!  ")
        return 1
    else:
        print("  WRONG!  ")
        return 0


def reset_game():
    rest = input(" Do you want to play again (yes,no):")
    if rest == "yes":
        start_game()
    else:
        return False


def score(guess, count_anwser):
    print("*"*50)
    print("- RESULTS -")
    print("*"*50)
    for i in questions.values():
        print("- Answer is :", end=" ")
        print(i, end=" ")
        print()
    for j in guess:
        print("- Your Answer is :", end=" ")
        print(j[0], end=" ")
        print()
    x = (count_anwser / 4) * 100
    print("-  CORRECT:", str(x) + "%")


questions = {"- Who invented python ? ": "A",
             "- when python invented ? ": "B",
             "- Who Is The Best Player In the Word ? ": "C",
             "- Is The Earth Rounder ?  ": "A"
             }

option = [["- A. Guide Van Russon", "- B. Elon Musk", "- C. Andraw Tate", "- D. Yossef Sabry"],
          ["- A. 1992", "- B. 1991", "- C. 1995", "- D. 2004"],
          ["- A. Ronloado", "- B. The Goat", "- C. M.Salah", "- D. Me"],
          ["- A. True", "- B. False", "- C. Not All", "- D. maybe"]]


start_game()
print("*"*50)
print("- Byeee!")
