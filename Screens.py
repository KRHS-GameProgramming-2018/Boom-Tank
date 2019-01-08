

def showSplash():
    output = ""
    output += "---------------------------------------\n"
    output += "|                                     |\n"
    output += "|              Boom Tank              |\n"
    output += "|                                     |\n"
    output += "|                                     |\n"
    output += "|                                     |\n"
    output += "---------------------------------------\n"



    return output





def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "2" 
            or response == "Two"):
            response = "2"
            goodInput = True
        elif (response == "3"
            or response == "Three"):
            response = "3"
            goodInput = True
        elif (response == "4"
            or response == "Four"):
            response = "4"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True              
        else:
            print "Please make a valid choice boi"
    return response
