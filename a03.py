### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget, bashir_budget):
    if ali_budget == str or bashir_budget == str:
        return "Not Possible"
    if ali_budget <= 0 or bashir_budget <= 0:
        return "Not Possible"
    
    if ali_budget > bashir_budget:
        highest_factor = ali_budget % bashir_budget
        if highest_factor != 0:
            chocolatePrice = highest_factor
            return chocolatePrice
        else:
            chocolatePrice = bashir_budget
            return chocolatePrice    
    elif ali_budget < bashir_budget:
        highest_factor = bashir_budget % ali_budget
        if highest_factor != 0:
            chocolatePrice = highest_factor
            return chocolatePrice
        else:
            chocolatePrice = ali_budget
            return chocolatePrice
    else:
        chocolatePrice = ali_budget
        return chocolatePrice

#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget, bashir_budget):
    if type(ali_budget) == str or type(bashir_budget) == str:
        return "Not Possible"
    if ali_budget <= 0 or bashir_budget <= 0:
        return "Not Possible"
    
    if type(ali_budget) == float:
        if ali_budget - int(ali_budget) >= 0.50:
            ali_budget = int(ali_budget) + 1
        elif ali_budget - int(ali_budget) < 0.50:
            ali_budget = int(ali_budget)
    elif type(bashir_budget) == float:
        if bashir_budget - int(bashir_budget) >= 0.50:
            bashir_budget = int(bashir_budget) + 1
        elif bashir_budget - int(bashir_budget) < 0.50:
            bashir_budget = int(bashir_budget)
    
    if ali_budget > bashir_budget:
        if ali_budget % bashir_budget != 0:
            chocolate = ali_budget // (ali_budget % bashir_budget)
            ali_revenue = chocolatePrice(ali_budget, bashir_budget) * chocolate * (3 / 2)
            chocolate = bashir_budget // chocolatePrice(ali_budget, bashir_budget)
            bashir_revenue = chocolatePrice(ali_budget, bashir_budget) * chocolate * (2)
        else:
            chocolate = ali_budget // bashir_budget
            ali_revenue = chocolatePrice(ali_budget, bashir_budget) * chocolate * (3 / 2)
            bashir_revenue = chocolatePrice(ali_budget, bashir_budget) * 1 * (2)
    elif ali_budget < bashir_budget:
        if bashir_budget % ali_budget != 0:
            chocolate = ali_budget // (bashir_budget % ali_budget)
            ali_revenue = chocolatePrice(ali_budget, bashir_budget) * chocolate * (2)
            chocolate = bashir_budget // chocolatePrice(ali_budget, bashir_budget)
            bashir_revenue = chocolatePrice(ali_budget, bashir_budget) * chocolate * (3 / 2)
        else: 
            chocolate = bashir_budget // ali_budget
            ali_revenue = chocolatePrice(ali_budget, bashir_budget) * 1 * (2)
            chocolate = bashir_budget // chocolatePrice(ali_budget, bashir_budget)
            bashir_revenue = ali_budget * chocolate * (3 / 2)
     
    ali_profit = ali_revenue - ali_budget
    bashir_profit = bashir_revenue - bashir_budget
    
    if ali_profit > bashir_profit:
        return int(ali_profit)
    else:
        return int(bashir_profit)    



#### End OF MARKER


