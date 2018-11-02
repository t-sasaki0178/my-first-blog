from django.shortcuts import render

def post_list(request):
    return render(request,'blog/post_list.html',{}) #requestで受け取った内容をテンプレートに出力