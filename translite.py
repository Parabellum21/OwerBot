from googletrans import Translator


def leng(intext):
    translator = Translator()
    a = translator.translate(intext, dest='sk')
    return a.text



if __name__ == "__main__":

    print(leng("Добрий день друзі"))


