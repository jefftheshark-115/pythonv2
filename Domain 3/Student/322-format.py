score = 20000000000
level = 3
player1 = "Stacey"

print("Player1:", player1, "Score:", score, "Level:", level)
print("{} has {} points and has reached level {}".format(player1, score, level))
print(f"{player1} has {score} points and has reached level {level}")
print(f"{player1:<15} {score:>10}")
print("player1: %1s score: %.2f" % (player1, score))