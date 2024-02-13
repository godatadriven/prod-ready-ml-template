from context_manager_examples import my_timer

with my_timer("List from a Comprehension Example"):
    list_comprehension = [x for x in range(10_000_000)]

with my_timer("List from a for Loop Example"):
    list_for_loop = []
    for x in range(10_000_000):
        list_for_loop.append(x)