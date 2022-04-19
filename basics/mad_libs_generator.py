loop = 1

while (loop < 10):

    # Todas las preguntas que se le realiza al usuario para que las conteste
    noun = input("Selecciona un sustantivo: ")
    p_noun = input("Selecciona un sustantivo en plural: ")
    noun2 = input("Selecciona otro sustantivo: ")
    place = input("Nombra un lugar: ")
    adjective = input("Selecciona un adjetivo (Describe una palabra): ")
    noun3 = input("Selecciona un ultimo sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1
    break