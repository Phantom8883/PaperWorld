from django.shortcuts import render, get_object_or_404
from .models import Work
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def work_list(request):

    works = Work.published.all()


    # Пагинация
    # Для фанфиков думаю можно 8 работ на страницу сделать, или больше, но думаю 8 хватит пока
    paginator = Paginator(works, 8)
    page_number = request.GET.get('page', 1)

    try:
        works = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number находится вне диапазона, то
        # выдать последнюю страницу результатов
        works = paginator.page(1)
    except EmptyPage:
        # Если page_number находятся вне диапазона, то
        # выдать последнюю страницу
        works = paginator.page(paginator.num_pages)

    return render(
        request,
        'works/work/list.html',
        {
            'works': works
        }
    )


def work_detail(request, work_id):
    work = get_object_or_404(
        Work,
        id=work_id,
        status=Work.Status.PUBLISHED
    )

    return render(
        request,
        'works/work/detail.html',
        {
            'work': work
        }
    )