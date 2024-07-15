from blog.models import Post, Category


def resent_posts(request):
    posts = Post.objects.all()
    return {'resent': posts[:3]}


def category(request):
    categories = Category.objects.all()
    return {'category': categories}