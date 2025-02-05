# OpenAI Deep Research Link Cleaner

A specialized Python script that fixes the formatting of citation links in OpenAI's deep research output. This tool solves a specific issue where copying deep research results produces Markdown links that don't match OpenAI's displayed format, ensuring consistent and professional-looking citations in your research documents.

## Table of Contents
- [Purpose](#purpose)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Purpose

When you copy deep research results from OpenAI, the citations appear as domain names in parentheses, but the actual Markdown links don't match this format. This tool fixes that by:

- Extracting domain names from citation URLs
- Formatting links as `[domain.com](full_url)` for consistent appearance
- Removing 'www.' prefix from domains for cleaner display
- Preserving the full URL as the link destination

## Usage

### Basic Usage (Overwrite Original File)

```bash
python3 openai_deep_research_link_cleaner.py input.md
```

### Create New File (Non-destructive)

```bash
python3 openai_deep_research_link_cleaner.py input.md -o output.md
```

## Example

Original deep research output when copied:
```markdown
[Title of the research](https://www.example.com/research/paper)
```

After processing:
```markdown
[example.com](https://www.example.com/research/paper)
```

This matches how the citations appear in OpenAI's interface, making your research documents more consistent and professional.

## Requirements

- Python 3.x
- No additional packages required

## Installation

1. Clone this repository
2. Ensure Python 3.x is installed
3. The script is ready to use

## Command Line Arguments

- `file_path`: Path to the Markdown file to process (required)
- `-o, --output`: Output file path (optional). If not specified, updates the input file

## Contributing

Contributions are welcome! Here's how you can help:

- Report bugs by opening an issue
- Suggest new features or improvements
- Submit pull requests

Please ensure your code follows PEP 8 style guidelines for Python code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Notes

- Preserves all other Markdown formatting
- Only modifies citation links
- Maintains the full URL as the link destination
- Version: 1.0.0
