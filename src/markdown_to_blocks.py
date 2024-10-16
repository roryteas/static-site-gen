import re
from htmlnode import *
from textnode import *
from textnode_split_logic import *
def markdown_to_blocks(document):
    blocks = document.split('\n\n')
    stripped_blocks = list(map(lambda block: block.strip('\n ').strip(),blocks))
    return stripped_blocks

def block_to_block_type(block):
    if re.match(r"#{1,6} *",block):
        return 'heading'
    if re.match(r"\{3}\*\{3}",block):
        return 'code'
    if re.match(r"^(?:>\s?.*(?:\n>\s?.*)*)$",block,re.MULTILINE):
        return 'quote'
    if re.match(r"^(?:[-+*]\s+.*(?:\n[-+*]\s+.*)*)$",block,re.MULTILINE):
        return 'unordered-list'
    if re.match(r"^(?:\d+\.\s+.*(?:\n\d+\.\s+.*)*)$",block,re.MULTILINE):
        return 'ordered-list'
    else:
        return 'paragraph'

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        match block_to_block_type(block):
            case 'heading':
                child_nodes.append( header_block_to_html(block))
            case 'code':
                child_nodes.append( code_block_to_html(block))
            case 'quote':
                child_nodes.append( quote_block_to_html(block))
            case 'paragraph':
                child_nodes.append( paragraph_block_to_html(block))
            case 'unordered-list':
                child_nodes.append( unordered_list_block_to_html(block))
            case 'ordered-list':
                child_nodes.append( ordered_list_block_to_html(block))
    return ParentNode('div',child_nodes)
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return list(map(lambda node: text_node_to_html_node(node), textnodes))
    



def header_block_to_html(block):
    hash_count = 0
    for char in block[:6]:
        if char!= '#':
            break
        hash_count+=1
    tag = f"h{hash_count}"
    text = block[hash_count:]
    return ParentNode(tag,text_to_children(text))


def code_block_to_html(block):
    return ParentNode('code',text_to_children(block[3:-3]))


def quote_block_to_html(block):
    return ParentNode('blockquote',text_to_children(block[2:]))

def paragraph_block_to_html(block):
    return ParentNode('p',text_to_children(block))

def unordered_list_block_to_html(block):
    list_items = re.split('\n[\*\-] ',block)
    li_items = [HTMLNode('li',list_items[0][2:])]
    for item in list_items:
        li_items.append(ParentNode('li',text_to_children(item)))
    return ParentNode('ul',li_items)

def ordered_list_block_to_html(block):
    list_items = re.split('\n[\d+] ',block)
    li_items = [HTMLNode('li',list_items[0][3:])]
    for item in list_items:
        li_items.append(ParentNode('li',text_to_children(item)))
    return ParentNode('ol',li_items)


