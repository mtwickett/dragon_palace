from math import ceil


VALUES = {
    'mls_ozs_conversion': 29.6,
    'rounded_digits': 2,

}


def convert_mls_to_ozs(mls: int) -> float:
    return round(mls / VALUES['mls_ozs_conversion'], VALUES['rounded_digits'])


def get_liquor_cost_per_ounce(wholesale_price: float, ounces: float) -> float:
    return round(wholesale_price / ounces, VALUES['rounded_digits'])


def get_drink_cost(liquor_cost_per_ounce, multiplier=5) -> float:
    return round(liquor_cost_per_ounce * multiplier, 2)


def get_shrinkage_cost(drink_cost: float, percent=0.2) -> float:
    return round(drink_cost * percent, 2)


def get_final_cost(drink_cost: float, shrinkage_cost: float, garnish_cost=0) -> float:
    return ceil((drink_cost + shrinkage_cost + garnish_cost) * 4) / 4


def main():
    ounces = convert_mls_to_ozs(1000)
    liquor_cost_per_ounce = get_liquor_cost_per_ounce(23.75, ounces)
    drink_cost = get_drink_cost(liquor_cost_per_ounce)
    shrinkage_cost = get_shrinkage_cost(drink_cost)
    total_cost = get_final_cost(drink_cost, shrinkage_cost)
    print(total_cost)


if __name__ == '__main__':
    main()
