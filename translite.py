from googletrans import Translator


def leng(intext, mova):
    translator = Translator()
    a = translator.translate(intext, dest=mova)
    return a.text



if __name__ == "__main__":

    print(leng("Добрий день друзі","ru"))
