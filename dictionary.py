kwords = "test","tone","syntax","gui","user","dictionary"

for i in range(10):
 word = input('Search a Word...')
 print("Searched for " + word)
 if word in kwords:
  print("Found Results")
 else:
  print("No results found")
 if word == "test":
  print("Using something for the first time")
 if word == "tone":
  print("A piece of a sound")
 if word == "syntax":
  print("A spelling / The way a word is mentioned")
 if word == "gui":
  print("A graphical interface that's used")
 if word == "user":
  print("A person that is using a object")
 if word == "dictionary":
  print("A atlas / book that has the meanings of words")
  
