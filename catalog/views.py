from django.shortcuts import render

# Create your views here.
def score_list(request):
    # This view would typically fetch data from the database
    scores = [
        {'name': 'Alice', 'score': 95},
        {'name': 'Bob', 'score': 85},
        {'name': 'Charlie', 'score': 75},
    ]
    return render(request, 'catalog/score_list.html', {'scores': scores})
>>>>>>> 6b77fcc (新增 catalog 應用並更新路由 (ScoreSystem/urls.py))
