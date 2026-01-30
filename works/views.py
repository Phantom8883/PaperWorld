from django.shortcuts import render, get_object_or_404, redirect
from .models import Work
from .forms import WorkForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

def work_list(request):
    works = Work.published.all()
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


def work_detail(request, year, month, day, slug):
    work = get_object_or_404(
        Work,
        status=Work.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    return render(
        request,
        'works/work/detail.html',
        {
            'work': work,
        }
    )

@login_required
def work_create(request):
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)

            base_slug = slugify(work.title)
            slug = base_slug
            counter = 1

            while Work.objects.filter(
                publish__date=work.publish.date(),
                slug=slug
            ).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            work.slug = slug
            work.save()

            return redirect(work.get_absolute_url())
        
    else:
        form = WorkForm()

    return render(
        request,
        'works/work/create.html',
        {'form': form}
    )