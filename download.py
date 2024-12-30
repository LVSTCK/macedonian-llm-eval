from huggingface_hub import hf_hub_download, login

login(token="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")
repo_id = "gordicaleksa/serbian-llm-eval-v1"  
destination_directory = "data/"

jsonl_files = [
    "arc_challenge_test_partial_0_1171_end.jsonl",
    "arc_easy_test_partial_0_2375_end.jsonl",
    "boolq_test_partial_0_3269_end.jsonl",
    "hellaswag_test_partial_0_10041_end.jsonl",
    "nq_open_test_partial_0_3609_end_end.jsonl",
    "nq_open_train_partial_0_87924_end.jsonl",
    "openbookqa_test_partial_0_499_end.jsonl",
    "piqa_test_partial_0_1837_end.jsonl",
    "triviaqa_test_partial_0_17943_end.jsonl",
    "triviaqa_train_partial_0_138383_end.jsonl",
    "winogrande_test_partial_0_1266_end.jsonl"
]

for file_name in jsonl_files:
    print(f"Downloading {file_name} from {repo_id}...")
    file_path = hf_hub_download(
        repo_id=repo_id,
        filename=file_name,
        repo_type="dataset",  
        local_dir=destination_directory  
    )
    print(f"File downloaded to: {file_path}")
