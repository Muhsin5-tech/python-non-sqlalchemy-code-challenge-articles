class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable and cannot be changed.")
    
class Author:
    all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be non-empty string.")
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable and cannot be changed.")

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
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be non-empty string.")
        
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")
        
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