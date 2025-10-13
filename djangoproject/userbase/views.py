from django.shortcuts import render
from home.models import Doggy
from django.db.models import Count


def post_list(request):
    name_lookup = request.GET.get("name", None)
    dog = Doggy.objects.all()

    if name_lookup:
        dog = dog.filter(user__name=name_lookup)

    user_with_dog = Doggy.objects.values("user__name").annotate(num_posts=Count("id"))
    total_posts = Doggy.objects.count()

    # Extract the username from user_with_dog
    owner = [user_with_dog["user__name"] for user_with_dog in user_with_dog]

    return render(
        request,
        #
        "post.html",
        {
            "dog name": dog,
            "owner": owner,
            "user_with_posts": user_with_posts,
            "total_posts": total_posts,
        },
    )
