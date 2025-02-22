


weights = [1, 2, 3, 4]  # Example weights in kg
heights = [5, 6, 7, 8]  # Example heights in meters

for weight in weights:
    for height in heights:
        bmi = weight / (height ** 2)  # BMI formula
        print(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}")
