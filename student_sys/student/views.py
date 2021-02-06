from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
# Create your views here.

from .models import Student
from .forms import StudentForm


@csrf_exempt
@method_decorator(login_required, name='as_view')
class IndexView(View):
    template_name = 'student/index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)


@csrf_exempt
def register(request):
    name = 'unknown'
    if request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        profession = request.POST['profession']
        email = request.POST['email']
        qq = request.POST['qq']
        phone = request.POST['phone']
        Student.objects.create(name=name, sex=sex, profession=profession, email=email,
                               qq=qq, phone=phone)
        return render(request, 'student/index.html', context={'name': name})
    else:
        return render(request, 'student/register.html', {})
