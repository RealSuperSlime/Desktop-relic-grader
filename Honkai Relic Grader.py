# Normalization values
normalizations = {
    "cd": 1,
    "be": 1,
    "de_pct": 1.2,
    "hp_pct": 1.5,
    "atk_pct": 1.5,
    "ehr": 1.5,
    "cr": 2,
    "spd": 2.59,
    "ohb": 1.87,
    "err": 3.33,
    "element_dmg": 1.67,
}

# Argenti weights
argenti_weights = {
    "cd": 1,
    "be": 0,
    "de_pct": 0,
    "hp_pct": 0,
    "atk_pct": 0.75,
    "ehr": 0,
    "cr": 1,
    "spd": 1,
    "ohb": 0,
    "err": 0,
    "element_dmg": 1,
    "flat_atk": 0.75,
}

# Argenti base stats
argenti_base_stats = {
    "atk": 1266,
    "hp": 1894,
    "def": 694
}

main_flat_values = {
    "atk": 43.2,
    "hp": 43.2,
    "def": 54
}

# Function to calculate the scores of flat values
def flat_stat_calculate_score(stat, value, base_stat):
    flat_normalization = (1 / (2 * argenti_base_stats[base_stat] * 0.01)) * (64.8 / main_flat_values[base_stat])
    weight = argenti_weights[stat]
    score = weight * flat_normalization * value
    return score



# Function to calculate the score
def calculate_score(stat, value):
    if stat in normalizations and stat in argenti_weights:
        normalization = normalizations[stat]
        weight = argenti_weights[stat]
        score = weight * normalization * value
        return score


# Example usage


stat = "atk_pct"
value = 6.2
if stat in normalizations:
    score = calculate_score(stat, value)
    print(f"The score for {stat} with value {value} is {round(score, 2)}")
elif stat == "flat_atk":
    score = flat_stat_calculate_score(stat, value, "atk")
    print(f"your stat choice was {stat} with a value of {value}, your output score is {round(score, 2)}")
    #print(f"The score for {stat} with value {value} is {round(score, 2)}")
else:
    print ("\n stat-type syntax error")




    
