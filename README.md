# Macedonian LLM eval 🇲🇰

This repository is adapted from the original work by [Aleksa Gordić](https://github.com/gordicaleksa/serbian-llm-eval). If you find this work useful, please consider citing or acknowledging the original source.

## 🎯 What is currently covered:
* Common sense reasoning: `Hellaswag`, `Winogrande`, `PIQA`, `OpenbookQA`, `ARC-Easy`, `ARC-Challenge`
* World knowledge: `NaturalQuestions`
* Reading comprehension: `BoolQ`

You can find the Macedonian LLM eval dataset [on HuggingFace](https://huggingface.co/datasets/LVSTCK/macedonian-llm-eval). The dataset was translated from Serbian to Macedonian using the Google Translate API. The Serbian dataset was selected as the source instead of English because Serbian and Macedonian are closer from a linguistic standpoint, making Serbian a better starting point for translation. Additionally, the Serbian dataset was refined using GPT-4, which, according to the original report, significantly improved the quality of the translation. 
<p>
    Quality check was conducted on the translated Macedonian dataset, and the translations were deemed to be of good quality.
</p>

---

## 📊 Latest Results - January 8, 2025

![output](https://github.com/user-attachments/assets/d644ec36-a1ad-42e4-8c59-4d745106b5f1)

---


| Model                                                                                  | Version | Multilingual Support | Macedonian Explicit Support | ARC Easy              | ARC Challenge         | Bool Q               | HellaSwag            | Openbook QA          | PIQA                 | NQ Open             | WinoGrande          | Notes                                                                 |
|----------------------------------------------------------------------------------------|---------|-----------------------|-----------------------------|-----------------------|-----------------------|----------------------|----------------------|----------------------|----------------------|---------------------|---------------------|----------------------------------------------------------------------|
| MKLLM-7B-Instruct [(trajkovnikola/MKLLM-7B-Instruct)](https://huggingface.co/trajkovnikola/MKLLM-7B-Instruct) | 7B      | Yes                   | Yes                         | 0.5034 ± 0.0103   | 0.3003 ± 0.0134   | 0.7878 ± 0.0072  | 0.4328 ± 0.0049  | **0.2940 ± 0.0204**  | 0.6420 ± 0.0112  | 0.0432 ± 0.0034 | **0.6148 ± 0.0137** |                                                                      |
| BLOOM [(bigscience/bloomz-7b1)](https://huggingface.co/bigscience/bloomz-7b1)          | 7B      | Yes                   | Yes                         | 0.2774 ± 0.0092       | 0.1800 ± 0.0112       | 0.5028 ± 0.0087      | 0.2664 ± 0.0044      | 0.1580 ± 0.0163      | 0.5316 ± 0.0116      | 0                   | 0.4964 ± 0.0141      | NQ is exact match, that's why the score is so low.                     |
| Phi-3.5-mini [(microsoft/Phi-3.5-mini-instruct)](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)             | 3.8B    | Yes               | No                          | 0.2887 ± 0.0093       | 0.1877 ± 0.0114       | 0.6028 ± 0.0086      | 0.2634 ± 0.0044      | 0.1640 ± 0.0166      | 0.5256 ± 0.0117      | 0.0025 ± 0.0008     | 0.5193 ± 0.0140     |                                                                      |
| Mistral [(mistralai/Ministral-8B-Instruct-2410)](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410)       | 7B      | Yes               | No                          | 0.4625 ± 0.0102       | 0.2867 ± 0.0132       | 0.7593 ± 0.0075      | 0.3722 ± 0.0048      | 0.2180 ± 0.0185      | 0.5783 ± 0.0115      | 0.0241 ± 0.0026     | 0.5612 ± 0.0139     |                                                                      |
| Mistral-Nemo [(mistralai/Mistral-Nemo-Instruct-2407)](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | 12B     | Yes               | No                          | 0.4718 ± 0.0102   | 0.3191 ± 0.0134   | 0.8086 ± 0.0072  | 0.3997 ± 0.0049  | 0.2420 ± 0.0185  | 0.6066 ± 0.0112  | 0.0291 ± 0.0034 | 0.6062 ± 0.0137 |                                                                      |
| Qwen2.5 [(Qwen/Qwen2.5-7B-Instruct)](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)                                | 7B      | Yes               | No                          | 0.3906 ± 0.0100       | 0.2534 ± 0.0127       | 0.7789 ± 0.0073      | 0.3390 ± 0.0047      | 0.2160 ± 0.0184      | 0.5598 ± 0.0116      | 0.0042 ± 0.0011     | 0.5351 ± 0.0140     |                                                                      |
| LLaMA 3.1 [(meta-llama/Llama-3.1-8B-Instruct)](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)               | 8B      | Yes               | No                          | 0.4453 ± 0.0102       | 0.2824 ± 0.0132       | 0.7639 ± 0.0074      | 0.3740 ± 0.0048      | 0.2520 ± 0.0194      | 0.5865 ± 0.0115      | 0.0335 ± 0.0030     | 0.5683 ± 0.0139     |                                                                      |
| LLaMA 3.2 [(meta-llama/Llama-3.2-3B-Instruct)](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)               | 3B      | Yes               | No                          | 0.3224 ± 0.0096       | 0.2329 ± 0.0124       | 0.6624 ± 0.0083      | 0.2976 ± 0.0046      | 0.2060 ± 0.0181      | 0.5462 ± 0.0116      | 0.0044 ± 0.0011     | 0.5059 ± 0.0141     |                                                                      |
| **🏆LLaMA 3.3 - 8bit** [(cortecs/Llama-3.3-70B-Instruct-FP8-Dynamic)](cortecs/Llama-3.3-70B-Instruct-FP8-Dynamic)               | 70B      | Yes               | No                          | **0.5808 ± 0.0101**       |  **0.3686 ± 0.0141**       | **0.8511 ± 0.0062**      | **0.4656 ± 0.0050**      | 0.2820 ± 0.0201      | **0.6600 ± 0.0111**      | **0.0878 ± 0.0047**     | 0.6093 ± 0.0137     |                                                                      |



---

## 📋Evaluation
To run the evaluation using the current version of [macedonian-llm-eval](https://huggingface.co/datasets/LVSTCK/macedonian-llm-eval) you can follow the steps below:

### Prerequisites
Before running the evaluation, ensure you have installed the necessary dependencies. First create an environment, e.g:

```bash
conda create -n mk_eval python==3.10
conda activate mk_eval              
```

Then run: 
```bash
pip install -e .
```

### Run Evaluation
To evaluate a specific language model on a specific task run:
```
python3 main.py --language "Macedonian" --model hf-causal-experimental --model_args "pretrained=microsoft/Phi-3.5-mini-instruct" --tasks arc_challenge,arc_easy,boolq,hellaswag,openbookqa,piqa,winogrande --batch_size 8 --output_path "results_eval"
```

*Info: You can run the evaluation for Serbian and Slovenian as well, just swap Macedonian with either one of them.* 

## 🈂️ (Optional) Translation

* running this this will eat your google cloud credits or will bill you if you're already in the billing mode (this happens after you spend free credits and then deliberately enable billing again).

* you can use your free credits to translate 500.000 chars / month!

* if this is the first time you're creating a gcloud project you'll have 300$ of free credits!

### Prerequisites

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

## 📗 Instructions for translating from Serbian into Macedonian

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

## 🤝 How to Contribute?

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


## 📝 TODOs

- ⬜️ Add COPA-MK to the eval (https://huggingface.co/datasets/classla/COPA-MK)
