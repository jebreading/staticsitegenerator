class HTMLNode:
    def __init__(self, TAG=None, VALUE=None, CHILDREN=None, PROPS=None):
        self.TAG = TAG
        self.VALUE = VALUE
        self.CHILDREN = CHILDREN
        self.PROPS = PROPS
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.PROPS == None:
            return ""
        propshtmltext = ""

        for p in self.PROPS:
            propshtmltext += f' "{p}"="{self.PROPS[p]}"'

        return propshtmltext
    
    def __repr__(self):
        return f"HTMLNode({self.TAG}, {self.VALUE}, children: {self.CHILDREN}, {self.PROPS})"