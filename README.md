# French Numbers Converter

This project provides a utility to convert numeric values into their corresponding French words. It's designed to handle numbers from 0 to millions.

## Installation

Before you can use the converter, you'll need to install it. This section guides you through the installation process.

### Setup
```bash
git clone https://github.com/lucaordronneau/french_numbers.git

cd french_numbers

pip install -r requirements.txt
```

### Usage
```python
from french_numbers_converter import FrenchNumberConverter

converter = FrenchNumberConverter()
print(converter.convert_to_french(123))  # Outputs: cent-vingt-trois
```

### Run test
```bash
python -m unittest discover -s tests
```

## Informations
Algorithm, Architecture and Code Cleaning:  ~ 2h15

Unit Test, GitHub, README: ~ 20 min

### Copilot, LLMs (ChatGPT)
Prompt:

- Provide unit tests for this function (function convert_to_french)
- Provide the README structure for a project
- How to decompose a number recursively starting by thousands

