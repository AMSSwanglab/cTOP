# cTOP: Combinatorial Transcription Factor Oriented Program

## Introduction
This repository contains the implementation of the cTOP (Combinatorial Transcription Factor Oriented Program) model used in the research paper "High-quality sika deer omics data and integrative analysis reveal genic and cellular regulation of antler regeneration." The cTOP model integrates single-cell RNA-seq data with bulk regulatory networks to uncover the regulation of key cellular programs during antler regeneration.

## Installation
To use the cTOP model, please follow the steps below to set up your environment.

### Prerequisites
- MATLAB R2014b or higher
- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/AMSSwanglab/cTOP_new.git
    cd cTOP
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the cTOP model, use the provided scripts with the appropriate input data. Below is an example of how to run the main script:

```bash
python run_cTOP.py --input data/input_data.csv --output results/output_results.csv
```

### Arguments
- `--input`: Path to the input data file.
- `--output`: Path to save the output results.

### Example
You can find example input data and expected output in the `example` directory. To test the model with the example data, run:

```bash
python run_cTOP.py --input example/RAd4.csv --output example/RAd4.csv
```

## File Structure
- `src/`: Contains the source code for the cTOP model.
- `tools/`: Contains the tools for the cTOP model.
- `main/`: Contains main code for the cTOP model.
- `example/`: Contains example input data for testing.
- `requirements.txt`: Lists the Python packages required to run the cTOP model.

## Contact
For any questions or issues, please contact:
- Ziyu Xu: [xuziyu231@mails.ucas.ac.cn](mailto:xuziyu231@mails.ucas.ac.cn)
