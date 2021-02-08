alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

#Function that handles encoding and decoding text
def caesar(in_text,shift_amount,cipher_direction):
  end_text = ""
  for i in in_text:
    if i in alphabet:
      x = alphabet.index(i)
      if cipher_direction == 'encode':
        new_index = x + shift_amount
      elif cipher_direction == 'decode':
        new_index = x - shift_amount
      new_text = alphabet[new_index]
      end_text += new_text
    else:
      end_text += i
  print(f"The {cipher_direction}d text is {end_text}")

#To contine after one message
should_continue =True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  if direction == 'encode':
    caesar(in_text=text, shift_amount=shift,cipher_direction=direction)
  elif direction == 'decode':
    caesar(in_text=text,shift_amount=shift,cipher_direction=direction)

  result = input("Type 'Yes' to continue or 'No' to exit\n").lower()
  if result == 'no':
    should_continue = False
    print("Thanks!")





  
