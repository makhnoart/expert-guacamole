from django.core.mail import EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Author


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/detail.html'


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('library')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('appname/library')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'library/book_create.html'
    success_url = reverse_lazy("pk:library")


class AuthorListView(ListView):
    context_object_name = 'authors'
    template_name = 'library/library.html'
    # paginate_by = 10

    def get_queryset(self):
        author_list = Author.objects.order_by('first_name')
        paginator = Paginator(author_list, 4) # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            authors = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            authors = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            authors = paginator.page(paginator.num_pages)

        return authors


email = EmailMessage('title', 'body', to=['makhnoarthur@gmail.com'])
email.send()
