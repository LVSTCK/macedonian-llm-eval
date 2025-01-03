#!/bin/bash

TASKS="arc_challenge,arc_easy,boolq,hellaswag,openbookqa,piqa,winogrande,nq_open"
BATCH_SIZE=8
LANGUAGE="Macedonian"

python3 main.py --language "$LANGUAGE" --model hf-causal-experimental --model_args "pretrained=trajkovnikola/MKLLM-7B-Instruct" --tasks $TASKS --batch_size $BATCH_SIZE --output_path "results_eval_mkllm"
python3 main.py --language "$LANGUAGE" --model hf-causal-experimental --model_args "pretrained=mistralai/Ministral-8B-Instruct-2410" --tasks $TASKS --batch_size $BATCH_SIZE --output_path "results_eval_mistral-8b-instruct-2410"
python3 main.py --language "$LANGUAGE" --model hf-causal-experimental --model_args "pretrained=Qwen/Qwen2.5-7B-Instruct" --tasks $TASKS --batch_size $BATCH_SIZE --output_path "results_eval_qwen"
python3 main.py --language "$LANGUAGE" --model hf-causal-experimental --model_args "pretrained=meta-llama/Llama-3.1-8B-Instruct" --tasks $TASKS --batch_size $BATCH_SIZE --output_path "results_eval_llama3.1_8b"
python3 main.py --language "$LANGUAGE" --model hf-causal-experimental --model_args "pretrained=meta-llama/Llama-3.2-3B-Instruct" --tasks $TASKS --batch_size $BATCH_SIZE --output_path "results_eval_llama3.2_3b"

echo "All evaluations completed successfully."