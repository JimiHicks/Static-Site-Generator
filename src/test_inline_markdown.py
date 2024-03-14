import unittest 
from inline_markdown import (
    split_nodes_delimiter,
    EXTRACT_MARKDOWN_IMAGES,
    EXTRACT_MARKDOWN_LINKS,
    split_image_nodes,
    split_link_nodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_double_bold(self):
        node = TextNode("This is text with a **bolded** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
            )
        

    def test_delim_double_bold(self):
        node = TextNode("This is text with a **bolded** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
            )  
        
    def test_delim_double_bold_multi_word(self):
        node = TextNode("This is text with a **bolded word** and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
            )
            
    def test_delim_italic(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_double_italic(self):
        node = TextNode("This is text with a *italic* word and *another*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_italic),
            ],
            new_nodes,
            )  

    def test_delim_code(self):
        node = TextNode("This is text with a `code` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_image(self):
        node = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        new_node = EXTRACT_MARKDOWN_IMAGES(node)
        self.assertEqual = new_node

    def test_extract_image(self):
        node = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        new_node = EXTRACT_MARKDOWN_LINKS(node)
        self.assertEqual = new_node

    def test_split_image(self):
        node = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        new_node = split_image_nodes(node)
        self.asserEqual = new_node

    def test_split_link(self):
        node = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        new_node = split_link_nodes(node)
        self.asserEqual = new_node

if __name__ == "__main__":
    unittest.main()
