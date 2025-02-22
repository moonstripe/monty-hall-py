import random


def simulate_monty_hall(n: int, strategy: str) -> float:
    """
    Simulates n iterations of the monty hall game.

    Args:
        n: number of games to simulate
        strategy: whether to 'switch' or 'stay'

    Returns:
        win rate as percentage
    """
    if strategy not in ["switch", "stay"]:
        raise ValueError("Strategy must be either 'switch' or 'stay'")

    wins = 0

    for _ in range(n):
        # Setup the game
        doors = [0, 1, 2]  # 0, 1, 2 represent the door numbers
        car = random.choice(doors)  # Place car behind random door

        # Initial player choice
        initial_choice = random.choice(doors)

        # Monty reveals a goat
        available_for_reveal = [
            door for door in doors if door != initial_choice and door != car
        ]
        revealed_door = random.choice(available_for_reveal)

        # Make final choice based on strategy
        if strategy == "stay":
            final_choice = initial_choice
        else:  # strategy == 'switch'
            # Switch to the unopened door that wasn't revealed
            final_choice = [
                door
                for door in doors
                if door != initial_choice and door != revealed_door
            ][0]

        # Check if won
        if final_choice == car:
            wins += 1

    return (wins / n) * 100


# Simulate with a large number of trials (e.g., 100,000)
trials = 100000
stay_wins = simulate_monty_hall(trials, "stay")
switch_wins = simulate_monty_hall(trials, "switch")

print(f"stay win rate: {stay_wins:2f}%")

print(f"switch win rate: {switch_wins:2f}%")
