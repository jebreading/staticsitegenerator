class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        text = ""
        for p in self.props:
            text += f' {p}="{self.props[p]}"'
        return text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}, {self.props_to_html()})"
    
class LeafNode(HTMLNode):
    def __init__(self,tag, value,  props=None):
        super().__init__(tag, value,None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("No value specified")
        if self.tag is None:
            return self.value
        if self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag specified")
        
        if self.children is None:
            raise ValueError("No children specified")
        if self.props:
            htmltext = f"<{self.tag}{self.props_to_html()}"
        else:
            htmltext = f"<{self.tag}>"
        if isinstance(self.children, list):
            for child in self.children:
                htmltext += child.to_html()
        else:
            htmltext += self.children.to_html()
        htmltext += f"</{self.tag}>"

        return htmltext
        
