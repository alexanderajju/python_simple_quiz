from Question import Question

questions_prompts = [

    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Red/Green\n(b) Yellow\n(c) Orange\n\n",
    "What color are Orange?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"

]

questions = [Question(questions_prompts[0], "a"), Question(
    questions_prompts[1], "b"), Question(questions_prompts[2], "c")]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got "+str(score) + "/" + str(len(questions)) + " correct")
    print("Total Score: " + str(score*10))


run_test(questions)
