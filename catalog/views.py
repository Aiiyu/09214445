from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def UI(request):
    return render(request, 'UI.html')

def submit_score(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        subject = request.POST.get('subject')
        score = request.POST.get('score')
        
        # 這裡可以加入資料處理邏輯
        # 例如: 儲存到資料庫
        
        return HttpResponse('成績已提交：學號 {}, 姓名 {}, 科目 {}, 分數 {}'.format(
            student_id, student_name, subject, score
        ))
    
    return redirect('catalog')