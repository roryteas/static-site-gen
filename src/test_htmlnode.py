import unittest
from textnode_split_logic import *
from htmlnode import * 

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        tag = 'Body'
        value = 'Stuff'
        props = {"href":"www.lim.com"}
        node = HTMLNode(tag=tag,value=value,props=props)
        expected_result = f"HTMLNode(tag={tag}, value={value}, children=None, props={props}"
        self.assertEqual(f"{node}", expected_result)
    def test_empty_props_to_html(self):
        props = {}
        node = HTMLNode(props=props)
        expected_result = " "
        self.assertEqual(node.props_to_html(),expected_result)
    def test_props_to_html(self):
        props = {"a":"b", "FfffffFFF":"fdsfdsfds"}
        node = HTMLNode(props=props)
        expected_result = ' a="b" FfffffFFF="fdsfdsfds"' 
        self.assertEqual(node.props_to_html(), expected_result)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):

        leafnode = LeafNode(value ="test the leaf",tag="a")
        expected_result = "<a>test the leaf</a>"
        self.assertEqual(leafnode.to_html(),expected_result)
    def test_constructor(self):

        leafnode = LeafNode(tag="b", value = "e", props={"style":"gothic"})
        expected_result = "LeafNode(tag=b, value=e, props={'style': 'gothic'}"
        self.assertEqual(f"{leafnode}", expected_result)
    def test_no_value(self):
        
        self.assertRaises(TypeError,LeafNode,tag="a")



class TestParentNode(unittest.TestCase):
    def test_parent_bootdev_example(self):
        node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
           ],
        )

        result = node.to_html()
        self.assertEqual(result,"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_single_nested_parent(self):
        node = ParentNode(
                "body",
                [
                ParentNode(
                    "p",
                    [
                    LeafNode("p", "paragraph"),
                    LeafNode(None, "just some text"),
                    LeafNode(None, "hello")
                    ],
                )
                ,
                ParentNode(
                            "p",
                            [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                           ],
                        )
                ],
        )
        result = node.to_html()
        expected_result = "<body><p><p>paragraph</p>just some texthello</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>"
        self.assertEqual(result,expected_result)

    def test_no_children(self):
        
        self.assertRaises(TypeError,ParentNode,("p",None))

        
    def test_single_nested_parent_with_Leafs(self):
        node = ParentNode(
                "body",
                [
                ParentNode(
                    "p",
                    [
                    LeafNode("p", "paragraph"),
                    LeafNode(None, "just some text"),
                    LeafNode(None, "hello")
                    ],
                )
                ,
                LeafNode(None, "just some text"),
                LeafNode("b", "just some text")
                ],
        )
        result = node.to_html()
        expected_result = "<body><p><p>paragraph</p>just some texthello</p>just some text<b>just some text</b></body>"
        self.assertEqual(result,expected_result)





