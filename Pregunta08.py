time = input("ingrese la hora(HH:MM): ")

hora,minutos = time.split(":")

if(hora <= '24' and minutos <= '60'):
    if(hora == '7' or hora == '8'):
        if(hora == '8' and minutos != '00'):
                print(" ")
        else:
            print("Hora de desayunar")
    
    if(hora == '12' or hora == '13'):
        if(hora == '13' and minutos != '00'):
                print(" ")
        else:
            print("Hora de almorzar")
        
    if(hora == '18' or hora == '19'):
        if(hora == '19' and minutos != '00'):
                print(" ")
        else:
            print("Hora de cenar")





