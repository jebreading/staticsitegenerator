from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        splitnodes = []
        splitlist = node.text.split(delimiter)
        if len(splitlist) % 2 == 0:
            raise Exception("No closing delimiter")
        for i in range(len(splitlist)):
            if splitlist[i] == "":
                continue
            if i % 2 == 0:
                splitnodes.append(TextNode(splitlist[i], TextType.NORMAL))
            else:
                splitnodes.append(TextNode(splitlist[i], text_type))
        new_nodes.extend(splitnodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches