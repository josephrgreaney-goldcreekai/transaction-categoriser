import json
from src.transaction_categoriser.categoriser import TransactionCategoriser

def main():
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
    engine = TransactionCategoriser(transactions)
    print(f"Welcome, {len(transactions)} transactions loaded.")
    while True:
        user_input = input("Would you like to [search] or [/quit] the program?\n").lower()
        if user_input == "/quit":
            break
        elif user_input == "search":
            description = input("Search here:\n")
            results = engine.suggest(description)
            print(f"The top category was {results[0]}. The three top results were\n1: {results[1][0][1]['description']} for total of ${results[1][0][1]['amount']} in the {results[1][0][1]['category']} category with a score of {results[1][0][0]:.4f}"
                f"\n2: {results[1][1][1]['description']} for total of ${results[1][1][1]['amount']} in the {results[1][1][1]['category']} category with a score of {results[1][1][0]:.4f}"
                f"\n3: {results[1][2][1]['description']} for total of ${results[1][2][1]['amount']} in the {results[1][2][1]['category']} category with a score of {results[1][2][0]:.4f}")
            if not results:
                print("No results found")
                
        else:
            print("Please type search or /quit")
                

if __name__ == "__main__":
    main()