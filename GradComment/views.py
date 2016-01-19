from django.shortcuts import render, HttpResponseRedirect
from GradComment.models import *
from GradComment.forms import *


# Create your views here.

def indexView(request):
    getStudent_list = Students.objects.order_by('name')
    context = {'Student_list': getStudent_list}
    return render(request, 'student_list.html', context)


def StudentDetails(request, student_id):
    pushedComments = Comments.objects.filter(student_comment__id = student_id)
    getStudent = Students.objects.get(pk=student_id)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        form.save()

        fetch_saved_data = Comments.objects.order_by('-id')[:1]
        for i in fetch_saved_data:
            getStudent.comments_set.create(comment_text = i.comment_text)

        return HttpResponseRedirect('student_details.html')

    else:
        form = CommentsForm()
    context = {'Student': getStudent, 'form': form, 'ShowComments': pushedComments}
    return render(request, 'student_details.html', context)





