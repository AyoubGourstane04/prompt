def calculate_average(numbers_list):
        """Calculate the average of a list of numbers, handling invalid inputs."""
        total = 0
        valid_count = 0
        
        for num in numbers_list:
            if isinstance(num, (int, float)):  # Vérification du type numérique
                total += num
                valid_count += 1
            else:
                print(f"Avertissement : '{num}' ignoré (non numérique)")
        
        if valid_count == 0:
            raise ValueError("La liste ne contient aucun nombre valide.")
        
        return total / valid_count

# Exemple d'utilisation
my_nums = [1, 2, 'three', 4] 
avg = calculate_average(my_nums)
print(f"Moyenne : {avg}")

