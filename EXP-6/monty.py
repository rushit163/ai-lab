import random

def monty_hall_sim(switch=True, trials=1000):
    wins = 0
    for _ in range(trials):
        car, choice = random.randint(1, 3), random.randint(1, 3)
        if switch:
            choice = [d for d in range(1, 4) if d != choice and d != car][0]
        wins += choice == car
    return (wins / trials) * 100

switch_wins = monty_hall_sim()
no_switch_wins = monty_hall_sim(switch=False)
print(f"With switching: {switch_wins:.2f}%")
print(f"Without switching: {no_switch_wins:.2f}%")
