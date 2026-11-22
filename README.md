# Identificação de espécies de plantas a partir de fotografias

Projeto da 2.ª época de **Deep Learning Neural Networks** (EDSA 2026/27, NOVA IMS), **Grupo 4**. 
Elementos: Ana Filipa Filipe; Ana Rita Carapinha; Inês Rodrigues; Madalena Lourenço; Nuno Pinto.

## Objetivo

Identificar a **espécie de uma planta a partir de uma fotografia** tirada em condições reais.

- **Input:** uma fotografia de uma planta (flor, folha, fruto, casca ou planta inteira).
- **Output:** a espécie prevista, entre as 20 espécies escolhidas (ver [Espécies](#as-20-espécies)).
- **Tipo de problema:** classificação de imagens com 20 classes.

## Dataset

**Pl@ntNet-300K** (Garcin et al., NeurIPS 2021 Datasets and Benchmarks): 306 087 fotografias de 1 000 espécies, tiradas pelos utilizadores da app Pl@ntNet, com split oficial em treino, validação e teste.

- Repositório: <https://github.com/plantnet/PlantNet-300K>
- Download (v2): <https://zenodo.org/records/10419064>
- Artigo: <https://openreview.net/forum?id=eLYinD0TtIt>

Os dados **não** ficam no repositório. As instruções de download estão em [`data/README.md`](data/README.md). Cada imagem tem a licença e o autor nos metadados, e o dataset tem de ser citado no relatório.

## Decisões (22/11/2026)

Tomadas depois de rever os metadados do dataset. A exploração completa está no [Explorador Pl@ntNet-300K](https://claude.ai/artifact/9nGUrwgrk4SbpkEgSeS6nr).

| Tema | Decisão | Porquê, segundo os dados |
|---|---|---|
| Espécies | **20 espécies em 10 pares do mesmo género** (ver tabela abaixo) | Há pares difíceis e pares fáceis, o que mostra se a rede erra sobretudo entre espécies parecidas |
| Limpeza | Excluir as classes `spp.` e os nomes repetidos, e também os géneros que têm uma classe `spp.` | *Lavandula spp.* e *Pelargonium spp.* sobrepõem-se às outras espécies desses géneros |
| Treino | **Até 1 000 fotos por espécie** | Equilibra o treino (~20 000 fotos). Só *Cucurbita maxima* fica abaixo (~890) |
| Métrica | **Macro-F1**, com accuracy e matriz de confusão | O teste não é equilibrado: tem de 111 a 766 fotos por espécie |
| Órgãos | Treinar com flor, folha, fruto, planta inteira e casca (excluir `other`, `branch`, `scan` e `none`). Na análise de erros, comparar só **flor vs. folha** | No teste há 4 643 fotos de flor, 2 350 de folha, 144 de fruto, 77 de planta inteira e 36 de casca. O órgão também está ligado à espécie (96% das fotos de *T. zebrina* são de folha) |
| Avaliação | Avaliar no **teste completo** e num **teste só com fotógrafos novos** | 23% das fotos de teste são de pessoas que também têm fotos da mesma espécie no treino (até 36% em *Cirsium arvense*) |
| Split | Usar o split oficial sem alterações. O teste só é usado uma vez | Permite comparar com os resultados publicados |
| Download | Só as pastas das 20 espécies (~10 GB), extraídas do zip remoto | O Zenodo aceita downloads parciais (testado a 22/11) |
| Extensão | Deteção de espécies desconhecidas, opcional e só no fim | Só se o modelo base estiver pronto até ~11/12 |

### As 20 espécies

O `species_id` de cada espécie está entre parênteses.

| Género | Espécie A | Espécie B | Família |
|---|---|---|---|
| Cirsium | *Cirsium vulgare* (4) | *Cirsium arvense* (3) | Asteraceae |
| Trifolium | *Trifolium pratense* (112) | *Trifolium repens* (225) | Fabaceae |
| Lamium | *Lamium purpureum* (84) | *Lamium galeobdolon* (171) | Lamiaceae |
| Papaver | *Papaver rhoeas* (200) | *Papaver somniferum* (202) | Papaveraceae |
| Tradescantia | *Tradescantia pallida* (190) | *Tradescantia zebrina* (15) | Commelinaceae |
| Hypericum | *Hypericum perforatum* (11) | *Hypericum calycinum* (406) | Hypericaceae |
| Sedum | *Sedum album* (47) | *Sedum acre* (46) | Crassulaceae |
| Petrosedum | *Petrosedum sediforme* (60) | *Petrosedum rupestre* (186) | Crassulaceae |
| Calendula | *Calendula officinalis* (35) | *Calendula arvensis* (243) | Asteraceae |
| Cucurbita | *Cucurbita pepo* (310) | *Cucurbita maxima* (366) | Cucurbitaceae |

Os mesmos valores, prontos a usar no código:

```python
SPECIES = [4, 3, 112, 225, 84, 171, 200, 202, 190, 15, 11, 406, 47, 46, 60, 186, 35, 243, 310, 366]
TRAIN_CAP = 1000
ORGANS = ["flower", "leaf", "fruit", "habit", "bark"]
```

## Estrutura do repositório

```text
plant-identifier_dlnn26/
├── data/              # dados descarregados (fora do git; ver data/README.md)
├── notebooks/         # notebooks de exploração e de treino (Colab)
├── src/               # código partilhado
│   ├── config.py      #   caminhos e hiperparâmetros
│   ├── data.py        #   carregamento, filtragem e data augmentation
│   ├── models.py      #   arquiteturas
│   ├── train.py       #   treino e callbacks
│   └── evaluate.py    #   métricas e matriz de confusão
├── models/            # pesos treinados (fora do git)
├── results/
│   ├── figures/       # gráficos para o relatório
│   └── tables/        # tabelas para o relatório
├── report/            # relatório (máx. 5 páginas, Arial 11)
├── requirements.txt   # dependências (TensorFlow/Keras, Python 3.12)
└── README.md
```

## Ambiente de trabalho

O código é escrito no computador de cada pessoa e o treino corre no **Google Colab**. O TensorFlow não usa a GPU nativamente no Windows, por isso no computador treinar é muito lento.

### No computador (editar código e explorar dados)

Pré-requisitos: **Python 3.12** e **Git**.

```bash
# 1. Clonar o repositório
git clone https://github.com/aphils12/plant-identifier_dlnn26.git
cd plant-identifier_dlnn26

# 2. Criar o ambiente virtual (só da primeira vez)
python -m venv .venv

# 3. Ativar o ambiente (sempre que se abre um terminal novo)
.venv\Scripts\activate          # Windows (PowerShell)
source .venv/bin/activate       # macOS / Linux

# 4. Instalar as dependências
python -m pip install --upgrade pip
pip install -r requirements.txt
```

No VS Code, escolher o interpretador `.venv` (`Ctrl+Shift+P` › *Python: Select Interpreter*). Nos notebooks, escolher o mesmo ambiente como kernel.

O PowerShell pode bloquear a ativação do ambiente. Nesse caso, correr uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

### No Google Colab (treinar)

1. Abrir o notebook a partir do GitHub (`File > Open notebook > GitHub`).
2. Escolher uma GPU (`Runtime > Change runtime type > T4 GPU`).
3. Correr esta célula no início do notebook:

   ```python
   from google.colab import drive
   drive.mount("/content/drive")

   !git clone https://github.com/aphils12/plant-identifier_dlnn26.git
   %cd plant-identifier_dlnn26
   !pip install -q -r requirements.txt
   ```

4. Se o `pip` mudar versões que já vinham instaladas no Colab, reiniciar a sessão (`Runtime > Restart session`) e continuar.
5. Descarregar os dados para o Google Drive, seguindo [`data/README.md`](data/README.md). Só é preciso fazer isto uma vez.

## Entrega

- **Prazo:** 18 de dezembro de 2026, no Moodle (Turnitin).
- **Ficheiro:** um único `GROUP 4.zip` com o código, o link do dataset e o relatório.
- Preencher também o Excel do docente com os dados do grupo.
