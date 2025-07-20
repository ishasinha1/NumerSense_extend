# Empirical Analysis of commonsense knowledge of PTLMs (Color, Size, Location)

This reproduction expands on the _NumerSense_ paper (https://arxiv.org/abs/2005.00683) to attempt to induce commonsense knowledge of pre-trained language models like BERT-Base and RoBERTa-Base in the domains of color, size and location.

We clone the original codebase used by the authors of that paper and add to it. You can find the original Github here: https://github.com/INK-USC/NumerSense/tree/main

Please follow the instructions listed in THEIR readme for setting up your local environment.

**Compiling Datasets:**

Each of the following files can also be found in the directories, 'color', 'size', 'location' and 'masking'. The intermediate datasets from different points while cleaning the data can be found in 'intermediate-datasets'. The final datasets used can be found in 'data-484'.

_Color:_

Extracting examples from ConceptNet and OMCS: https://colab.research.google.com/drive/1oCKCbsc5AqS8RUGXkutecp8EW4wyBTkc?usp=sharing

Cleaning the data and selecting 3,000 examples: https://colab.research.google.com/drive/1LRRhXx2n8_FdmCAWo-3W7J6yeLgVCgjG?usp=sharing

_Size:_ https://colab.research.google.com/drive/1sB5pb8_og-LJFJeUmI4cVyBQmRb1Fa3-?usp=sharing

_Location:_ https://colab.research.google.com/drive/1UiDvNkBnXRPLOxxjMKFobjvSYku5pDxy?usp=sharing

_Masking:_ 
Code for masking colors and places dataset: https://colab.research.google.com/drive/1jh9l8yMKBatjH5JkZ8TB_3XIN6rNGmNT?usp=sharing

**Predictions & Evaluation:**

The files we modified for our reproduction are ``src/mlm_predict.py``, ``src/evaluator.py`` and ``happy-transformer/happytransformer/happy_transformer.py``.

To run the prediction code, navigate to this directory on your local computer. You would need to modify ``src/mlm_predict.py`` to ensure that only the code pertaining to the dataset you are considering is included, and that the code pertaining to the other two datasets is commented out. The code is clearly marked for each dataset using comments.

``python src/mlm_predict.py (bert-base OR roberta-base) data-484/<any_masked_input_file_WITHOUT_LABELS>.txt <any_output_filename>.jsonl``

The masked input files can be found in directory 'data-484'. The predictions made by the model in our runs can be found in the directory 'results-484'.

For evaluating the code, you need to edit the code in ``src/evaluator.py`` in your IDE to change the ``filepath`` to the output of the dataset under consideration produced by the model in .jsonl form. You can use any of our results in 'results-484', or run the code yourself using the instructions above. You also need to change ``truth_file`` to the corresponding masked input file (.txt) in the 'data-484' directory. You would also need to uncomment the code pertaining to the dataset you are considering, and comment out code pertaining to the other datasets in ``src/evaluator.py``.

This is the line of code you would need to run:
``python src/evaluator.py``

The results of the evaluation can be found in the 'images' directory, that shows our terminal outputs for each of these cases. In this directory, you can also find the graphs of the results of the color and size datasets.

The required tables (for location) and graphs are generated in the following file. This file is included in 'results-484': https://colab.research.google.com/drive/1rGcm5zgCSXH718qhRY7btMHn2HZacpxr?usp=sharing

Finally, we evaluate the content of the CC-News dataset (https://paperswithcode.com/dataset/cc-news). This code is also included in 'results-484': https://colab.research.google.com/drive/1f_zG1549bAQI-og-27jThyE0pXM0Jce4?usp=sharing
