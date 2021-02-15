from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from registration.forms import User

from .forms import UserForm, UserInfoForm, CommodityForm
from .models import UserInfo, Record, Commodity, Category


# Create your views here.


def index(request):
    return render(request, 'saltfish/index.html', {})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            # 把userform中的数据存入数据库
            user = user_form.save(commit=False)

            # 使用set_password方法计算密码的哈希值
            # 更新user对象
            user.set_password(user.password)
            user.save()

            info = info_form.save(commit=False)
            info.user = user

            if 'profile' in request.FILES:
                info.profile = request.FILES['profile']

            info.save()
            registered = True
        else:
            print(user_form.errors, info_form.errors)
    else:
        user_form = UserForm()
        info_form = UserInfoForm()

    return render(request,
                  'saltfish/register.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'info_form': info_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is disabled')
        else:
            print('Invalid login details:{0}, {1}'.format(username, password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'saltfish/login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


@login_required
def register_info(request):
    form = UserInfoForm()

    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'saltfish/register-info.html', context_dict)


@login_required
def edit_info(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DeseNotExist:
        return redirect('index')

    user_info = UserInfo.objects.get_or_create(user=user)[0]
    form = UserInfoForm(
        {'phone': user_info.phone, 'grade': user_info.grade,
         'faculty': user_info.faculty, 'profile': user_info.profile
         }
    )

    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save(commit=True)
            return redirect('info', user.username)
        else:
            print(form.errors)

    return render(request, 'saltfish/user-info.html',
                  {'user_info': user_info, 'selecteduser': user, 'form': form})


@login_required
def release_commodity(request):
    success = False
    com_form = CommodityForm()

    if request.method == 'POST':
        # 创建商品对象
        com_form = CommodityForm(data=request.POST, files=request.FILES)
        if com_form.is_valid():
            com = com_form.save(commit=False)
            com.owner = request.user
            com.save()

            # 创建一条发布记录
            newrecord = Record()
            newrecord.user = com.owner
            newrecord.commodity = com
            newrecord.save()
            success = True
        else:
            print(com_form.errors)

    return render(request,
                  'saltfish/release-commodity.html',
                  {'com_form': com_form,
                   'success': success})


def register_complete(request):
    return render(request, 'registration/registration_complete.html', {})


@login_required
def show_record(request):
    return render(request, 'saltfish/show-record.html', {})


@login_required
def get_record(request):
    type = int(request.GET.get('type'))
    records = Record.objects.filter(type=type, user=request.user)
    nothing = len(records) == 0
    context_dict = {'records': records, 'nothing': nothing, 'type': type}
    return render(request, 'saltfish/record.html', context_dict)


def detail(request, com_id):
    commodity = find_commodity(com_id)

    found = commodity is not None
    if not found:
        return render(request, 'saltfish/com-detail.html', {'found': found})

    com_form = CommodityForm(
        {'tag': commodity.tag, 'price': commodity.price,
         'description': commodity.description, 'picture': commodity.picture,
         'quantity': commodity.quantity, 'category': commodity.category,
         'departure': commodity.departure
         })

    if request.method == 'POST':
        commodity.create_time = timezone.now()
        com_form = CommodityForm(request.POST, request.FILES, instance=commodity)
        if 'update' in request.POST:
            if com_form.is_valid():
                com_form.save(commit=True)
                return HttpResponse('ok')
            else:
                print(com_form.errors)
        elif 'remove' in request.POST:
            commodity.delete()
            return redirect('index')

    return render(request,
                  'saltfish/com-detail.html',
                  {'commodity': commodity,
                   'com_form': com_form,
                   'owner': request.user,
                   'found': found})


@login_required
def add_commodity(request, com_id):
    commodity = find_commodity(com_id)

    type = 0
    if 'buy' in request.POST:
        type = 2
        ownerRecord = Record(user=commodity.owner, commodity=commodity, type=3)
        ownerRecord.save()
    elif 'cart' in request.POST:
        type = 4
    elif 'collect' in request.POST:
        type = 5

    # 查看是否已经收藏或加入购物车 若是则移出收藏或购物车
    userRecord = Record.objects.filter(user=request.user, commodity=commodity, type=type)
    if len(userRecord) == 0:
        userRecord = Record(user=request.user, commodity=commodity, type=type)
        userRecord.save()
    else:
        userRecord[0].delete()

    return redirect('record')


def search(request):
    return


def show_category(request):
    categories = Category.objects.all()

    return render(request, 'saltfish/show-category.html', {'categories': categories})


def get_category(request):
    type = request.GET.get('type')
    category = Category.objects.get(id=type)
    commodities = Commodity.objects.filter(category=category)
    found = len(commodities) != 0
    return render(request, 'saltfish/category.html', {'commodities': commodities, 'found': found})


def find_commodity(com_id):
    try:
        commodity = Commodity.objects.get(id=com_id)
        return commodity
    except Commodity.DoesNotExist:
        return None


@login_required
def fill_order(request, com_id):

    return


@login_required
def show_order(request):
    return render(request, 'saltfish/show-order.html', {})


def get_result_list(starts_with=''):
    com_list = []
    userinfo_list = []
    if starts_with:
        com_list = Commodity.objects.filter(tag__istartswith=starts_with)
        userinfo_list = UserInfo.objects.filter(user__username__istartswith=starts_with)

    return [com_list, userinfo_list]


def get_suggest(request):
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    result_list = get_result_list(starts_with)
    return render(request,
                  'saltfish/suggestion.html',
                  {
                   'com_list': result_list[0],
                  'userinfo_list': result_list[1]})


