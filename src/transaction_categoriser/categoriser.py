import math
from collections import Counter
from src.transaction_categoriser.cleaning import clean_txt

class TransactionCategoriser:
    def __init__(self, transactions):
        self.descriptions = transactions
        self.description_counts = []
        for transaction in transactions:
            description = clean_txt(transaction["description"])
            self.description_counts.append(Counter(description))
        self.doc_freq = Counter()
        for counts in self.description_counts:
            for word in counts:
                self.doc_freq[word] += 1
        self.num_descriptions = len(transactions)

    # Find how rare each word is across all chunks.
    def idf(self, word):
        df = self.doc_freq[word]
        if not df:
            return 0
        return math.log(self.num_descriptions/df)

    # Return one chunks total score for the query.
    def score(self, description_words, chunk_index):
        # Numbr of times each word appears in each given description.
        counts = self.description_counts[chunk_index]
        # start the total
        total = 0
        for word in description_words:
            tf = counts[word]
            total += tf*self.idf(word)
        return total

    def find_matches(self, description, top_k=3):
        description_words = clean_txt(description)
        results = []
        for i, description in enumerate(self.descriptions):
            description_score = self.score(description_words, i)
            if description_score > 0:
                results.append((description_score, description))
        results.sort(key=lambda pair: pair[0], reverse=True)
        return results[:top_k]

    def suggest(self, description):
        top_3_pairs = self.find_matches(description)
        if not top_3_pairs:
            return None, top_3_pairs
        top_pairs_categories = []
        for score, transaction in top_3_pairs:
            category = transaction["category"]
            top_pairs_categories.append(category)
        category = Counter(top_pairs_categories).most_common(1)[0][0]
        return category, top_3_pairs

        

            
        
        
        



    

        
        





        

