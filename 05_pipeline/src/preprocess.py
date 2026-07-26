"""
Preprocessing Pipeline Module.
Sets up ColumnTransformer for taxonomic, geographic, and etnobotanical text features.
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def build_preprocessor(max_tfidf_features: int = 300) -> ColumnTransformer:
    """
    Constructs Scikit-Learn ColumnTransformer for dataset preprocessing.
    
    Args:
        max_tfidf_features (int): Maximum number of features for TF-IDF vectorization of Uses text.
        
    Returns:
        ColumnTransformer: Unfitted preprocessor pipeline object.
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ('taxonomic', OneHotEncoder(handle_unknown='ignore'), ['Family', 'Genus']),
            ('geographic', CountVectorizer(tokenizer=lambda x: [y.strip() for y in x.split(',') if y.strip()]), 'Distribution'),
            ('etnobotanical', TfidfVectorizer(max_features=max_tfidf_features), 'Uses')
        ]
    )
    return preprocessor

def encode_target(y_train, y_val, y_test):
    """
    Fits LabelEncoder on target labels and transforms train/val/test splits.
    
    Returns:
        tuple: (y_train_enc, y_val_enc, y_test_enc, label_encoder)
    """
    le = LabelEncoder()
    y_train_enc = le.fit_transform(y_train)
    y_val_enc = le.transform(y_val)
    y_test_enc = le.transform(y_test)
    return y_train_enc, y_val_enc, y_test_enc, le
