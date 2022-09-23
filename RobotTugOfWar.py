import random


r1_victory_counter = 0
r2_victory_counter = 0


for k in range(0,4):

    for i in range(0,1000000):
        initial_position = -0.2849
        r1_victory = False
        r2_victory = False

        while (r1_victory == False and r2_victory == False):
            r1_move = random.random()
            initial_position += r1_move
            if(initial_position > 0.5):
                r1_victory = True
                r1_victory_counter += 1
            else:
                r2_move = random.random()
                initial_position -= r2_move
                if(initial_position < -0.5):
                    r2_victory = True
                    r2_victory_counter += 1

    print("Robot 1 won {} times and robot 2 won {} times"
          .format(r1_victory_counter, r2_victory_counter))

