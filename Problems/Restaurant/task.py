from itertools import product

main_courses_full = zip(main_courses, price_main_courses)
desserts_full = zip(desserts, price_desserts)
drinks_full = zip(drinks, price_drinks)

for (mc, mc_cost), (des, des_cost), (dr, dr_cost) in product(main_courses_full, desserts_full, drinks_full):
    full_cost = mc_cost + des_cost + dr_cost
    if full_cost <= 30:
        print(mc, des, dr, full_cost)
