def project_population(initial_population, growth_rate, years):
    
    # # Predicts the population after a given number of years. # #
    ##############################################################
    # Arguments 
    # initial_population: Initial population of the city
    # growth_rate: Annual growth rate (in decimal form, e.g., 0.03 for 3% growth)
    # years: Number of years to project
    # Returns:
    # Projected population after the specified number of years.
    
    projected_population = initial_population * (1 + growth_rate) ** years
    return projected_population

def main():
    initial_population = 7719  # Population of Emmett, Idaho in 2020
    growth_rate = 0.0231  # Average annual growth rate (2.31%)
    years = 20
    
    projected_population = project_population(initial_population, growth_rate, years)
    print(f"Projected population in {years} years: {projected_population:.0f}")

if __name__ == "__main__":
    main()
