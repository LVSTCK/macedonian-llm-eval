""" Configuration file for translation. 


For some of the datasets we use a template-based translation approach to preserve structure
## Example: 
# {"id": "7-942", "query": "Hladnokrvne životinje su često", "choices": ["brze", "velike", "bez dlake", "spore"], "gold": 2}

# If we translate only the query as a standalone entity we get:
# Често се ладнокрвни животни

# However, if we translate it with one choice lets say  "velike":
# Ладнокрвните животни често се големи

# This is why we use a template-based approach to preserve structure; e.g. we add a placeholder "_____" to the query:
# "Hladnokrvne životinje su često _____" and then translate it to get the correct structure:
# "Ладнокрвните животни често се _____"

"""

DATASET_CONFIGS = [
    {
        'input_file': '../data/hellaswag_test_partial_0_10041_end.jsonl',
        'output_file': '../translated/hellaswag_test_mk.jsonl',
        'fields': ['query', 'choices'],
        'use_template': False  # From inspection, this dataset doesn't need template-based translation
    },
    # {
    #     'input_file': '../data/boolq_test_partial_0_3269_end.jsonl',
    #     'output_file': '../translated/boolq_test_mk.jsonl',
    #     'fields': ['question', 'passage'],
    #     'use_template': False # This does not need template-based translation
    # },
    # {
    #     'input_file': '../data/nq_open_test_partial_0_3609_end_end.jsonl',
    #     'output_file': '../translated/nq_open_test_mk.jsonl',
    #     'fields': ['question', 'answer'],
    #     'use_template': False # This does not need template-based translation
    # },
    # {
    #     'input_file': '../data/openbookqa_test_partial_0_499_end.jsonl',
    #     'output_file': '../translated/openbookqa_test_mk.jsonl',
    #     'fields': ['query', 'choices'],
    #     'use_template': True  # Enable template-based translation for this dataset
    # },
    # {
    #     'input_file': '../data/piqa_test_partial_0_1837_end.jsonl',
    #     'output_file': '../translated/piqa_test_mk.jsonl',
    #     'fields': ['goal', 'choices'],
    #     'use_template': False # Does not seem like its needed, although it could be used; Will leave it as False
    # },
    # {
    #     'input_file': '../data/nq_open_train_partial_0_87924_end.jsonl',
    #     'output_file': '../translated/nq_open_train_mk.jsonl',
    #     'fields': ['question', 'answer'],
    #     'use_template': False # This does not need template-based translation
    # },
    # {
    #     'input_file': '../data/winogrande_test_partial_0_1266_end.jsonl',
    #     'output_file': '../translated/winogrande_test_mk.jsonl',
    #     'fields': ['sentence', 'option1', 'option2'],
    #     'use_template': True # Enable template-based translation for this dataset
    # },
    # {
    #     'input_file': '../data/arc_challenge_test_partial_0_1171_end.jsonl',
    #     'output_file': '../translated/arc_challenge_test_mk.jsonl',
    #     'fields': ['query', 'choices'],
    #     'use_template': True # Enable template-based translation for this dataset
    # },
    # {
    #     'input_file': '../data/arc_easy_test_partial_0_2375_endd.jsonl',
    #     'output_file': '../translated/arc_easy_test_mk.jsonl',
    #     'fields': ['query', 'choices'],
    #     'use_template': True # Enable template-based translation for this dataset
    # },
]