class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):  # changes the old content to the new one
        self.content = new_content

    def change_author(self, new_author):  # changes the old author to with the new one
        self.author = new_author

    def rename(self, new_title):  # changes the old title with the new one
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)

