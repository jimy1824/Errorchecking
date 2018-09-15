from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import ERRORTYPE
from django.contrib import messages
import math

class TrainingView(View):
    template_name = 'training.html'

    def get(self, request):
        return render(request, self.template_name)



    def post(self, request):
        title = request.POST.get('error_title')
        p_type = request.FILES['p_type_file']
        thd_type = request.FILES['thd_type_file']
        p_file_data = p_type.file.read().decode("utf-8")
        thd_file_data = thd_type.file.read().decode("utf-8")

        p_lines = p_file_data.split("\n")
        thd_lines = thd_file_data.split("\n")
        p_user_list = []
        thd_user_list = []
        p_lines_legth=0
        for p_line in p_lines:
          if p_line :
            p_lines_legth=p_lines_legth+1
            a= str(p_line)
            a=float(a)
            p_user_list.append(a)
        thd_lines_length=0
        for thd_line in thd_lines:
            if thd_line:
                thd_lines_length=thd_lines_length+1
                a = str(thd_line)
                a = float(a)
                thd_user_list.append(int(a))

        min_length=min(p_lines_legth,thd_lines_length,)
        final_array = []
        for index in range(min_length):
            multiply = p_user_list[index]*thd_user_list[index]
            final_array.append(multiply)
        max_value=max(final_array)
        sum_values=sum(final_array)
        avg_values=sum_values/float(len(final_array))
        error_type=ERRORTYPE(error_title=title,max_value=max_value,avg_value=avg_values)
        error_type.save()
        messages.success(request, 'Data Saved Successfully')
        return render(request, self.template_name)


class TestingView(View):
    template_name = 'testing.html'

    def get(self, request):
        return render(request, self.template_name)



    def post(self, request):
        p_type = request.FILES['p_type_file']
        thd_type = request.FILES['thd_type_file']
        p_file_data = p_type.file.read().decode("utf-8")
        thd_file_data = thd_type.file.read().decode("utf-8")

        p_lines = p_file_data.split("\n")
        thd_lines = thd_file_data.split("\n")
        p_user_list = []
        thd_user_list = []
        p_lines_legth=0
        for p_line in p_lines:
          if p_line :
            p_lines_legth=p_lines_legth+1
            a= str(p_line)
            a=float(a)
            p_user_list.append(a)
        thd_lines_length=0
        for thd_line in thd_lines:
            if thd_line:
                thd_lines_length=thd_lines_length+1
                a = str(thd_line)
                a = float(a)
                thd_user_list.append(int(a))
        min_length=min(p_lines_legth,thd_lines_length,)
        final_array = []
        for index in range(min_length):
            multiply = p_user_list[index]*thd_user_list[index]
            final_array.append(multiply)
        max_value=max(final_array)
        sum_values=sum(final_array)
        avg_values=sum_values/float(len(final_array))
        results=[]
        records=ERRORTYPE.objects.all()
        for record in records:
          if  math.isclose(max_value, record.max_value, rel_tol=1e-09, abs_tol=0.0) or math.isclose(avg_values, record.avg_value, rel_tol=1e-09, abs_tol=0.0) :
                results.append(record)

        return render(request, self.template_name ,{'results': results})