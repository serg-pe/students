import os

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.contrib.auth import get_user_model
from pandas import read_csv, DataFrame

from .admin_forms import AdminBulkStudentsForm
from .models import Student
from .models import StudentGroup


User = get_user_model()


@user_passes_test(lambda user: user.is_superuser)
def admin_bulk_create_students(request):
    # df = DataFrame([
    #     [1, 1, 1, 123, '1@1.1'],
    #     [2, 2, 2, 234, '2@2.2']
    # ], columns=['surname', 'name', 'patronymic', 'groups', 'email']).to_csv(os.path.join(settings.MEDIA_ROOT, 'students_norm.csv')
    # )

    if request.method == 'POST':
        form = AdminBulkStudentsForm(request.POST, request.FILES)
        if form.is_valid():
            csv_frame = read_csv(form.cleaned_data['students_csv'])
            for _, row in csv_frame.iterrows():

                user = User(
                    username=row['email'], 
                    password=User.objects.make_random_password()
                )

                # user.save()

                group = StudentGroup.objects.get(number=row['groups'])
                if not group:
                    group = StudentGroup(number=row['groups'])
                    # group.save()

                # avatar_file = None
                # print(form.cleaned_data['students_avatars'])

                student = Student(
                    # avatar=avatar_file,
                    surname=row['surname'], 
                    name=row['name'], 
                    patronymic=row['patronymic'],
                    user=user,
                )
                student.groups.set([group,])
                student.save()

            return redirect(to='/admin/main/student')

        return render(request, 'main/admin/admin_students_view.html', {
            'form': form,
        })

    form = AdminBulkStudentsForm()
    return render(request, 'main/admin/admin_students_view.html', {
        'form': form,
    })

