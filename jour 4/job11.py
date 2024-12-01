def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60  
        reste_minutes = minutes % 60 
        print(f"{heures} heures et {reste_minutes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif pour les minutes.")


print(time_to_text(125))  
print(time_to_text(45))   
print(time_to_text(0))    
print(time_to_text(-10))  
print(time_to_text(150))

