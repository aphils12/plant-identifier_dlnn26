# Data

The images are not in the repository. They are in the shared Google Drive folder `plantnet_dlnn26`.

## Pl@ntNet-300K

- Download (v2): <https://zenodo.org/records/10419064>
- License: CC BY 4.0 (each image also has its own author and license in the metadata)

## Our subset

Downloaded on 23/11/2026 with `notebooks/00_download_data.ipynb`. It only downloads the folders of our 20 species from the Zenodo zip (41.8 GB in total), and keeps:

- organs: flower, leaf, fruit, habit, bark
- train: max 1000 images per species (seed 42)
- val and test: all images of these species and organs (official split)

| split | images |
|---|---|
| train | 19,885 |
| val | 7,243 |
| test | 7,250 |
| total | 34,378 |

Files in the Drive folder:

```text
plantnet_dlnn26/
├── plantnet20_v1.zip            # images/<split>/<species_id>/<PN_hash>.jpg (4.7 GB)
├── selection.csv                # one row per image: species, organ, author, license, split, path
├── plantnet300K_metadata.csv    # original metadata (all 306,087 images)
├── species_metadata.csv         # original species list (1000 species)
└── 00_download_data.ipynb
```

## How to use it

1. Add a shortcut to the shared folder in your Drive (right click > Organise > Add shortcut > My Drive).
2. At the top of each notebook:

```python
from google.colab import drive
drive.mount('/content/drive')

!cp /content/drive/MyDrive/plantnet_dlnn26/plantnet20_v1.zip /content/
!unzip -q -o /content/plantnet20_v1.zip -d /content/plantnet20
```

The images are read from `/content/plantnet20` (Colab disk), not directly from Drive, because Drive is very slow with many small files.

There is no need to run `00_download_data.ipynb` again.

## Split

`data/selection.csv` (in the repo) is a copy of the list in Drive: one row per image with its split. All models use this same split. Experiment results go to `experiments.csv` in the Drive folder (see `src/experiments.py`).
