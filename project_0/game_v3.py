import numpy as np
import random

def game_core_v3(number: int = np.random.randint(1, 101)) -> int:
    """Randomly guess the number
    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    #number of attempts
    count = 0
    #minimum number
    min = 1
    #maximum number
    max = 100
    #a random number from 1 to 100
    predict_number = number = np.random.randint(1, 101)

    #infinite loop
    while True:
      #find a middle of the range from 1 to 100 to shorten the search for the hidden number
      predict_number = (min + max) // 2
      count += 1

      #if a predict number is greater, then we set a new upper bound
      if predict_number > number:
        max = predict_number - 1

      #if a predict number is less, then we set a new lower bound
      elif predict_number < number:
        min = predict_number + 1

      else:
        break #game over

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)