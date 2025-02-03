#FutureTime.py
#Name:Arturo
#Date:2/2/2025
#Assignment:Future Time Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter hours: ")
  hours = int(hours) 

  
  #Ask user for minutes
  mins = input("Enter mins: ")
  mins = int(mins)

  moreMins = 500

  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60
  futureHours = (currentHour + hours + extraHour) % 24
  print(extraHour)

  print(futureMins)
  #Calculate the time after the user-supplied time has passed.
  strHour = str(futureHours)
  strMin = str(futureMins)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(strHour + ":"+ strMin)

if __name__ == '__main__':
  main()
