"""
Sample script to download or prepare demonstration data for federated learning and RAG experiments.
"""

import os
import urllib.request

DATA_URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
DATA_PATH = "data/pima-indians-diabetes.csv"

def download_data():
    os.makedirs("data", exist_ok=True)
    print("Downloading sample dataset...")
    urllib.request.urlretrieve(DATA_URL, DATA_PATH)
    print(f"Saved dataset to {DATA_PATH}")

if __name__ == "__main__":
    download_data()