from django.http import JsonResponse

# Create your views here.
def JasonResponse(param):
    pass


def show_books(request):
   return JasonResponse({"result:your API is working!"})