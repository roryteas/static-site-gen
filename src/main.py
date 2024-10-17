import os
import shutil
from textnode import * 
from recursive_copy import *
from pathlib import Path
from markdown_to_blocks import *
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == 'heading' and block[1]!='#':
            return block[2:]
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = Path(from_path).read_text()
    node = markdown_to_html_node(markdown)
    html_code = node.to_html()
    title = extract_title(markdown)
    template = Path(template_path).read_text()
    template = template.replace('{{ Title }}',title)
    template = template.replace('{{ Content }}',html_code)
    print(f'writing html file to {dest_path}') 
    with open(dest_path, "w") as file:
        file.write(template)

def generate_page_recursive(from_path, template_path, dest_path):
    if not os.path.exists(dest_path):
        print(f"making directory {dest_path}")
        os.mkdir(dest_path)
    for item in os.listdir(from_path):
        if os.path.isfile(os.path.join(from_path,item)):
            print(f"converting {item} md from {from_path} to html in {dest_path}")
            generate_page(os.path.join(from_path,item),template_path,os.path.join(dest_path,f"{item[:-2]}html"))
        else:
            generate_page_recursive(os.path.join(from_path,item),template_path, os.path.join(dest_path,item))

            


def main():
    recursive_delete_dir('public')
    copy_dir_to_dir('static','public')
    generate_page_recursive('content','template.html','public')
if __name__ == "__main__":
    main()
