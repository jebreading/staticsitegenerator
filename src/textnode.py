from enum import Enum

class TextType(Enum):
    NORMAL_TEXTTYPE = "Normal Text"
    BOLD_TEXTTYPE = "Bold Text"
    ITALIC_TEXTTYPE = "Italic Text"
    CODE_TEXTTYPE = "Code Text"
    LINK_TEXTTYPE = "Link"
    IMAGE_TEXTTYPE = "Image"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.TEXT = TEXT
        self.TEXT_TYPE = TEXT_TYPE
        self.URL = URL

    def __eq__(self, other):
        return (
            self.TEXT == other.TEXT
            and self.TEXT_TYPE == other.TEXT_TYPE
            and self.URL == other.URL
        )
    
    def __repr__(self):
        return f"TextNode({self.TEXT}, {self.TEXT_TYPE.value}, {self.URL})"
    
    