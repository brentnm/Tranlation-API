from translate import Translator
translator= Translator(to_lang=input("Type in 'es' for spanish, 'pt' for portuguese, or 'zh' for chinese: "))
while True:
   translation = translator.translate(input("What do you want to translate?: "))
   print (translation) 