import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "undordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown):
    lines = markdown.split("\n")
    if (
        markdown.startswith("# ")
        or markdown.startswith("## ")
        or markdown.startswith("### ")
        or markdown.startswith("#### ")
        or markdown.startswith("##### ")
        or markdown.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return block_type_code
    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if markdown.startswith("*"):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if markdown.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i} "):
                return block_type_paragraph
            i += 1 
        return block_type_ordered_list
    return block_type_paragraph
