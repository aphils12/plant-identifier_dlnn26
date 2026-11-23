"""Caminhos e hiperparâmetros partilhados pelo projeto."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
FIGURES_DIR = ROOT / "results" / "figures"
TABLES_DIR = ROOT / "results" / "tables"

# Colab: shared Drive folder and unzipped images (see data/README.md)
DRIVE_DIR = Path("/content/drive/MyDrive/plantnet_dlnn26")
COLAB_DATA = Path("/content/plantnet20")

SEED = 42
IMG_SIZE = 224
BATCH_SIZE = 32
