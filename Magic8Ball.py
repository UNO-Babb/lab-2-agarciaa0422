#Magic8Ball.py
#Name:Arturo
#Date:2/2/2025
#Assignment:Magic 8 Ball Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["Yes", "It is certain", "It is decidedly so", "Without a doubt", 
           "Yes, Definitely", "You may rely on it", "As I see it, yes", "Most Likely", 
           "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", 
           "No", "Very doubtful", "Cannot predict now", "Signs point to Yes", 
           "Outlook good", "Reply hazy, try again", "Outlook not so good", "My sources say no"]
  #Answer question randomly with one of the options from your earlier list.
length = len(answers)
r = random.random() * length

r= int(r)

print(r)
response = answers[r]
print(response)

if __name__ == '__main__':
  main()
