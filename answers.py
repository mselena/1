def get_answer(question, answers):
    question= input('')
    answers= {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'пока': 'увидимся'}
    return answers[question]
print(get_answer(1,2))
