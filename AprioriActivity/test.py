from collections import defaultdict
import operator

THRESHOLD = 50

item_counts = defaultdict(int)
pair_counts = defaultdict(int)
triple_counts = defaultdict(int)

# Read data
with open("groceries.csv") as f:
  lines = f.readlines()
f.close()

def normalize_group(*args):
  return str(sorted(args))

def generate_pairs(*args):
  pairs = []
  for idx_1 in range(len(args) - 1):
    for idx_2 in range(idx_1 + 1, len(args)):
      pairs.append(normalize_group(args[idx_1], args[idx_2]))
  return pairs

# Find Candidate items 
for line in lines:
  for item in line.split():
    item_counts[item] += 1
    
# Filter for Frequent Items Set One
frequent_items = set()
for key in item_counts:
  if item_counts[key] > THRESHOLD:
    frequent_items.add(key)
    

# Filter for Frequent Item Set Two
for line in lines:
  items = line.split()
  for idx_1 in range(len(items) -1):
    if items[idx_1] not in frequent_items:
      continue
    for idx_2 in range(idx_1 + 1, len(items)):
      if items[idx_2] not in frequent_items:
        continue
      pair = normalize_group(items[idx_1], items[idx_2]) 
      pair_counts[pair] += 1
        

frequent_pairs = set()
for key in pair_counts:
  if pair_counts[key] > THRESHOLD:
    frequent_pairs.add(key)
    

# Filter for Frequent Item Set Three
for line in lines:
  items = line.split()
  for idx_1 in range(len(items) -1):
    if items[idx_1] not in frequent_items:
      continue
    for idx_2 in range(idx_1 + 1, len(items)):
      if items[idx_2] not in frequent_items:
        continue
      first_pair = normalize_group(items[idx_1], items[idx_2])
      if first_pair not in frequent_pairs:
        continue
      for idx_3 in range(idx_2 + 1, len(items)):
        if items[idx_3] not in frequent_items:
          continue
        pairs = generate_pairs(items[idx_1], items[idx_2], items[idx_3])
        if any(pair not in frequent_pairs for pair in pairs):
          continue
        triple = normalize_group(items[idx_1], items[idx_2], items[idx_3])
        triple_counts[triple] += 1
  
frequent_triples = set()
for key in triple_counts:
  if triple_counts[key] > THRESHOLD:
    frequent_triples.add(key)
    
# triple_counts = { k: v for k, v in triple_counts.items() if v > THRESHOLD }
# sorted_triples = sorted(triple_counts.items(), key=operator.itemgetter(1))

# for entry in sorted_triples:
#   print('{0}: {1}'.format(entry[0], entry[1]))
print(frequent_triples)