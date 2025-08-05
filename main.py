import time;
from tic_tac_toe.game import play_game

runs = 500

stats = {}

start = time.time()
for x in range(runs):
    temp = play_game(0)
    count = stats.get(temp, 0)
    stats[temp] = count + 1
end = time.time()
print(stats)
print(end-start)
    




