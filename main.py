from translate import Translator
translator= Translator(to_lang="es")
while True:
   translation = translator.translate(input("What do you want to translate?: "))
   print (translation) 