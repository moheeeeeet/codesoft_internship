import random
import string
print("for random password generation")
def que():
  lenght=int(input("please enter the required lenght of the password"))
  Lowercase=string.ascii_lowercase
  uppercase=string.ascii_uppercase
  numbers=string.digits
  symbols=string.punctuation
  mix=Lowercase+uppercase+numbers+symbols
  pass_word=random.sample(mix,lenght)
  final="".join(pass_word) 
  print(final)
  que()
  

que()