# class HashTable:
#     def _init_(self, size=10):
#         self.size = size
#         self.table = [None] * size
    
#     def _hash(self, key):
#         return key % self.size
    
#     def Insert(self, key, value):
#         index = self._hash(key)
#         while self.table[index] is not None:
#             if self.table[index][0] == key:
#                 self.table[index] = (key, value)
#                 print(f"Updated ({key}: {value}) at index {index}")
#                 return
#             index = (index + 1) % self.size
#         self.table[index] = (key, value)
#         print(f"Inserted ({key}: {value}) at index {index}")

# # Demo
# ht = HashTable()
# ht.Insert(5, "apple")  # Inserted (5: apple) at index 5
# ht.Insert(15, "orange") # Inserted (15: orange) at index 6 (linear probe)
# ht.Insert(5, "banana")  # Updated (5: banana) at index 5





import numpy as np

class FeatureHasher:
    def __init__(self, n_features=1000):
        self.n_features = n_features
    
    def transform(self, raw_features):
        """Convert text features to hashed feature vector"""
        hashed_features = np.zeros(self.n_features)
        
        for feature in raw_features:
            # Hash the feature and map to one of n_features bins
            hashed_index = hash(feature) % self.n_features
            # Increment count for this feature
            hashed_features[hashed_index] += 1
            
        return hashed_features

# Example usage
hasher = FeatureHasher(n_features=20)
text_data = ["machine", "learning", "hashing", "trick", "feature", "engineering"]

# Convert text to hashed feature vector
hashed_vector = hasher.transform(text_data)
print("Hashed feature vector:", hashed_vector)