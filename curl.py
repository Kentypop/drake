
#Convert queryset type to list
from django.contrib.auth.models import User
users= User.objects.all()

user_list= list(users)
type(user_list)


#Get one value from a lst item
user_one= users[:1]
user_one.values()
