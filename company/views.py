from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from company.models import Person, Department


def index(request):
    return HttpResponse('Hello world! !')

# def employees(request):
#     person_list = Person.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(person_list, 1)
#     try:
#         person_list = paginator.page(page)
#     except PageNotAnInteger:
#         person_list = paginator.page(1)
#     except EmptyPage:
#         person_list = paginator.page(paginator.num_pages)
#
#     Person.objects.filter()
#     return render(request, 'person_list.html', context={
#         'person_list' : person_list,
#     })

class EmployeeList(ListView):
    model = Person
    template_name = 'person_list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_list'] = Department.objects.all()
        request_get_items = dict(self.request.GET.items())
        if 'page' in request_get_items:
            del request_get_items['page']
        qs = ''
        for key, value in request_get_items.items():
            qs += key + '=' + value + '&'
        context['get_params'] = qs
        return context

    def get_queryset(self):
        is_working = self.request.GET.get('is_working')
        if is_working == 'True':
            is_working = True
        elif is_working == 'False':
            is_working = False
        else:
            is_working = None
        res_queryset = Person.objects.all()
        if is_working is not None:
            res_queryset = res_queryset.filter(end_work_date__isnull=is_working)
        department = self.request.GET.get('department')
        department = None if department == 'None' else department
        if department is not None:
            res_queryset = res_queryset.filter(department__department_tittle=department)
        return res_queryset

class EmployeeDetail(DetailView):
    model = Person
    template_name = 'person_detail.html'





def test(request):
    print(f'request.GET = {request.GET}')
    print(f'request.POST = {request.POST}')

    return HttpResponse('aaaa')