from textnode import TextNode
from textnode import TextType

def main():
    text_type = TextType.BOLD
    test = TextNode("testing text node", text_type, "https://www.boot.dev")
    print(test)

if __name__ == "__main__":
    main()