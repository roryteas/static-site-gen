import unittest
from textnode_split_logic import *
from textnode import *


class TestTextNodeSplitLogic(unittest.TestCase):
    def test_text_node_splitting_bold(self):
        old_nodes = [TextNode("Hi **This Bold** this not",'text')]
        new_nodes = split_nodes_delimiter(old_nodes, '**', 'bold')
        self.assertEqual(len(new_nodes),3)
        self.assertEqual("Hi ",f"{new_nodes[0].text}")
        self.assertEqual("This Bold", f"{new_nodes[1].text}")
        self.assertEqual(" this not", f"{new_nodes[2].text}")
        self.assertEqual("bold",f"{new_nodes[1].text_type}")

    def test_text_node_splitting_italic(self):
        old_nodes = [TextNode("Hi *This italic* this not",'text')]
        new_nodes = split_nodes_delimiter(old_nodes, '*', 'italic')
        self.assertEqual(len(new_nodes),3)
        self.assertEqual("Hi ",f"{new_nodes[0].text}")
        self.assertEqual("This italic", f"{new_nodes[1].text}")
        self.assertEqual(" this not", f"{new_nodes[2].text}")
        self.assertEqual("italic",f"{new_nodes[1].text_type}")

    def test_text_node_splitting_code(self):
        old_nodes = [TextNode("Hi `This code` this not",'text')]
        new_nodes = split_nodes_delimiter(old_nodes, '`', 'code')
        self.assertEqual(len(new_nodes),3)
        self.assertEqual("Hi ",f"{new_nodes[0].text}")
        self.assertEqual("This code", f"{new_nodes[1].text}")
        self.assertEqual(" this not", f"{new_nodes[2].text}")
        self.assertEqual("code",f"{new_nodes[1].text_type}")

    def test_text_text_node_splitting_nosplit(self):
        old_nodes = [TextNode("Hi, no split in this one","text")]

        new_nodes = split_nodes_delimiter(old_nodes, '*', "italic")
        self.assertEqual(len(old_nodes),len(new_nodes))
        self.assertEqual(old_nodes[0],new_nodes[0])

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(f"{images}", f"{expected_images}")

    def test_extract_markdown_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        links = extract_markdown_links(text)
        expected_links = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(f"{links}", f"{expected_links}")

    def test_split_nodes_link_single(self):
        
        old_nodes = [TextNode("Hi, no split [rick roll](https://i.imgur.com/aKaOqIh.gif)in this one","text")]

        new_nodes = [TextNode("Hi, no split ","text"),TextNode("rick roll","link","https://i.imgur.com/aKaOqIh.gif"),TextNode("in this one","text")]

        self.assertEqual(split_nodes_link(old_nodes), new_nodes)

    def test_split_nodes_link_double(self):
        
        old_nodes = [TextNode("Hi, no split [rick roll](https://i.imgur.com/aKaOqIh.gif)in thi[dick roll](https://i.imgur.com/aKaOqIh.gif)s one","text")]

        new_nodes = [TextNode("Hi, no split ","text"),TextNode("rick roll","link","https://i.imgur.com/aKaOqIh.gif"),TextNode("in thi","text"),TextNode("dick roll","link","https://i.imgur.com/aKaOqIh.gif"),TextNode("s one","text")]

        self.assertEqual(split_nodes_link(old_nodes), new_nodes)


    def test_split_nodes_image_single(self):

        old_nodes = [TextNode("Hi, no split ![rick roll](https://i.imgur.com/aKaOqIh.gif)in this one","text")]

        new_nodes = [TextNode("Hi, no split ","text"),TextNode("rick roll","image","https://i.imgur.com/aKaOqIh.gif"),TextNode("in this one","text")]

        self.assertEqual(split_nodes_image(old_nodes), new_nodes)

    def test_split_nodes_image_double(self):
        
        old_nodes = [TextNode("Hi, no split ![rick roll](https://i.imgur.com/aKaOqIh.gif)in thi![dick roll](https://i.imgur.com/aKaOqIh.gif)s one","text")]

        new_nodes = [TextNode("Hi, no split ","text"),TextNode("rick roll","image","https://i.imgur.com/aKaOqIh.gif"),TextNode("in thi","text"),TextNode("dick roll","image","https://i.imgur.com/aKaOqIh.gif"),TextNode("s one","text")]

        self.assertEqual(split_nodes_image(old_nodes), new_nodes)
        
    def test_split_nodes_image_double_same(self):
        
        old_nodes = [TextNode("Hi, no split ![rick roll](https://i.imgur.com/aKaOqIh.gif)in thi![rick roll](https://i.imgur.com/aKaOqIh.gif)s one","text")]

        new_nodes = [TextNode("Hi, no split ","text"),TextNode("rick roll","image","https://i.imgur.com/aKaOqIh.gif"),TextNode("in thi","text"),TextNode("rick roll","image","https://i.imgur.com/aKaOqIh.gif"),TextNode("s one","text")]

        self.assertEqual(split_nodes_image(old_nodes), new_nodes)

    def test_split_nodes_image_no_split(self):

        old_nodes = [TextNode("Hi `This code` this not",'text')]
        self.assertEqual(split_nodes_image(old_nodes),old_nodes)

    def test_split_nodes_link_no_split(self):

        old_nodes = [TextNode("Hi `This code` this not",'text')]
        self.assertEqual(split_nodes_link(old_nodes),old_nodes)

    def test_text_to_nodes(self):
        text  = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        nodes = [
                TextNode("This is ", 'text'),
                TextNode("text", 'bold'),
                TextNode(" with an ", 'text'),
                TextNode("italic", 'italic'),
                TextNode(" word and a ", 'text'),
                TextNode("code block", 'code'),
                TextNode(" and an ", 'text'),
                TextNode("obi wan image", 'image', "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", 'text'),
                TextNode("link", 'link', "https://boot.dev"),
            ]
        self.assertEqual(text_to_textnodes(text),nodes)

    def test_text_to_nodes_no_splits(self):
        text = "the lazy brown dog jumped over the quick fox"
        nodes = [TextNode("the lazy brown dog jumped over the quick fox",'text')] 
        self.assertEqual(text_to_textnodes(text),nodes)
if __name__ == "__main__":
    unittest.main()
