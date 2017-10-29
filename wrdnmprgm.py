responses = {
    'max': "yay iz frend",
    'caleb': "oof iz perzn",
    'aaron': "oof iz leder",
}

response = input("PICK A NUMBER! NOW! ")
if response == "2":
  death = "u fail biomentric"
  name = input("vas iz u nam: ").lower()
  if name in responses:
      death = responses[name]
else:
  death = "no. die in a pit"

print(death)
