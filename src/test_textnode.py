import unittest
from textnode_split_logic import *
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node","bold")
        node2 = TextNode("This is a text node","bold")
        self.assertEqual(node, node2)
    def test_eq_url(self):
        node = TextNode("This is a text node","bold","www.cats.com")
        node2 = TextNode("This is a text node","bold","www.cats.com")
        self.assertEqual(node,node2)

    def test_eq_none(self):
        node = TextNode("This is a text node","bold",None)
        node2 = TextNode("This is a text node","bold")
        self.assertEqual(node,node2)

    def test_eq_difftext(self):
        node = TextNode("This is a pretext node","bold")
        node2 = TextNode("This is a text node","bold")
        self.assertNotEqual(node,node2)

    def test_eq_diff_url(self):
        node = TextNode("This is a text node","bold","www.cat.com")
        node2 = TextNode("This is a text node","bold","www.cats.com")
        self.assertNotEqual(node,node2)

    def test_eq_diff_style(self):
        node = TextNode("This is a text node","old","www.cats.com")
        node2 = TextNode("This is a text node","bold","www.cats.com")
        self.assertNotEqual(node,node2)

    def test_text_node_to_html_node(self):
        textnode = TextNode("This is a text node","bold")
        leafnode = LeafNode("b","This is a text node")

        self.assertEqual(f"{text_node_to_html_node(textnode)}",f"{leafnode}")

    def test_text_node_to_html_node_div(self):
        textnode = TextNode("This is a text node","div")
        self.assertRaises(Exception, text_node_to_html_node, textnode)

    def test_print_created_leaf_node_bold(self):
        textnode = TextNode("e","bold")
        leafnode = LeafNode(tag="b", value = "e")
        expected_result = "LeafNode(tag=b, value=e, props=None"
        self.assertEqual(f"{text_node_to_html_node(textnode)}", expected_result)

    def test_textnode_to_htmlnode_link(self):
        textnode = TextNode("Anchor Text","link","www.anchor.com")
        leafnode = LeafNode("a", "Anchor Text", {"href":"www.anchor.com"})
        self.assertEqual(f"{text_node_to_html_node(textnode)}",f"{leafnode}")

    def test_textnode_to_htmlnode_image(self):
        textnode = TextNode("Alt Text","image","www.image.com")
        leafnode = LeafNode("img", "", {"src":"www.image.com", "alt": "Alt Text"})
        self.assertEqual(f"{text_node_to_html_node(textnode)}",f"{leafnode}")
    
    def test_text_node_to_html_node_text(self):
        textnode = TextNode("This is a text node","text")
        leafnode = LeafNode(None,"This is a text node")

        self.assertEqual(f"{text_node_to_html_node(textnode)}",f"{leafnode}")

    def test_print_created_leaf_node_italic(self):
        textnode = TextNode("e","italic")
        leafnode = LeafNode(tag="i", value = "e")
        self.assertEqual(f"{text_node_to_html_node(textnode)}", f"{leafnode}")

    def test_print_created_leaf_node_code(self):
        textnode = TextNode("e","code")
        leafnode = LeafNode(tag="code", value = "e")
        self.assertEqual(f"{text_node_to_html_node(textnode)}", f"{leafnode}")

if __name__ == "__main__":
    unittest.main()

