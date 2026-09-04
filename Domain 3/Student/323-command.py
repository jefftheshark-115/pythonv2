#items = ["Wand", "Rock", "Pogo Stick"]
#levels = [1, 2, 3]
#for level in levels: 
 #   for item in items:
 #       if level == 2 and item == "Rock":
  #          continue
 #       print(f"you can get a {item} at level {level}")

items, levels = ["Wand", "Rock", "Pogo Stick"], [1, 2, 3]
[print(f"you can get a {i} at level {l}") for l in levels for i in items if not (l == 2 and i == "Rock")]
