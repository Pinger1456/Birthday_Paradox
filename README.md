
# Birthday Paradox Simulation

## Overview
This project implements a **Birthday Paradox** simulation using Python. The Birthday Paradox is a well-known problem in probability theory that reveals how likely it is for two people in a group to share the same birthday. Surprisingly, in a group of just 23 people, there's a better than even chance that two of them will have the same birthday.

The simulation generates random birthdays for a specified number of people and checks whether any two birthdays match. The process is repeated 100,000 times to estimate the probability of a birthday match in different-sized groups.

## How It Works
- **Birthday Generator**: Generates a random list of birthdays for a group of people. Each birthday is chosen randomly from the 365 possible days in a non-leap year.
- **Birthday Match Checker**: Checks whether there is a match between any two birthdays in a group.
- **Simulation**: Repeats the process 100,000 times for a specified group size to calculate the probability of a birthday match.

## Features
- Simulates birthday matches for groups of different sizes (up to 100 people).
- Monte Carlo simulation with 100,000 iterations to estimate the probability of a birthday match.
- Provides a detailed breakdown of results, showing when a match is found in the group.

## How to Run
### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/birthday-paradox-simulation.git
   cd birthday-paradox-simulation
   ```

2. Run the script:
   ```bash
   python birthday_simulation.py
   ```

### Example Output
```bash
Birthday Paradox, by Al Sweigart

How many birthdays shall I generate? (Max 100)
> 23

Here are 23 birthdays:
Mar 1, May 18, Sep 22, Jan 15, ...

In this simulation, multiple people have a birthday on Oct 13

Generating 23 random birthdays 100,000 times...
10,000 simulations run...
100,000 simulations run.

Out of 100,000 simulations of 23 people, there was a matching birthday in that group 50,682 times.
This means that 23 people have a 50.68% chance of having a matching birthday in their group.
```

## Project Structure
- **birthday_generator.py**: Contains the `BirthdayGenerator` class, which generates random birthdays.
- **birthday_simulation.py**: Contains the `BirthdaySimulation` class, which runs the simulation and checks for matching birthdays.

## Future Enhancements
- Add support for leap years.
- Improve the user interface by adding a graphical representation of the results.
- Implement additional statistical analysis, such as confidence intervals for the probability estimates.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project was inspired by the **Birthday Paradox** problem, a popular example in probability theory.
- Original simulation concept by Al Sweigart in his book "Big Book of Small Python Projects".
