# cTOP: Combinatorial Transcription Factor Oriented Program

## Introduction
This repository contains the implementation of the cTOP (Combinatorial Transcription Factor Oriented Program) model used in the research paper "High-quality sika deer omics data and integrative analysis reveal genic and cellular regulation of antler regeneration." The cTOP model integrates single-cell RNA-seq data with bulk regulatory networks to uncover the regulation of key cellular programs during antler regeneration.

## Installation
To use the cTOP model, please follow the steps below to set up your environment.

### Prerequisites
- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/cTOP.git
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
python run_ctop.py --input data/input_data.csv --output results/output_results.csv
```

### Arguments
- `--input`: Path to the input data file.
- `--output`: Path to save the output results.

### Example
You can find example input data and expected output in the `examples` directory. To test the model with the example data, run:

```bash
python run_ctop.py --input examples/input_data.csv --output examples/output_results.csv
```

## File Structure
- `src/`: Contains the source code for the cTOP model.
- `data/`: Directory for input data files.
- `results/`: Directory where output results will be saved.
- `examples/`: Contains example input data and output results for testing.
- `requirements.txt`: Lists the Python packages required to run the cTOP model.
- `run_ctop.py`: Main script to execute the cTOP model.

## Contact
For any questions or issues, please contact the corresponding authors:
- Wen Wang: [wenwang@nwpu.edu.cn](mailto:wenwang@nwpu.edu.cn)
- Yong Wang: [ywang@amss.ac.cn](mailto:ywang@amss.ac.cn)
- Dingjun Hao: [haodingjun@mail.xjtu.edu.cn](mailto:haodingjun@mail.xjtu.edu.cn)
- Qiang Qiu: [qiuqiang@nwpu.edu.cn](mailto:qiuqiang@nwpu.edu.cn)
