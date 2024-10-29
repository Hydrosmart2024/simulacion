hábito = 0  

for día in range(5):  
    
    
    if día % 3 == 0:
        hábito -= 1
        print(f"Día {día + 1}: Recaída - hábito reducido a {hábito}")

    else: hábito += 1
    print(f"Día {día + 1}: Hábito reforzado a {hábito}")

print(f"Hábito final después de 5 días: {hábito}")
