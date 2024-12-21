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


if __name__ == "__main__":
    unittest.main()