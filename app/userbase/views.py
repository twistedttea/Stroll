from django.shortcuts import render
from userbase.models import Doggy
from django.db.models import Count


def dog_list(request):
    # Pull from database
    name_lookup = request.GET.get("name", None)
    # grab all dogs
    dog = Doggy.objects.all()

    if name_lookup:
        dog = dog.filter(user__name=name_lookup)

    # FIXME I left out changing after user__name > num_posts....
    user_with_dog = Doggy.objects.values("dog_name").annotate(num_posts=Count("id"))
    total_posts = Doggy.objects.count()

    # Extract the username from user_with_dog
    owner = [user_with_dog["user__name"] for user_with_dog in user_with_dog]

    return render(
        request,
        # Send post request to post.html, which uses it.
        # this is what will send all the data back to the site
        "post.html",
        {
            "dog name": dog,
            "owner": owner,
            "user_with_dog": user_with_dog,
            "total_posts": total_posts,
        },
    )
