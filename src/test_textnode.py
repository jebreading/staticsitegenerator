import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq_text(self):
        node = TextNode("This is a test node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node2", TextType.BOLD, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_noteq_textype(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_noteq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.test2.com")
        self.assertNotEqual(node, node2)

class Testtextnodetohtml(unittest.TestCase):
    def test_text(self):
        textnode = TextNode("This is a text node", TextType.NORMAL, None)
        node = textnode.text_node_to_html_node()
        print(node.to_html())

    def test_bold(self):
        textnode = TextNode("This is a bold node", TextType.BOLD, None)
        node = textnode.text_node_to_html_node()
        print(node.to_html())

    def test_italic(self):
        textnode = TextNode("This is a italic node", TextType.ITALIC, None)
        node = textnode.text_node_to_html_node()
        print(node.to_html())

    def test_CODE(self):
        textnode = TextNode("This is a code node", TextType.CODE, None)
        node = textnode.text_node_to_html_node()
        print(node.to_html())

    def test_LINK(self):
        textnode = TextNode("This is a link node", TextType.LINKS, "www.google.co.uk")
        node = textnode.text_node_to_html_node()
        print(node.to_html())

    def test_IMAGE(self):
        textnode = TextNode("This is a image node", TextType.IMAGES, "www.google.co.uk/image.png")
        node = textnode.text_node_to_html_node()
        print(node.to_html())
if __name__ == "__main__":
    unittest.main()