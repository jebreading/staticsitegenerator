import unittest
from inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class Test_split_nodes_delimter(unittest.TestCase):
    def test_normal(self):
        old_nodes = [TextNode("Testing basic text with a **bolded phrase** in the middle", TextType.NORMAL)]
        output = split_nodes_delimiter(old_nodes, "**", TextType.NORMAL)
        print(output)
    
    def test_non_text(self):
        old_nodes = [TextNode("Testing non text with a **bolded phrase** in the middle", TextType.BOLD)]
        output = split_nodes_delimiter(old_nodes, "**", TextType.NORMAL)
        print(output)

    def test_multiple_nodes(self):
        old_nodes = [TextNode("Testing multiple text with a **bolded phrase** in the middle", TextType.NORMAL), TextNode("Testing multiple text with a **bolded phrase** in the middle", TextType.NORMAL)]
        output = split_nodes_delimiter(old_nodes, "**", TextType.NORMAL)
        print(output)
    
    def test_other_delimiter(self):
        old_nodes = [TextNode("Testing other delimter text with a 'code phrase' in the middle", TextType.NORMAL)]
        output = split_nodes_delimiter(old_nodes, "'", TextType.CODE)
        print(output)

class Test_extract_markdown_images(unittest.TestCase):
    def test_basic(self):
        testtext = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(testtext)
        print(output)

    def test_spaces_and_numbers(self):
        testtext = "Here is ![image one](url1) and ![image two](url2)"
        output = extract_markdown_images(testtext)
        print(output)

    def test_special_characters(self):
        testtext = "Here is ![image one%](url1%) and ![image two%](url2%)"
        output = extract_markdown_images(testtext)
        print(output)

class test_extract_markdown_links(unittest.TestCase):
    def test_basic(self):
        testtext = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(testtext)
        print(output)
    
    def test_boots_example(self):
        testtext = "Here is a [link](url1) and here is an ![image](url2)"
        output = extract_markdown_links(testtext)
        print(output)

    def test_boots_new_case(self):
        testtext = "[first link](url1) some text [second link](url2)"
        output = extract_markdown_links(testtext)
        print(output)
    