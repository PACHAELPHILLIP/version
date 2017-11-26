from django import template
from blog.models import Article

register = template.Library()

@register.inclusion_tag('blog/latest_article.html')
def latest_articles():
    articles = Article.objects.filter(published=True)
    return {'articles':articles}
