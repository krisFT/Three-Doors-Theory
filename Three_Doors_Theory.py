import random

# Simulation function for Monty Hall Problem
def monty_hall_simulation(trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(trials):
        # Randomly place the prize behind one of the doors
        prize_door = random.randint(1, 3)

        # Contestant makes an initial choice
        contestant_choice = random.randint(1, 3)

        # Host opens a door (not the prize door and not the contestant's choice)
        remaining_doors = [door for door in [1, 2, 3] if door != contestant_choice and door != prize_door]
        host_opens = random.choice(remaining_doors)

        # If the contestant switches, they choose the door not initially chosen or opened by the host
        switch_choice = [door for door in [1, 2, 3] if door != contestant_choice and door != host_opens][0]

        # Track wins for switching and staying
        if switch_choice == prize_door:
            switch_wins += 1
        if contestant_choice == prize_door:
            stay_wins += 1

    return switch_wins, stay_wins

# Run the simulation with 100,000 trials
trials = 100000
switch_wins, stay_wins = monty_hall_simulation(trials)

# Display results
print(f"Total Trials: {trials}")
print(f"Switch Wins: {switch_wins} ({(switch_wins / trials) * 100:.2f}%)")
print(f"Stay Wins: {stay_wins} ({(stay_wins / trials) * 100:.2f}%)")
