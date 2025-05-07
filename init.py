
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