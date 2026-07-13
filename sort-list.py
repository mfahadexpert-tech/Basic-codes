#Aik scoreboard list banayein. Is mein se sab se kam marks 
# .remove() karein aur baki list ko .sort() karke descending order mein dikhayen
scores = [85, 92, 70, 98, 65, 88]

lowest = min(scores)
scores.remove(lowest)

scores.sort(reverse=True)

print("Updated Leaderboard:", scores)