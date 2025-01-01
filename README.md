# Macedonian LLM eval 🇲🇰

This repository is adapted from the original work by Aleksa Gordić. If you find this work useful, please consider citing or acknowledging the original source.

## What is currently covered:
* Common sense reasoning: `Hellaswag`, `Winogrande`, `PIQA`, `OpenbookQA`, `ARC-Easy`, `ARC-Challenge`
* World knowledge: `NaturalQuestions`
* Reading comprehension: `BoolQ`

You can find the Macedonian LLM eval dataset [on HuggingFace](TODO). For more details on how the dataset was built see [this technical report](TODO) TODO. The datase was translated from Serbian to Macedonian using the Google Translate API. The Serbian dataset was selected as the source instead of English because Serbian and Macedonian are closer from a linguistic standpoint, making Serbian a better starting point for translation. Additionally, the Serbian dataset was refined using GPT-4, which, according to the original report, significantly improved the quality of the translation. Note that this is an assumption that needs further validation (quantitative).. a small quality check was conducted on the translated Macedonian dataset, and the results were deemed to be of good quality.

## Evaluation

If needed, you can extend the [script](https://huggingface.co/datasets/LVSTCK/macedonian-llm-eval/blob/main/macedonian-llm-eval.py) to support additional datasets. If you choose to do so, we encourage you to open a PR. For example, if you translate additional benchmarks, such as PubmedQA, from English to Macedonian and want to include it in this evaluation framework, you should first modify the corresponding evaluation script in lm_eval/tasks/<dataset_name>.py. For guidance, refer to the implementations for existing evaluations (e.g., ARC, SuperGLUE, HellaSwag, NQOpen, OpenBookQA).

To run the evaluation using the current version of [macedonian-llm-eval](https://huggingface.co/datasets/LVSTCK/macedonian-llm-eval) you can follow the steps below:

### Prerequisites
Before running the evaluation, ensure you have installed the necessary dependencies. First create an environment, e.g:

```bash
conda create -n mk_eval python==3.10
```

Then run: 
```bash
pip install -e .
```

### Run Evaluation
To evaluate a specific language model on a specific task run:
```
python3 main.py --language "Macedonian" --model gpt2 --tasks hellaswag,piqa --batch_size 1
```

Note that gpt is already supported in the lm_eval; if you wish to run a huggingface model then run:
```
python3 main.py --language "Macedonian" --model hf --model_args "pretrained=EleutherAI/gpt-neo-125m" --tasks hellaswag,piqa --batch_size 1
```


## Translation (optional; In case you want to translate any other dataset) 

* running this this will eat your google cloud credits or will bill you if you're already in the billing mode (this happens after you spend free credits and then deliberately enable billing again).

* you can use your free credits to translate 500.000 chars / month!

* if this is the first time you're creating a gcloud project you'll have 300$ of free credits!

## Prerequisites

Before you begin, ensure you meet the following requirements:

**For Linux Users:**

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

**For Windows Users:**
1. Windows Subsystem for Linux [(WSL2)](https://learn.microsoft.com/en-us/windows/wsl/install). If you don't have WSL2 installed, follow these steps in Windows cmd/powershell in administrator mode:

    ```bash
    wsl --install

   // Check version and distribution name.
   wsl -l -v

    // Set the newly downloaded linux distro as default.
    wsl --set-default <distribution name>
    ```
2. Install [Git](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git) from the WSL terminal.

    ```bash
    sudo apt update
    sudo apt install git
    git --version
    ```
3. Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) from the WSL terminal.
    ```bash
    mkdir -p ~/miniconda3

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

    rm -rf ~/miniconda3/miniconda.sh

    // Initialize conda with bash.
    ~/miniconda3/bin/conda init bash
    ```

4. Follow the instructions below on WSL.

## Instructions for translating lm harness eval from English into Slovenian

First let's setup a minimal Python program that makes sure you can run Google Translate on your local machine.

1. Create a Google Console project (https://console.cloud.google.com/)
2. Enable Google Translation API -> to enable it you have to setup the billing and input your credit card details (a note regarding safety: you'll have 300$ of free credit (if this is the first time you're doing it) and no one can spend money from your credit card unless all those free credits are spent and you re-enable the billing again! if you already had it setup in that case you have 500.000 chars/month for free!)
3. Install Google Cloud CLI (gsutil) on your machine (see this: https://cloud.google.com/storage/docs/gsutil_install/)

    a.) Download the Linux archive file (find latest version from link above)

     `curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-455.0.0-linux-x86_64.tar.gz`

    b.) Extract the contents from the archive file above.

    `tar -xf google-cloud-cli-455.0.0-linux-x86_64.tar.gz`

    c.) Run installation script. `./google-cloud-sdk/install.sh`

    d.) Initiate and authenticate your account. `./google-cloud-sdk/bin/gcloud init`

    e.) Create a credentials file with `gcloud auth application-default login`
4. Create and setting up the conda env

    a.) Open a terminal (if on Windows use the `WSL` terminal, if you're on Linux just use your terminal conda will already be in the PATH)

    b.) Run `conda create -n sr_mk_translate python=3.10 -y`

    c.) Run `conda activate sr_mk_translate`

    d.) Run  `pip install google-cloud-translate`


5. To run translation following these steps: 

    a.) Download the Serbian LLM evaluation dataset [Serbian LLM Eval](https://huggingface.co/datasets/gordicaleksa/serbian-llm-eval-v1/tree/main), or any other dataset of choice (just make sure to change the source language in translate.py - maybe the logic as well). 

    b.) Place the dataset in a data/ folder.

    c.) Navigate to the translate/ directory.

    d.) Set up the `config.py` file.

    e.) Run the translation script:
    ```bash
    python translate.py
    ```



## How to Contribute?

We welcome contributions to the Macedonian LLM Eval! If you'd like to contribute, here’s how you can get involved:

1. **Translate Popular Benchmarks**:  
   - Identify benchmarks that have not yet been translated into Macedonian. For example, PubmedQA, SQuAD, or any other popular datasets.  
   - Translate the dataset into Macedonian using appropriate tools or methods (e.g., Google Translate API).  

2. **Fork and Modify the Repository**:  
   - Fork this repo.  
   - Modify the necessary parts of the repository to support the new dataset. This includes:  
     - Updating the evaluation script (`lm_eval/tasks/<dataset_name>.py`) to include the new benchmark.  
     - Refer to existing implementations (e.g., ARC, SuperGLUE, HellaSwag) for guidance on how to implement evaluation logic.  

3. **Update and Modify the Script**:  
   - Edit the [evaluation script](https://huggingface.co/datasets/LVSTCK/macedonian-llm-eval/blob/main/macedonian-llm-eval.py) to include the new benchmark.  
   - Ensure all changes are tested and documented.  

4. **Open a PR**:  
   - Open a PR to submit your changes.  
   - In your PR description, detail the following:  
     - The benchmark you translated.  
     - The modifications you made to the code.  
     - How your changes were tested.  
   - If applicable, attach the modified evaluation script to your PR.  

By following these steps, you can help expand the Macedonian LLM Eval project and contribute to advancing the evaluation of Macedonian-language models. Thank you for your support!

## License

Apache 2.0
