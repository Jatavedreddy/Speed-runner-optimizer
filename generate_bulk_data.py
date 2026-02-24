import os
import pandas as pd
import random

def generate_files(target_dir='bulk_data', num_files=200):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    for i in range(num_files):
        filename = f"log_{i}.csv"
        filepath = os.path.join(target_dir, filename)
        
        # Each file has 100 rows of random data
        data = {
            'id': range(100),
            'value': [random.random() * 100 for _ in range(100)],
            'category': [random.choice(['A', 'B', 'C']) for _ in range(100)]
        }
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)

if __name__ == "__main__":
    print("Generating 200 files in bulk_data...")
    generate_files()
    print("Done.")
