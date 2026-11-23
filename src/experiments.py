"""Experiment log: one row per training run."""
import os
from datetime import datetime

import pandas as pd


def log_experiment(log_path, **row):
    # e.g. log_experiment(path, model='baseline_cnn', author='Ana', epochs=30, val_macro_f1=0.41)
    row = {'date': datetime.now().strftime('%Y-%m-%d %H:%M'), **row}
    df = pd.DataFrame([row])
    if os.path.exists(log_path):
        df = pd.concat([pd.read_csv(log_path), df], ignore_index=True)
    df.to_csv(log_path, index=False)
    return df
