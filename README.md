# plant-identifier_dlnn26

Projeto da 2.ª época de **Deep Learning Neural Networks** (EDSA 2026/27, NOVA IMS), **Grupo 4**.

## Objetivo

Identificar a **espécie de uma planta a partir de uma fotografia** tirada em condições reais.

- **Input:** uma fotografia de uma planta (flor, folha, fruto, casca ou planta inteira).
- **Output:** a espécie, entre as espécies do subconjunto escolhido.

_A definição final da tarefa, do subconjunto de espécies e das métricas ainda está por decidir em grupo._

## Dataset

**Pl@ntNet-300K** (Garcin et al., NeurIPS 2021 Datasets and Benchmarks): 306 087 fotografias de 1 000 espécies, tiradas pelos utilizadores da app Pl@ntNet, com split oficial de treino, validação e teste.

- Repositório: <https://github.com/plantnet/PlantNet-300K>
- Download (v2): <https://zenodo.org/records/10419064>
- Artigo: <https://openreview.net/forum?id=eLYinD0TtIt>

Os dados **não** ficam no repositório (ver [`data/README.md`](data/README.md)). Cada imagem tem a sua licença e autor nos metadados; citar o dataset no relatório.

## Estrutura

```
plant-identifier_dlnn26/
├── data/          # dados descarregados (fora do git)
├── notebooks/     # notebooks de exploração e de treino (Colab)
├── src/           # código partilhado: carregar dados, modelos, callbacks
├── report/        # relatório (máx. 5 páginas, Arial 11) e figuras
├── requirements.txt
└── README.md
```

## Como correr

1. Abrir o notebook no Google Colab a partir do GitHub (`File > Open notebook > GitHub`).
2. Descarregar os dados para o Google Drive, seguindo [`data/README.md`](data/README.md).
3. Instalar as dependências: `pip install -r requirements.txt` (no Colab, a maioria já vem instalada).

## Entrega

Até **18 de dezembro**, no Moodle (Turnitin): código, link do dataset e relatório, num único ficheiro `GROUP 4.zip`.

## Grupo 4

- Ana Filipa Filipe
- Ana Rita Carapinha
- Inês Rodrigues
- Madalena Lourenço
- Nuno Pinto
