# COS484: Final Project

This reproduction expands on the _NumerSense_ paper (https://arxiv.org/abs/2005.00683) to attempt to induce commonsense knowledge of pre-trained language models like BERT-Base and RoBERTa-Base in the domains of color, size and location.

We clone the original codebase used by the authors of that paper and add to it. You can find the original Github here: https://github.com/INK-USC/NumerSense/tree/main

Please follow the instructions listed in THEIR readme for running the code locally. 

**Compiling Datasets:**

Each of the following files can also be found in the directories, 'color', 'size', 'location' and 'masking'. The intermediate datasets from different points while cleaning the data can be found in 'intermediate-datasets'. The final datasets used can be found in 'data-484'.

_Color:_

Extracting examples from ConceptNet and OMCS: https://colab.research.google.com/drive/1oCKCbsc5AqS8RUGXkutecp8EW4wyBTkc?usp=sharing

Cleaning the data and selecting 3,000 examples: https://colab.research.google.com/drive/1LRRhXx2n8_FdmCAWo-3W7J6yeLgVCgjG?usp=sharing

_Size:_

_Location:_

_Masking:_ 
Code for masking colors and places dataset: https://colab.research.google.com/drive/1jh9l8yMKBatjH5JkZ8TB_3XIN6rNGmNT?usp=sharing

Predictions & Evaluation:

The files we modified for our reproduction are ``src/mlm_predict.py``, ``src/evaluator.py`` and ``happy-transformer/happytransformer/happy_transformer.py``.

To run the prediction code, navigate to this directory on your local computer and run the following in the command line:

``python src/mlm_predict.py <any_masked_input_file_WITHOUT_LABELS>.txt <any_output_filename>.jsonl``

