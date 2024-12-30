"""
This script/module is adapted from the original work by Aleksa Gordić.

Original Author: Aleksa Gordić  
Original Source: serbian-llm-eval 
Dataset URL: https://huggingface.co/datasets/gordicaleksa/serbian-llm-eval-v1/blob/main/serbian-llm-eval-v1.py 

Description:
This is an adaptation or copy of the Serbian LLM evaluation script from the above source. All credits for the original work go to Aleksa Gordić. 

If you find this work useful, please consider citing or acknowledging the original source.
"""


import json
import datasets

class MacedonianLLMConfig(datasets.BuilderConfig):
    """BuilderConfig for Macedonian LLM eval."""

    def __init__(self, features, **kwargs):
        """BuilderConfig for Macedonian LLM eval.
        Args:
          features: `list[string]`, list of the features that will appear in the
            feature dict.
          **kwargs: keyword arguments forwarded to super.
        """
        # Version history:
        # 0.0.1: Initial version.
        super(MacedonianLLMConfig, self).__init__(version=datasets.Version("0.0.1"), **kwargs)
        self.features = features


class SuperGlue(datasets.GeneratorBasedBuilder):
    """The Macedonian LLM eval."""

    BUILDER_CONFIGS = [
        MacedonianLLMConfig(
            name="arc_challenge",
            features=["query", "choices", "gold"],
        ),
        MacedonianLLMConfig(
            name="arc_easy",
            features=["query", "choices", "gold"],
        ),
        MacedonianLLMConfig(
            name="boolq",
            features=["question", "passage", "label"],
        ),
        MacedonianLLMConfig(
            name="hellaswag",
            features=["query", "choices", "gold"],
        ),
        MacedonianLLMConfig(
            name="nq_open",
            features=["question", "answer"],
        ),
        MacedonianLLMConfig(
            name="openbookqa",
            features=["query", "choices", "gold"],
        ),
        MacedonianLLMConfig(
            name="piqa",
            features=["goal", "choices", "gold"],
        ),
        MacedonianLLMConfig(
            name="triviaqa",
            features=["question", "answer"],
        ),
        MacedonianLLMConfig(
            name="winogrande",
            features=["sentence", "option1", "option2", "answer"],
        ),
    ]

    DEFAULT_CONFIG_NAME = "winogrande"

    def _info(self):
        features = {feature: datasets.Value("string") for feature in self.config.features}
        if self.config.name in ["arc_challenge", "arc_easy", "hellaswag", "openbookqa"]:
            features["query"] = datasets.Value("string")
            features["choices"] = datasets.features.Sequence(datasets.Value("string"))
            features["gold"] = datasets.Value("int32")
        elif self.config.name == "boolq":
            features["question"] = datasets.Value("string")
            features["passage"] = datasets.Value("string")
            features["label"] = datasets.Value("int32")
        elif self.config.name == "nq_open":
            features["question"] = datasets.Value("string")
            features["answer"] = datasets.features.Sequence(datasets.Value("string"))
        elif self.config.name == "piqa":
            features["goal"] = datasets.Value("string")
            features["choices"] = datasets.features.Sequence(datasets.Value("string"))
            features["gold"] = datasets.Value("int32")
        elif self.config.name == "triviaqa":
            features["question"] = datasets.Value("string")
            features["answer"] = dict(
                {
                    "value": datasets.Value("string"),
                    "aliases": datasets.features.Sequence(datasets.Value("string"))
                }
            )
        elif self.config.name == "winogrande":
            features["sentence"] = datasets.Value("string")
            features["option1"] = datasets.Value("string")
            features["option2"] = datasets.Value("string")
            features["answer"] = datasets.Value("string")

        return datasets.DatasetInfo(
            description="For details about Macedonian LLM eval see the README.",
            features=datasets.Features(features),
            homepage="https://huggingface.co/LVSTCK",
        )

    _DATASET_PATHS = {
        "arc_challenge": ["arc_challenge_test_partial_0_1171_end.jsonl"],
        "arc_easy": ["arc_easy_test_partial_0_2375_end.jsonl"],
        "boolq": ["boolq_test_partial_0_3269_end.jsonl"],
        "hellaswag": ["hellaswag_test_partial_0_10041_end.jsonl"],
        "nq_open": ["nq_open_test_partial_0_3609_end_end.jsonl", "nq_open_train_partial_0_87924_end.jsonl"],
        "openbookqa": ["openbookqa_test_partial_0_499_end.jsonl"],
        "piqa": ["piqa_test_partial_0_1837_end.jsonl"],
        "triviaqa": ["triviaqa_test_partial_0_17943_end.jsonl", "triviaqa_train_partial_0_138383_end.jsonl"],
        "winogrande": ["winogrande_test_partial_0_1266_end.jsonl"],
    }

    def _split_generators(self, dl_manager):
        dataset_paths = self._DATASET_PATHS[self.config.name]
        downloaded_filepaths = []
        for dataset_path in dataset_paths:
            downloaded_filepaths.append(dl_manager.download_and_extract(dataset_path))

        if self.config.name in ["triviaqa", "nq_open"]:
            assert len(downloaded_filepaths) == 2, "Expected a train and a test file."
            return [
                datasets.SplitGenerator(
                    name=datasets.Split.TRAIN,
                    gen_kwargs={
                        "data_file": downloaded_filepaths[1],
                        "split": datasets.Split.TRAIN,
                    },
                ),
                datasets.SplitGenerator(
                    name=datasets.Split.TEST,
                    gen_kwargs={
                        "data_file": downloaded_filepaths[0],
                        "split": datasets.Split.TEST,
                    },
                ),
            ]
        else:
            assert len(downloaded_filepaths) == 1, "Expected a single file."
            return [
                datasets.SplitGenerator(
                    name=datasets.Split.TEST,
                    gen_kwargs={
                        "data_file": downloaded_filepaths[0],
                        "split": datasets.Split.TEST,
                    },
                ),
            ]

    def _generate_examples(self, data_file, split):
        with open(data_file, encoding="utf-8") as f:
            for id, line in enumerate(f):
                row = json.loads(line)

                if self.config.name in ["arc_challenge", "arc_easy", "hellaswag", "openbookqa"]:
                    query = row["query"]
                    choices = row["choices"]
                    gold = row["gold"]

                    if "id" in row:
                        id = row["id"]
                    yield id, {
                        "query": query,
                        "choices": choices,
                        "gold": gold,
                    }
                elif self.config.name == "boolq":
                    question = row["question"]
                    passage = row["passage"]
                    label = row["label"]

                    id = row["idx"]
                    yield id, {
                        "question": question,
                        "passage": passage,
                        "label": label,
                    }
                elif self.config.name == "nq_open":
                    question = row["question"]
                    answer = row["answer"]
                    yield id, {
                        "question": question,
                        "answer": answer
                    }
                elif self.config.name == "piqa":
                    goal = row["goal"]
                    choices = row["choices"]
                    gold = row["gold"]
                    yield id, {
                        "goal": goal,
                        "choices": choices,
                        "gold": gold,
                    }
                elif self.config.name == "triviaqa":
                    question = row["question"]
                    answer = row["answer"]
                    pruned_answer = {
                        "value": answer["value"],
                        "aliases": answer["aliases"]
                    }
                    yield id, {
                        "question": question,
                        "answer": pruned_answer,
                    }
                elif self.config.name == "winogrande":
                    sentence = row["sentence"]
                    option1 = row["option1"]
                    option2 = row["option2"]
                    answer = row["answer"]
                    yield id, {
                        "sentence": sentence,
                        "option1": option1,
                        "option2": option2,
                        "answer": answer
                    }