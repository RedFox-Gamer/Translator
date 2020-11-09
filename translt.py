#pip install translate
from translate import Translator

translator = Translator(from_lang = 'English', to_lang = 'Hungarian')
#Text that you want to translate
result = translator.translate('I love you')
print(result)