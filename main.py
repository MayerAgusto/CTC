dic = dict(zip('abcdefghijklmnopqrstuvwxyz',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]))

def complete(key, text):
  if len(text)%len(key) != 0:
    for i in range(len(key) - len(text)%len(key)):
      text+=" "
  return text

def ctc(key, text):
  diccionary= dict()
  
  for n in key:
    diccionary[dic[n]] = []

  for i in range(len(text)):
    diccionary[dic[key[(i)%len(key)]]].append(text[i])

  sorted_dict = dict(sorted(diccionary.items()))

  text_Encrypted = [ ''.join(sorted_dict[i]) for i in sorted_dict.keys()]

  return ''.join(text_Encrypted)
    
def ctc_des(key, text):
  diccionary= dict()
  
  for n in key:
    diccionary[dic[n]] = []
    
  sorted_dict = dict(sorted(diccionary.items()))
  j = 0
  n = len(key)
  for i in sorted_dict.keys():
    sorted_dict[i] = list(text[j:n])
    j=n
    n+=len(key) 

  for k in diccionary.keys():
    diccionary[k] = sorted_dict[k]

  result= ""
  for i in range(len(key)):
    for k in diccionary.keys():
      result += diccionary[k][i]
  return result
    
def main():
  key_value = input("Ingresa la clave: ")
  text_value = input("Ingrese el texto en claro:")
  text_value = complete(key_value, text_value)
  encrypted = ctc(key_value, text_value)
  des_ecrypted = ctc_des(key_value,encrypted)
  print('Mensaje encriptado: ')
  print(encrypted)
  print('Mensaje descifrado: ')
  print(des_ecrypted)
  
main()