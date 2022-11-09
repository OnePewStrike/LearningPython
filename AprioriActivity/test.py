from collections import defaultdict

THRESHOLD = 50

item_counts = defaultdict(int)

with open("groceries.csv") as f:
  lines = f.readlines()
f.close()

for line in lines:
  for item in line.split():
    item_counts[item] += 1
    
frequent_items = set()
for key in item_counts:
  if item_counts[key] > THRESHOLD:
    frequent_items.add(key)

for line in lines:
  items = line.split()
  for idx_1 in range(len(items) -1):
    if items[idx_1] not in frequent_items:
      continue
    for idx

print(frequent_items) 
