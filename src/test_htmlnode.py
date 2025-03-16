import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_tag(self):
        testchild = HTMLNode("a", "testing test", None, {"href": "https://www.google.com", "target": "_blank"})
        node = HTMLNode(None, "testing test", testchild, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(None, "testing test", testchild, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.TAG, node2.TAG)
        self.assertEqual(node.VALUE, node2.VALUE)
        self.assertEqual(node.CHILDREN, node2.CHILDREN)
        self.assertEqual(node.PROPS, node.PROPS)
    
    def test_no_text(self):
        testchild = HTMLNode("a", "testing test", None, {"href": "https://www.google.com", "target": "_blank"})
        node = HTMLNode("a", None, testchild, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", None, testchild, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.TAG, node2.TAG)
        self.assertEqual(node.VALUE, node2.VALUE)
        self.assertEqual(node.CHILDREN, node2.CHILDREN)
        self.assertEqual(node.PROPS, node.PROPS)
    
    def test_no_children(self):
        node = HTMLNode("a", "testing test", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "testing test", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.TAG, node2.TAG)
        self.assertEqual(node.VALUE, node2.VALUE)
        self.assertEqual(node.CHILDREN, node2.CHILDREN)
        self.assertEqual(node.PROPS, node.PROPS)

    def test_no_props(self):
        testchild = HTMLNode("a", "testing test", None, {"href": "https://www.google.com", "target": "_blank"})
        node = HTMLNode("a", "testing test", testchild, None)
        node2 = HTMLNode("a", "testing test", testchild, None)
        self.assertEqual(node.TAG, node2.TAG)
        self.assertEqual(node.VALUE, node2.VALUE)
        self.assertEqual(node.CHILDREN, node2.CHILDREN)
        self.assertEqual(node.PROPS, node.PROPS)

    def test_props_to_html(self):
        testchild = HTMLNode("a", "testing test", None, {"href": "https://www.google.com", "target": "_blank"})
        node = HTMLNode(None, "testing test", testchild, {"href": "https://www.google.com", "target": "_blank"})
        test = node.props_to_html()
        self.assertEqual(test, ' "href"="https://www.google.com" "target"="_blank"')

    def test_repr(self):
        node = HTMLNode("a", "testing test", None, {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, testing test, children: None, {'href': 'https://www.google.com'})")

