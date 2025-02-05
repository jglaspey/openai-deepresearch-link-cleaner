#!/usr/bin/env python3
"""
OpenAI Deep Research Link Cleaner
Version 1.0.0

A tool to fix the formatting of citation links in OpenAI's deep research output,
ensuring they match the displayed format with domain names as visible text.
"""

import re
from urllib.parse import urlparse
import argparse

__version__ = '1.0.0'

def clean_markdown_links(file_path, output_path=None):
    # Read the markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def replace_link(match):
        # Get the full match
        full_match = match.group(0)
        # Get the URL from the match
        url = match.group(2)
        
        # Parse the URL to get the domain
        try:
            parsed_url = urlparse(url)
            # Get domain without www.
            domain = parsed_url.netloc.replace('www.', '')
            
            # If there's no domain (perhaps due to malformed URL), use the URL as is
            if not domain:
                return full_match
                
            # Return markdown link with domain as anchor text and parentheses outside
            return f'[{domain}]({url})'
            
        except Exception:
            # If URL parsing fails, return the original match
            return full_match
    
    # Regular expression to match Markdown links
    # This will match both [...](url) and [](url) formats
    # Include the link text in the regex
    pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    
    # Replace all matches using the replace_link function
    modified_content = re.sub(pattern, replace_link, content)
    
    # If no output path specified, use the input path (overwrite)
    final_output_path = output_path if output_path else file_path
    
    # Write the modified content to the file
    with open(final_output_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    
    return final_output_path

def main():
    parser = argparse.ArgumentParser(
        description='Fix OpenAI deep research citation links by using domain names as visible text.',
        epilog='Example: %(prog)s input.md -o output.md')
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('file_path', help='Path to the markdown file to process')
    parser.add_argument('-o', '--output', help='Output file path (if not specified, overwrites input file)', default=None)
    args = parser.parse_args()
    
    output_path = clean_markdown_links(args.file_path, args.output)
    if args.output:
        print(f"Successfully processed {args.file_path}")
        print(f"Created new file: {output_path}")
    else:
        print(f"Successfully processed and updated {args.file_path}")

if __name__ == "__main__":
    main()
