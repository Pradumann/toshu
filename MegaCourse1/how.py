def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalized()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

print(sentence_maker("how are you"))
        