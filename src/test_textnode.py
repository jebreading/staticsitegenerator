import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        self.assertEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        node2 = TextNode("This is a text node2", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXTTYPE, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test2.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXTTYPE)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXTTYPE, "https://www.test.com")
        self.assertEqual("TextNode(This is a text node, Bold Text, https://www.test.com)", repr(node))

if __name__ == "__main__":
    unittest.main()