import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        testnode = HTMLNode("a", "testing text", None,{"href": "https://www.google.com", "target": "_blank"})
        testnode2 = HTMLNode("a", "testing text", None,{"href": "https://www.google.com", "target": "_blank"})
        list = []
        list.append(testnode)
        list.append(testnode2)
        node = HTMLNode("a", "testing text", list, {"href": "https://www.google.com", "target": "_blank"})
        print(node)
        print(node.props_to_html())

    def test_props2(self):
         node = HTMLNode("a", "testing text", None, {"href": "https://www.google.com", "target": "_blank", "test": "testing", "bob": "testing"})
         print(node)
         print(node.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_no_tag(self):
        node = LeafNode(None, "testing", {"href":"www.google.co.uk"})
        print(f"no tag {node.to_html()}")

    def test_no_props(self):
        node = LeafNode("p", "testing", None)
        print(f"no props {node.to_html()}")

    def test_value_only(self):
        node = LeafNode(None, "testing",None)
        print(f"value only {node.to_html()}")

class TestParentNode(unittest.TestCase):
    def test_normal(self):
        node = ParentNode("a", [LeafNode("a", "testing text",{"href": "https://www.google.com", "target": "_blank"}), LeafNode("a", "testing", {"href":"www.google.co.uk"})], {"href":"www.boot.dev"})
        print(node.to_html())

    def test_no_props(self):
        node = ParentNode("a", [LeafNode("a", "testing text",{"href": "https://www.google.com", "target": "_blank"}), LeafNode("a", "testing", {"href":"www.google.co.uk"})], None)
        print(node.to_html())

    def test_parent_children(self):
        node = ParentNode("a", [ ParentNode("a", [LeafNode("a", "testing text",{"href": "https://www.google.com", "target": "_blank"}), LeafNode("a", "testing", {"href":"www.google.co.uk"})], {"href":"www.boot.dev"})], None)
        print(node.to_html())
if __name__ == "__main__":
    unittest.main()