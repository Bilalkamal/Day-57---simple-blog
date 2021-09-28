
class Post:
    def __init__(self, id, title, contents, link):
        self.id = id
        self.title = title
        self.contents = contents
        self.link = link
    
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title
    
    def get_contents(self):
        return self.contents
    
    def get_link(self):
        return self.link