from django import template
from django.db.models import Count
from ..models import Post

register = template.Library()

# simple_tag: processa os dados e devolve uma string
# inclusion_tag: processa os dados e devolve um template renderizado
# Se quiser registrar uma tag com um nome diferente, utilizar o atributo name
# Exemplo: @register.simple_tag(name='my_tag')

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]