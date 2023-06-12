from python3.translate2 import Translator

translator = Translator(from_lang="Russian", to_lang="English")
result = translator.translate("Привет")
print(result)