def tours():
    tour = 0  
    for i in range(1, 13):  
        result = tour + 2  
        print(f"Tour {i} : {result}")
        tour = result 
print(tours())

