from textnode import *

def text_to_textnodes(text):
    initial_node = TextNode(text,'text')
    nodes = [initial_node]
    nodes = split_nodes_delimiter(nodes,'**','bold')
    nodes = split_nodes_delimiter(nodes,'*','italic')
    nodes = split_nodes_delimiter(nodes,'`','code')
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []
    new_type = text_type
    for node in old_nodes:
        text = node.text
        delimiter_index = text.find(delimiter)
        if delimiter_index == -1:
            new_nodes.append(node)
        else:
            delimiter_index_2 = text[delimiter_index+1:].find(delimiter)
            if delimiter_index_2 == -1:
                new_nodes.append(node)
            else:
                new_node_text = text.split(delimiter)

                new_nodes.append(TextNode(new_node_text[0],node.text_type,node.url))
                new_nodes.append(TextNode(new_node_text[1],new_type)) 
                new_nodes.append(TextNode(new_node_text[2],node.text_type,node.url))

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text) 
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)",text) 
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:

        matches = extract_markdown_links(node.text)
        remaining_text = node.text 
        for match in matches:
            parts = remaining_text.split(f"[{match[0]}]({match[1]})",1)
            new_nodes.append(TextNode(parts[0],node.text_type,node.url))
            new_nodes.append(TextNode(match[0],'link',match[1]))
            length_to_remove = len(parts[0]) + len(match[0]) + len(match[1]) +  4 
            remaining_text = remaining_text[length_to_remove:]
        if len(remaining_text.strip())>0:
            new_nodes.append(TextNode(remaining_text,node.text_type,node.url))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        remaining_text = node.text 
        for match in matches:
            parts = remaining_text.split(f"![{match[0]}]({match[1]})",1)
            new_nodes.append(TextNode(parts[0],node.text_type,node.url))
            new_nodes.append(TextNode(match[0],'image',match[1]))
            length_to_remove = len(parts[0]) + len(match[0]) + len(match[1])  + 5 
            remaining_text = remaining_text[length_to_remove:]
        if len(remaining_text.strip())>0:
            new_nodes.append(TextNode(remaining_text,node.text_type,node.url))
            
    return new_nodes
