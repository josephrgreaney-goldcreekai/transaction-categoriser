from src.transaction_categoriser.categoriser import TransactionCategoriser
import json

# helper function

def helper():
    with open('transactions.json', 'r') as file:
        transactions = json.load(file)
    engine = TransactionCategoriser(transactions)
    return engine
    

# Check IDF of "uber" is 1.735
def test_idf_uber():
    engine = helper()
    assert round(engine.idf("uber"), 3) == 1.735

# Check IDF of "netflix" (~2.833) is great than idf of "uber" (~1.735)
def test_idf_uber_greater_idf_netflix():
    engine = helper()
    assert engine.idf("netflix") > engine.idf("uber")

def test_idf_unknown_word_zero():
    engine = helper()
    assert engine.idf("") == 0

def test_uber_trip_to_airport_suggests_category_transport():
    engine = helper()
    assert engine.suggest("Uber trip to the airport")[0] == "Transport"

def test_uber_eats_order_sushi_suggests_category_meals():
    engine = helper()
    assert engine.suggest("Uber Eats order sushi")[0] == "Meals"

def test_woolworths_groceries_suggests_category_Groceries():
    engine = helper()
    assert engine.suggest("Woolworths Groceries")[0] == "Groceries"

def test_random_shop_xyz_is_none():
    engine = helper()
    assert engine.suggest("Random Shop XYZ")[0] is None

def test_find_matches_exactly_one_result():
    engine = helper()
    assert len(engine.find_matches("uber", top_k=1)) == 1

