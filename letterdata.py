class Document:
    """
    Object that contains data about a document, such as
    title and date.
    """
    def __init__(self, title, date, address1, address2, paragraph, name):
        self.title = title
        self.date = date
        self.address1 = address1
        self.address2 = address2
        self.paragraph = paragraph
        self.name = name