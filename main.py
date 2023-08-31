#CyHelp Starter Code
cybersecurityBirthYear = 1970



#Greets user
print ("Hello! I'm CyHelp.\n")
userName = input ("What's your name?\n")
print ("\nNice to meet you, " + userName)



#Recounts start of Cybersecurity
todaysYear = input ("What year is it?\n")
timePassed = int(todaysYear) - cybersecurityBirthYear

print ("\nWow! That means it has been " + str(timePassed) + " years since Cybersecurity began.\n")

print ("The field of Cybersecurity started in 1970, when more and more information started being stored on computer systems and networks!\n"
)

input ("Press enter to continue.\n")



#Describes Cybersecurity
print ("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats. These people can be government, nations, companies, community organizations. and individuals.\n"
)

input ("Press enter to continue.\n")



#Introduces CIA Triad
print ("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability. \nWould you like to learn about the CIA triad?\n"
)

giveInfo = input ("Type 'yes' or 'no'.\n")



#Explains pillars of CIA Triad
while giveInfo.lower() == "yes": 

  print ("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) confidentiality \n(b) integrity \n(c) availability \n(d) none")
  
  chosenTopic = input()
  
  if chosenTopic.lower() == "a":
    print ("Confidentiality makes sure data is private.\n")
  
  elif chosenTopic.lower() == "b":
    print ("Integrity makes sure data has not been tampered with and can be trusted.\n")
  
  elif chosenTopic.lower() == "c":
    print ("Availability makes sure authorized people can access the data.\n")
  
  elif chosenTopic.lower() == "d":
    break 
  
  else:
    print ("Sorry, I didn't catch that. Choose one of the options listed.")


#Chatbot ends conversation
print ("\nThanks for chatting with me, and I hope you learned something new!")
