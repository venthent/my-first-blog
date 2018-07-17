from django.shortcuts import render

def post_list(requst):
    return render(requst,'blog/post_list.html',{})

