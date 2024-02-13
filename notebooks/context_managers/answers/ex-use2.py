from context_manager_examples import looking_glass

with looking_glass() as what:
    print('hello')
    print(what)