import json
import time
from pathlib import Path
from google.cloud import translate_v2 as translate
from typing import Dict, List, Any
import logging
from .config import DATASET_CONFIGS

class DatasetTranslator:
    def __init__(self, source_lang: str = 'sr', target_lang: str = 'mk'):
        self.client = translate.Client()
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('translation.log'),
                logging.StreamHandler()
            ]
        )
        
    def translate_text(self, text: str, retry_count: int = 2) -> str:
        """Translate text with retry mechanism and rate limiting."""
        if not text or text.isspace():
            return text
            
        for attempt in range(retry_count):
            try:
                time.sleep(0.1)  # Basic rate limiting
                result = self.client.translate(
                    text, 
                    source_language=self.source_lang,
                    target_language=self.target_lang
                )
                return result['translatedText']
            except Exception as e:
                logging.error(f"Translation error on attempt {attempt + 1}: {str(e)}")
                if attempt == retry_count - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff

    def translate_with_template(self, query: str) -> str:
        """Translate query using a template to preserve structure."""
        # Add placeholder to maintain structure
        template = f"{query} _____"
        translated = self.translate_text(template)
        # Remove placeholder
        return translated.replace("_____", "").strip()

    def translate_choices(self, choices: List[str]) -> List[str]:
        return [self.translate_text(choice) for choice in choices]

    def process_template_dataset(self, data: Dict) -> Dict:
        """Process datasets that need template-based translation."""
        result = data.copy()
        
        # Translate query using a template
        if 'query' in data:
            result['query'] = self.translate_with_template(data['query'])
            
        # Translate choices normally
        if 'choices' in data:
            result['choices'] = self.translate_choices(data['choices'])
            
        return result

    def process_normal_dataset(self, data: Dict, fields_to_translate: List[str]) -> Dict:
        """Process datasets that does not need template-based translation."""
        result = data.copy()
        for field in fields_to_translate:
            if field in data:
                if isinstance(data[field], list):
                    result[field] = [self.translate_text(item) for item in data[field]]
                else:
                    result[field] = self.translate_text(data[field])
        return result

    def process_dataset(self, input_file: str, output_file: str, config: Dict):
        """Process a dataset file with specified configuration."""
        input_path = Path(input_file)
        output_path = Path(output_file)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")
            
        output_path.parent.mkdir(parents=True, exist_ok=True)
        processed_count = 0
        error_count = 0
        logging.info(f"Starting translation of {input_file}")
        
        with input_path.open('r', encoding='utf-8') as infile, \
             output_path.open('w', encoding='utf-8') as outfile:
            
            for line_num, line in enumerate(infile, 1):
                try:
                    data = json.loads(line)
                    
                    if config.get('use_template', False):
                        translated_data = self.process_template_dataset(data)
                    else:
                        translated_data = self.process_normal_dataset(data, config['fields'])
                    
                    outfile.write(json.dumps(translated_data, ensure_ascii=False) + '\n')
                    processed_count += 1
                    
                    if processed_count % 100 == 0:
                        logging.info(f"Processed {processed_count} items")
                        
                except Exception as e:
                    error_count += 1
                    logging.error(f"Error processing line {line_num}: {str(e)}")
                    continue
        
        logging.info(f"Translation completed. Processed: {processed_count}, Errors: {error_count}")

def main():
    translator = DatasetTranslator()
    for config in DATASET_CONFIGS:
        try:
            logging.info(f"Processing dataset: {config['input_file']}")
            translator.process_dataset(
                config['input_file'],
                config['output_file'],
                config
            )
        except Exception as e:
            logging.error(f"Failed to process dataset {config['input_file']}: {str(e)}")

if __name__ == "__main__":
    main()