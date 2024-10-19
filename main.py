def sentence_maker(phrase):
    cap = phrase.capitalize()
    if phrase.startswith(('how' , 'why' , 'what')):
        return f"{cap}?"
    else:
        return f"{cap}"


result = []

while True:
    user_input = input("say something:  ")
    if user_input == '\end':
        break
    else:
        result.append(sentence_maker(user_input))

a = "\n".join(result)
print(a)  