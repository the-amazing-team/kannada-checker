from translate import Translator

FROM_LANG = "kn-IN"
TO_LANG = "en"

translator = Translator(from_lang=FROM_LANG, to_lang=TO_LANG)

sentence = "ನಾನು ನಿಮ್ಮನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ"

translation = translator.translate(sentence)
print(translation)
