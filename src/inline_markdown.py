import re 

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, bold section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def EXTRACT_MARKDOWN_IMAGES(TEXT):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", TEXT)
    return images

def EXTRACT_MARKDOWN_LINKS(TEXT):
    return re.findall(r"\[(.*?)\]\((.*?)\)", TEXT)

def split_image_nodes(old_nodes):
    new_list = []
    for node in old_nodes:
        if node != text_type_image:
            new_list.append(node)
            continue
        split_nodes = []
        extracted_images = EXTRACT_MARKDOWN_IMAGES(node)
        sections = node.text.split(f"![{extracted_images[0]}]({extracted_images[1]})", 1)
        for i in range(len(sections)):
            if i == "":
                continue
            else:
                split_nodes.append(TextNode(sections[i], extracted_images))
        new_list.extend(split_nodes)
    return new_list

def split_link_nodes(old_nodes):
    new_list = []
    for node in old_nodes:
        if node != text_type_link:
            new_list.append(node)
            continue
        split_nodes = []
        extracted_links = EXTRACT_MARKDOWN_LINKS(node)
        sections = node.text.split(f"[{extracted_links[0]}]({extracted_links[1]})", 1)
        for i in range(len(sections)):
            if i == "":
                continue
            else:
                split_nodes.append(TextNode(sections[i], extracted_links))
        new_list.extend(split_nodes)
    return new_list
