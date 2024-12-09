class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return[article.title for article in self.articles()]

    def contributing_authors(self):
        authors = {article.author for article in self.articles()}
        contributing_authors = [author for author in authors if len([a for a in Article.all if a.author == author and a.magazine == self]) > 2]

        return contributing_authors if contributing_authors else None