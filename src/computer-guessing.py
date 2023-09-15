# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.

# First strategy - going from 1 to 20
for guess in range(1, 21):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break

    print("I must have been too low, right?", result)

# Second strategy - starting at 20
for i in range(20, 0, -1): # doesn't include 0
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break

    print("I must have been too low, right?", result)

# Third strategy - starting by guessing 10 and using the middle of the interval
upper_bound = 20
lower_bound = 1
for guess in range(lower_bound, upper_bound + 1):
    guess = (upper_bound + lower_bound) // 2
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "low":
        lower_bound = guess + 1
    if result == "high":
        upper_bound = guess - 1
    if result == "hit":
        print("Wuhuu!")
        break