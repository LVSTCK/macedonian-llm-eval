from datasets import load_dataset

# Load the dataset for the 'piqa' task
dataset = load_dataset("LVSTCK/macedonian-llm-eval", name="boolq")

# Print the dataset to confirm it loads
print(dataset)
