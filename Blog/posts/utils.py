from django.shortcuts import redirect
from django.core.mail import send_mass_mail


def send_mail_to_reader(post):
    author = post.author
    data = """
Hello there!

Let's go and check out a new post '%s' from one of you're favorite author %s.

    """ % (post.title, post.author)
    mails = []
    for reader in author.readers.all():
        mails.append(reader.user.email)
    print(mails)
    message1 = ('New post at MyCoolBlog', data,'', mails)
    send_mass_mail((message1, ), fail_silently=False)
    return redirect('posts')