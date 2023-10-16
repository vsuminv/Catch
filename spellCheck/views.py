import os
import pathlib
import urllib.request
from datetime import datetime

import kss
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from hanspell import spell_checker
from soynlp.normalizer import *
from pathlib import Path
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse


# Create your views here.
def spellCheck(request):
    return render(request, 'spellCheck/cover_letter.html')


def textSave(request):
    print('textSave')
    getContent = request.GET.get('content')
    print(getContent)


    # 기본적인 전처리

    spelled_sent = spell_checker.check(getContent)
    checked_sent = spelled_sent.checked
    print('checked_sent', checked_sent)

    print(kss.split_sentences(checked_sent))
    ResultContent = ''
    for sent in kss.split_sentences(checked_sent):
        ResultContent += sent
        ResultContent += '\n'

    print('ResultContent', ResultContent)

    # media/txt/에 자기소개 저장
    nowDate = datetime.now()
    user = request.session['user']
    date = nowDate.strftime("%Y-%m-%d_%H_%M")
    filename = "media/txt/" + user + "_" + date + ".txt"
    f = open(filename, 'w',
             encoding='utf-8')
    f.write(ResultContent)

    context = {'getContent': ResultContent, 'filename':filename}
    return JsonResponse(context)


def saveSpellCheckResult(request):

    resultContent = request.GET.get('resultContent')
    filename = request.GET.get('filename')
    print('filename', filename)
    print('resultContent',resultContent)




    context = {'message':'성공'}
    return JsonResponse(context)
