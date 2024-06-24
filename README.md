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
To reproduce the results from the research paper and conduct similar analyses, follow these steps. The cTOP model requires three types of input data: paired bulk RNA-seq & ATAC-seq and scRNA-seq data, all of which can be found in the supplementary data of the publication. For ease of use, the `Input` folder already includes the regulatory network generated from the paired bulk RNA-seq & ATAC-seq data via the PECA model, detailed at the [PECA repository](https://github.com/SUwonglab/PECA). This setup allows you to focus solely on downloading the scRNA-seq data to replicate the study's findings.

To run the cTOP model, execute the following command in your terminal:

```bash
bash run_cTOP.sh $sample
```

`$sample` is the name of the sample you are analyzing. For this example, use `POPP_B` as the sample name.

Results from the cTOP model can be saved in the `Results` folder for easy reference (this folder might need to be created before running the model to store the results).

## File Structure
- `src/`: Contains the source code for the cTOP model.
- `tools/`: Contains the tools for the cTOP model.
- `main/`: Contains main code for the cTOP model.
- `example/`: Contains example input data for testing.
- `requirements.txt`: Lists the Python packages required to run the cTOP model.

## Reference
This work is based on the following paper:
Li, Z., Xu, Z., Zhu, L., Qin, T., Ma, J., Feng, Z., Yue, H., Guan, Q., Zhou, B., Han, G., Zhang, G., Li, C., Jia, S., Qiu, Q., Hao, D., Wang, Y., & Wang, W. (2024). High-quality sika deer omics data and integrative analysis reveal genic and cellular regulation of antler regeneration. *Genome Research*, 12(3), 123-145.

## Contact
For any questions or issues, please contact:
- Ziyu Xu: [xuziyu231@mails.ucas.ac.cn](mailto:xuziyu231@mails.ucas.ac.cn)
