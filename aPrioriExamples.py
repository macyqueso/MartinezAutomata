#MARKET BASKET ANALYSIS

from itertools import combinations

def apriori(transactions, min_support):
    # Count single items
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] = item_counts.get(frozenset([item]), 0) + 1

    n = len(transactions)
    frequent = {k: v for k, v in item_counts.items() if v/n >= min_support}
    all_frequent = dict(frequent)

    current = list(frequent.keys())
    k = 2

    while current:
        # Generate candidates of size k
        candidates = set()
        for i in range(len(current)):
            for j in range(i+1, len(current)):
                union = current[i] | current[j]
                if len(union) == k:
                    candidates.add(union)

        # Count candidates
        counts = {}
        for transaction in transactions:
            t_set = frozenset(transaction)
            for candidate in candidates:
                if candidate.issubset(t_set):
                    counts[candidate] = counts.get(candidate, 0) + 1

        frequent = {k_set: v for k_set, v in counts.items() if v/n >= min_support}
        all_frequent.update(frequent)
        current = list(frequent.keys())
        k += 1

    return all_frequent

transactions = [
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
]

result = apriori(transactions, min_support=0.6)
for itemset, count in result.items():
    print(f"{set(itemset)} → support: {count}/{len(transactions)}")

#GENERATING ASSOCIATION RULES

#EXAMPLE 2

def generate_rules(frequent_itemsets, transactions, min_confidence):
    n = len(transactions)
    rules = []

    for itemset in frequent_itemsets:
        if len(itemset) < 2:
            continue
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent

                support_antecedent = frequent_itemsets.get(antecedent, 0)
                support_itemset = frequent_itemsets[itemset]

                if support_antecedent > 0:
                    confidence = support_itemset / support_antecedent
                    if confidence >= min_confidence:
                        rules.append((set(antecedent), set(consequent), round(confidence, 2)))
    return rules

rules = generate_rules(result, transactions, min_confidence=0.75)
for ant, con, conf in rules:
    print(f"{ant} → {con}  (confidence: {conf})")