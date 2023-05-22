with open("life-expectancy.csv") as file:
    next(file)
    max_life_exp = 0
    min_life_exp = float('inf')
    user_year = int(input("\nEnter the year of interest: "))
    max_user_exp = 0
    min_user_exp = float('inf')
    sum = 0
    count = 0
    life_exp_list = []
    import statistics
    for line in file:
        line = line.strip().split(",")
        Entity = line[0]
        Code = line[1]
        Year = int(line[2])
        Life_Expectancy = float(line[3])
        # finding max
        if Life_Expectancy > max_life_exp:
            max_life_exp = Life_Expectancy
            max_country = Entity
            max_year = Year
        # finding min
        if Life_Expectancy < min_life_exp:
            min_life_exp = Life_Expectancy
            min_country = Entity
            min_year = Year
        # finding user year info
        if Year == user_year:
            if Life_Expectancy > max_user_exp:
                max_user_exp = Life_Expectancy
                max_user_country = Entity
            if Life_Expectancy < min_user_exp:
                min_user_exp = Life_Expectancy
                min_user_country = Entity

            life_exp_list.append(Life_Expectancy)
            
            # finding sum
            sum += Life_Expectancy
            
            # finding count
            count += 1
           
            # finding average
user_average = sum/count
# finding standard deviation 
stdv_life_exp = statistics.stdev(life_exp_list)

print(f"\nThe overall max life expectancy is: {max_life_exp} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life_exp} from {min_country} in {min_year}\n")

print(f'''\nFor the year {user_year}:
The average life expectancy across all countries was {user_average:.2f}
The max life expectancy was in {max_user_country} with {max_user_exp}
The min life expectancy was in {min_user_country} with {min_user_exp}
The life expectancy standard deviation for this year was: {stdv_life_exp:.2f}\n''')
      
        
    
