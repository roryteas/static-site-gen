import unittest
from markdown_to_blocks import *



class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks_doc(self):
        doc= f"# This is a heading \n\n#This is a heading \n\nthis is some text in a paragraph \n\n\nthis made a blankline\n\n * list \n* of \n* crap"
        block_types = []
        for block in markdown_to_blocks(doc):
            block_types.append(block_to_block_type(block))
        self.assertEqual(block_types,['heading','heading','paragraph','paragraph','unordered-list'])
        self.assertEqual(len(markdown_to_blocks(doc)),5)


    def test_markdown_to_html_node(self):
        doc = '# I like markdown\n\nIt is very good\n\nI like **bold** markdown'

        print(markdown_to_html_node(doc))
if __name__ == "__main__":
    unittest.main()
