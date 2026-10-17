transactions = [
    {"description": "Walmart", "category": "Groceries", "amount": 82.45},
    {"description": "Shell", "category": "Gas", "amount": 45.20},
    {"description": "Netflix", "category": "Entertainment", "amount": 15.99},
    {"description": "Amazon", "category": "Shopping", "amount": 73.50},
    {"description": "Target", "category": "Shopping", "amount": 125.50},
    {"description": "Costco", "category": "Groceries", "amount": 210.75},
    {"description": "Uber", "category": "Transportation", "amount": 32.40},
    {"description": "Best Buy", "category": "Electronics", "amount": 450.00},
]


def extract_categories(spendings):
    category_list = []
    for spend in spendings:
        category_list.append(spend['category'])
    return category_list


def total_spending(spendings):
    total = 0
    for spend in spendings:
        total += spend["amount"]
    return round(total, 2)


def category_spending(spendings):

    category_spend_dict = dict.fromkeys(extract_categories(spendings), 0)

    for spend in spendings:
        category_spend_dict[spend["category"]] += spend["amount"]

    return category_spend_dict


def highest_category(category_spend_dict):
    highest_value = max(category_spend_dict.values())
    for k, v in category_spend_dict.items():
        if highest_value == v:
            return k


def largest_transaction(spendings):
    return max(spendings, key=lambda item: item["amount"])


def top_5(spendings):
    sorted_spending = sorted(spendings, key=lambda item: item["amount"], reverse=True)
    top5 = sorted_spending[:5]
    return top5


def main():
    total = total_spending(transactions)

    category_spend_dict = category_spending(transactions)

    largest_transaction_dict = largest_transaction(transactions)
    print()
    print(f"Total spending:  ${total}\n")
    print("Spending by category:".upper())
    for category, amount in category_spend_dict.items():
        print(f"{category}:  ${amount}")
    print()
    print("largest spending:".upper())
    print(f"Largest Spending Category: {highest_category(category_spend_dict)}")
    print(f"Largest transaction: {largest_transaction_dict['description']} -  ${largest_transaction_dict['amount']}")
    print()
    print("Top 5 Transactions:")
    counter = 1
    for spend in top_5(transactions):
        print(f"{counter}) {spend['description']} -  ${spend['amount']}")
        counter += 1



main()
