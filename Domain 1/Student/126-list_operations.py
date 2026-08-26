capitals=["Montgomery","Juneau","Phoenix"]
capitals.append("Sacramento")
population=[200000, 32000, 1600000]
capitals.insert(3,"LittleRock")
capitals.remove("Juneau") #montgomery, phoenix, littlerock, sacramento
capitals[2]="Little Rock"
capitals.sort(reverse=True)
print(capitals.pop(0))
print(capitals)
print(min(population))
print(len(capitals))
