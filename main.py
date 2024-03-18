from art import logo
print(logo)
def caesar(text, shift, direction):
  end_text=""
  if direction=="decode":
    shift*=-1
  for i in text:
    if i in alphabet:

      c=alphabet.index(i)
      a=c+shift
      if a>25:
        a=a-26
      b=alphabet[a]
      end_text+=b
    else:
      end_text+=i

  print(f"the {direction} of the text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue=True
while should_continue:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  caesar(text, shift, direction)

  result=input("do you want to continue? yes or no\n").lower()
  if result=='no':
    should_continue=False
    print("goodbye")
