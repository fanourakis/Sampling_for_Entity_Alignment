# Structural Bias in Knowledge Graphs for the Entity Alignment Task

The source code of the paper

## Getting Started

### Creating conda environment for RREA, sampling and analysis:
```bash
conda env create --file install/env.yml -n dev_env
```

### Creating conda environment for RDGCN and MultiKE:
```bash
cd RDGCN
conda env create --file install/OpenEA.yml -n openea_env
```

### Creating conda environment for PARIS:
```bash
cd PARIS
conda env create --file install/entity_match.yml -n entity_match
```

## Execution Examples

### For sampling:
```bash
python main.py start_sampling "configuration_name"
```

### For analysis:
```bash
python main.py start_analysis sampled "configuration_name"
```

### For running RREA:

```bash
python RREA.py original original (for original datasets)
```

or

```bash
python RREA.py sampled "configuration_name" (for sampled datasets)
```


### For running RDGCN you should first:
1) Download wiki-news-300d-1M.vec.zip from https://fasttext.cc/docs/en/english-vectors.html
2) Unzip wiki-news-300d-1M.vec.zip
3) Copy wiki-news-300d-1M.vec to /datasets
4) cd RDGCN and pip install -e .

```bash
cd run
python main_from_args.py args/original_rdgcn_args_15K.json (for original datasets)
```

or

```bash
cd run
python main_from_args.py args/sampled_rdgcn_args_15K.json (for sampled datasets)
```

### For running MultiKE:

```bash
cd run
python main_from_args_wo_attr.py args/original_multike_args_15K.json (for original datasets)
```

or

```bash
cd run
python main_from_args_wo_attr.py args/sampled_multike_args_15K.json (for sampled datasets)
```

### For running PARIS:

```bash
cd src/experiments
mkdir results
python3 -u ../run_experiment.py \
        --method PARIS\
        --root_dataset "root of dataset folder"\
        --dataset "configuration_name"\
        --dataset_division 721_5fold\
        --out_folder ./results\
        --use_func > test.log
```

or

```bash
cd src/experiments
mkdir results
python3 -u ../run_experiment.py \
        --method PARIS\
        --root_dataset "root of dataset folder"\
        --dataset original\
        --dataset_division 721_5fold\
        --out_folder ./results\
        --use_func > test.log
```