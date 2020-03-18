from django.shortcuts import render

# Create your views here.
from datetime import datetime, timedelta


def post_view(request):
#     date_from = datetime.datetime.now() - datetime.timedelta(days=1)
# created_documents = CreatedDocumentDetails.objects.filter(
#      user=user, created_document_timestamp__gte=date_from).count()

    context = {
        
    }
    return render(request, 'posts.html', context)


'''
def delete_old_foos():
    # Query all the foos in our database
    foos = Foo.objects.all()

    # Iterate through them
    for foo in foos:

        # If the expiration date is bigger than now delete it
        if foo.expiration_date < timezone.now():
            foo.delete()
            # log deletion
    return "completed deleting foos at {}".format(timezone.now())
    
'''