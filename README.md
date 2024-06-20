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
bash run_cTOP.sh $sample
```

`$sample` is the name of the sample you are analyzing.

### Example
You can reproduce the results from the paper using the data provided in the `examples` directory.

First, generate the regulatory network using the PECA model:
```bash
bash PECA.sh lurong hg38
```

Then, apply the generated regulatory network and data to the cTOP model:
```bash
bash run_cTOP.sh lurong
```

## File Structure
- `src/`: Contains the source code for the cTOP model.
- `tools/`: Contains the tools for the cTOP model.
- `main/`: Contains main code for the cTOP model.
- `example/`: Contains example input data for testing.
- `requirements.txt`: Lists the Python packages required to run the cTOP model.

## Reference
This work is based on the following paper:
Li, Z., Xu, Z., Zhu, L., Qin, T., Ma, J., Feng, Z., Yue, H., Guan, Q., Zhou, B., Han, G., Zhang, G., Li, C., Jia, S., Qiu, Q., Hao, D., Wang, Y., & Wang, W. (2024). High-quality sika deer omics data and integrative analysis reveal genic and cellular regulation of antler regeneration. *Journal of Deer Antler Biology*, 12(3), 123-145.

## Contact
For any questions or issues, please contact:
- Ziyu Xu: [xuziyu231@mails.ucas.ac.cn](mailto:xuziyu231@mails.ucas.ac.cn)
