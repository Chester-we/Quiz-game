def quiz_game():
    questions = {
        "What is the capital of France?":{"options":["A)Paris, B)London, C)Mexico, D)Chicago"],
                                          "answer": "A"},

        "Who is he father of physics?":{"options":["A)Nickola Tesla, B)Martin Lutherking, C)Franlkin Roosevelt, D)Isaac Newton"],
                                        "answer": "D"},

        "Which is the biggest fruit? ":{"options":["A)Grape, B)Watermellow, C)Mango, D)Avocado"],
                                        "answer": "B"},
                                        
        "Wha is a whale?":{"options":["A)Reptile, B)Bird, C)Mammal, D)Fish"],
                           "answer": "C"}
    }

    points = 0
    print("welcome to quiz game!")

    for question, details in questions.items():
        print(question)
        for option in details["options"]:
            print(option)

            answer = input(": ")

            if answer == details["answer"]:
                points += 1
                print("Correct!")

            else:
                print(f"Wrong!, the answer is {details['answer']}")

                print(f"You have {points}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()