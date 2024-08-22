class compute_cost:
    x_train = 0
    y_train = 0
    total_cost = 0
    initial_w = 0
    initial_b = 0
    
    compute_cost(x_train, y_train, initial_w, initial_b):
        x_train = 12
        y_train = 8
        initial_w = 2
        initial_b = 2
        cost = x_train + y_train * ((initial_w / initial_b))
        return cost


cost = compute_cost(x_train, y_train, initial_w, initial_b)
print(type(cost))
print(f'Cost at initial w: {cost:.3f}')

