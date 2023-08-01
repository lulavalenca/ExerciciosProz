tomates = True
batatas = False

for dia in range(1, 8):  
    if tomates and not batatas:
        print(f"Regar os tomates - Dia {dia}")
        
        tomates = False
        batatas = True
    else:
        print(f"As batatas já foram regadas ontem - Dia {dia}")
