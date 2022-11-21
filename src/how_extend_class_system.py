ENGLISH_LANGUAGE_CODE = "EN-en"
Russian_LANGUAGE_CODE = "RU-ru"

class Article:

    def __init__(self, language):
        self.language = language

class EnglishArticle(Article):

    def __init__(self):
        super().__init__(language=ENGLISH_LANGUAGE_CODE)


class RussianArticle(Article):

    def __init__(self):
        super().__init__(language=Russian_LANGUAGE_CODE)


class ArticleTranslator:

    def translate(self, article):
        for line in article:
            localize(line, article.language)