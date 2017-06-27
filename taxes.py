

taxes = input("How much money, in dollars, did you pull in? >> $")

taxable_income = int(taxes)

def tax_rate(x):
    if taxable_income > 124400:
        bracket_one = taxable_income - 124400
        first_rate = bracket_one * .099
        total_tax_one = first_rate + 353.50 + 167.50 + 10494
        print(f"You owe ${total_tax_one} in state taxes money bucks")
    elif taxable_income <= 124400 and taxable_income > 8400:
        bracket_two = taxable_income - 8400
        second_rate = bracket_two * .09
        total_tax_two = second_rate + 353.50 + 167.50
        print(f"You owe ${total_tax_two} in state income taxes")
    elif taxable_income <= 8440 and taxable_income > 3350:
        bracket_three = taxable_income - 3350
        third_rate = bracket_three * .07
        total_tax_three = third_rate + 167.50
        print(f"You owe ${total_tax_three} in state income taxes this year")
    else:
        bracket_four = taxable_income * .05
        print(f"You owe ${bracket_four} in state income taxes small fry")



tax_rate(taxable_income)
