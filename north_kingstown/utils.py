# calculates price of a single drink (ome ounce/shot)

# example: jim beam orange
# bottle mls: 1 liter
# bottle price: $23.75
# pour cost percent: 14%
# shrinkage percent: 20%
# garnish: 50 cents
# final drink cost: $6.50


MLS_TO_OZS_CONVERSION = 29.6
ROUNDED_DIGITS = 2

bottle_mls = 1000
bottle_price = 23.75

pour_cost_percent = 0.14
shrinkage_percent = 0.2
garnish = 0.5


def convert_mls_to_ozs(bottle_mls: int) -> float:
    return round(bottle_mls / MLS_TO_OZS_CONVERSION, ROUNDED_DIGITS)


def calculate_liquor_cost_per_oz(bottle_price: float, bottle_ozs: float) -> float:
    return round(bottle_price / bottle_ozs, ROUNDED_DIGITS)


def calculate_drink_cost(liquor_cost_per_oz, pour_cost_percent: int) -> float:
    return round(liquor_cost_per_oz / pour_cost_percent, ROUNDED_DIGITS)


def calculate_shrinkage_cost(drink_cost: float, shrinkage_percent: float) -> float:
    return round(drink_cost * shrinkage_percent, ROUNDED_DIGITS)


def calculate_final_drink_cost(drink_cost: float, shrinkage_cost: float, garnish) -> float:
    return f'${drink_cost + shrinkage_cost + garnish:.2f}'


def main():
    bottle_ounces = convert_mls_to_ozs(bottle_mls)
    liquor_cost_per_ozs = calculate_liquor_cost_per_oz(bottle_price, bottle_ounces)
    drink_cost = calculate_drink_cost(liquor_cost_per_ozs, pour_cost_percent)
    shrinkage_cost = calculate_shrinkage_cost(drink_cost, shrinkage_percent)
    print(calculate_final_drink_cost(drink_cost, shrinkage_cost, garnish))


if __name__ == '__main__':
    main()
