import random
from brain_games.consts import MIN_PROGRESSION_LENGHT, MAX_PROGRESSION_LENGHT, PROGRESSION_INSTUCTION
from brain_games.engine import run_game



def get_progression_and_miss_num():
    start, step = random.randint(1, 100), random.randint(1, 100)
    
    progr_length = random.randint(MIN_PROGRESSION_LENGHT, MAX_PROGRESSION_LENGHT)
    missed_index = random.randint(0, progr_length - 1)
    progr = []
    for i in range(progr_length):
        progr.append(start + step * i)
        
    missed_index = random.randint(0, progr_length - 1)
    missed_num = progr[missed_index]
    progr[missed_index] = '..'
    progr_with_missed_num = ' '.join(map(str, progr))
    
    return progr_with_missed_num, str(missed_num)


def test_func():  # this is a func for test
    return get_progression_and_miss_num()

