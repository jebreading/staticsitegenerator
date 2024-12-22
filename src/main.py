from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    text_type = TextType.BOLD
    test = TextNode("testing text node", text_type, "https://www.boot.dev")
    testnode = HTMLNode("a", "testing text", None,{"href": "https://www.google.com", "target": "_blank"})
    testnode2 = HTMLNode("a", "testing text", None,{"href": "https://www.google.com", "target": "_blank"})
    list = []
    list.append(testnode)
    list.append(testnode2)
    node = HTMLNode("a", "testing text", list, {"href": "https://www.google.com", "target": "_blank"})
    print(node)
    print(test)

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case (text_node.text_type.TEXT):
            return LeafNode(None, text_node.value, None)
        case (text_node.text_type.BOLD):
            return LeafNode("b", text_node.value, None)
        case (text_node.text_type.ITALIC):
            return LeafNode("i", text_node.value, None)
        case (text_node.text_type.CODE):
            return LeafNode("code", text_node.value, None)
        case (text_node.text_type.LINK):
            return LeafNode("a", text_node.value, {"href": text_node.url})
        case (text_node.text_type.IMAGE):
            return LeafNode("img", text_node.value, {"src": text_node.url, "alt":text_node.text})

if __name__ == "__main__":
    main()