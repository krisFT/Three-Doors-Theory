# Monty Hall Simulation for Three Doors Theory

This project simulates the **Three Doors Theory** using the famous **Monty Hall Problem** to illustrate the probabilities of winning when switching versus staying with the initial choice.

## Overview

The Monty Hall Problem is a probability puzzle that challenges intuition. This simulation demonstrates how switching doors increases the likelihood of winning the prize compared to staying with the original choice.

## Features

- Simulates the Monty Hall Problem with three doors.
- Calculates and displays the probabilities of success for both strategies:
  - **Switching doors**
  - **Staying with the initial choice**
- Provides empirical results based on a large number of trials (default: 100,000).

## How It Works

1. A prize is randomly placed behind one of three doors.
2. The participant selects one door.
3. The host, knowing where the prize is, opens a different door that does not contain the prize.
4. The participant is given the option to switch to the remaining unopened door or stay with their initial choice.
5. The simulation tracks the outcomes for both strategies over multiple trials.

## Why This Question Feels Counterintuitive

The simple explanation is as follows:

- On your **first pick**, you only have a **1/3 chance** of selecting the correct door (the prize).
- This means there’s a **2/3 chance** that your first pick is **wrong**.
- When the host opens a door that doesn’t contain the prize:
  - If your **first pick is correct** (1/3 chance), switching will make you **lose** (100% wrong).
  - If your **first pick is incorrect** (2/3 chance), switching will make you **win** (100% correct).

Thus, by switching, you effectively take advantage of the **2/3 chance** that your initial pick was incorrect. This is why **switching doors gives you a much higher chance of winning** (2/3), compared to staying (1/3).

---

### A Quick Visual Example

1. **Three doors:** A, B, C.
2. The prize is behind Door B.
3. You pick Door A (1/3 chance correct, 2/3 chance wrong).
4. The host opens Door C (which does not contain the prize).
5. Switching to Door B guarantees that:
   - You win in 2/3 of scenarios.
   - Staying with Door A only wins in 1/3 of scenarios.

This counterintuitive outcome highlights the power of probability over intuition.

## Requirements

- Python 3.x

## Example Output
- Total Trials: 100000
- Switch Wins: 66959 (66.96%)
- Stay Wins: 33041 (33.04%)

