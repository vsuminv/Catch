from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from .forms import BoardWriteForm, CommentForm, CommentStudyForm
from .models import Board, Study, Reply, StudyReply
from user.models import User

from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def list(request):
    boards1 = Board.objects.filter(board_type=1).order_by('-board_id')
    boards2 = Board.objects.filter(board_type=2).order_by('-board_id')
    boards3 = Board.objects.filter(board_type=3).order_by('-board_id')
    studys = Study.objects.all().order_by('-study_id')
    boards4 = Board.objects.select_related('user_id')
    return render(request, 'community/community.html',
                  {'boards1': boards1, 'boards2': boards2, 'boards3': boards3, 'studys': studys, 'boards4': boards4})


def new_writing(request, communityid):
    user_id = request.session.get('user')
    context = {'login_session': user_id}
    request.session['communityid'] = communityid
    print(communityid)

    if user_id:
        if request.method == 'GET':
            write_form = BoardWriteForm()
            context['forms'] = write_form
            print(request.session['communityid'])
            return render(request, 'community/new_writing.html', context)

        elif request.method == 'POST':
            if communityid == 4:
                write_form = BoardWriteForm(request.POST)

                if write_form.is_valid():

                    Study(
                        title=write_form.title,
                        content=write_form.content,
                        user_id=User.objects.get(user_id=request.session['user']),
                        contact=request.POST['contact'],
                        process=request.POST['process'],
                        members=request.POST['members'],
                        tag=request.POST['tag'],
                        start_date=request.POST['start_date'],
                        study_period=request.POST['study_period'],
                        due_date=request.POST['due_date']
                    ).save()
                    return redirect('list')
                else:
                    context['forms'] = write_form
                    if write_form.errors:
                        for value in write_form.errors.values():
                            context['error'] = value
                    return render(request, 'community/new_writing.html', context)
                return redirect('list')
            else:
                write_form = BoardWriteForm(request.POST)

                if write_form.is_valid():

                    board = Board(
                        title=write_form.title,
                        content=write_form.content,
                        user_id=User.objects.get(user_id=request.session['user']),
                        board_type=request.session['communityid']
                    )
                    board.save()
                    return redirect('list')
                else:
                    context['forms'] = write_form
                    if write_form.errors:
                        for value in write_form.errors.values():
                            context['error'] = value
                    return render(request, 'community/new_writing.html', context)

        return render(request, 'community/new_writing.html')
    else:
        return HttpResponse("<script>alert('로그인 후 접근 가능합니다.'); location.href='/user/login'; </script>")


def community_post(request, communityid, board_id):
    user_id = request.session.get('user')
    context = {'login_session': user_id}
    request.session['communityid'] = communityid
    print(request.session['communityid'], board_id)
    if user_id:
        if communityid == 4:
            contentList = get_object_or_404(Study, pk=board_id)
            replyList = StudyReply.objects.filter(board_id=board_id).order_by('-reply_id')
            print(contentList.user_id.user_id, user_id)
            replyCount = StudyReply.objects.filter(board_id=board_id).count()
            return render(request, 'community/community_post.html',
                          {'contentList': contentList, 'replyList': replyList, 'replyCount':replyCount})
        else:
            contentList = get_object_or_404(Board, pk=board_id)
            replyList = Reply.objects.filter(board_id=board_id).order_by('-reply_id')
            print(contentList.user_id.user_id, user_id)
            replyCount = Reply.objects.filter(board_id=board_id).count()
            return render(request, 'community/community_post.html',
                          {'contentList': contentList, 'replyList': replyList, 'replyCount':replyCount})
    else:
        return HttpResponse("<script>alert('로그인 후 접근 가능합니다.'); location.href='/user/login'; </script>")


def community_delete(request, communityid, board_id):
    user_id = request.session.get('user')
    context = {'login_session': user_id}
    request.session['communityid'] = communityid
    print(request.session['communityid'], board_id)
    if user_id:
        if communityid == 4:
            study = Study.objects.get(pk=board_id)
            study.delete()
            return HttpResponse("<script>alert('삭제 되었습니다.'); location.href='/community/list';</script>")
        else:
            board = Board.objects.get(pk=board_id)
            board.delete()
            return HttpResponse("<script>alert('삭제 되었습니다.'); location.href='/community/list';</script>")
    else:
        return HttpResponse("<script>alert('로그인 후 접근 가능합니다.'); location.href='/user/login'; </script>")


def community_update(request, communityid, board_id):
    if communityid == 4:
        board_number = get_object_or_404(Study, study_id=board_id)
        session = request.session['user']

        context = {'board': board_number, 'session': session}

        if board_number.user_id.user_id != request.session['user']:
            return redirect(f'/community/community_post/{communityid}/{board_id}/')

        if request.method == 'GET':
            write_form = BoardWriteForm(instance=board_number)
            context['forms'] = write_form
            return render(request, 'community/community_update.html', context)

        elif request.method == 'POST':
            write_form = BoardWriteForm(request.POST)

            if write_form.is_valid():

                board_number.title = write_form.title
                board_number.content = write_form.content
                board_number.contact = request.POST['contact']
                board_number.process = request.POST['process']
                board_number.members = request.POST['members']
                board_number.start_date = request.POST['start_date']
                board_number.study_period = request.POST['study_period']
                board_number.due_date = request.POST['due_date']
                board_number.save()
                return redirect('list')
            else:
                context['forms'] = write_form
                if write_form.errors:
                    for value in write_form.errors.values():
                        context['error'] = value
                return render(request, 'community/community_update.html', context)
    else:
        board_number = get_object_or_404(Board, board_id=board_id)
        session = request.session['user']

        context = {'board': board_number, 'session': session}

        if board_number.user_id.user_id != request.session['user']:
            return redirect(f'/community/community_post/{communityid}/{board_id}/')

        if request.method == 'GET':
            write_form = BoardWriteForm(instance=board_number)
            context['forms'] = write_form
            return render(request, 'community/community_update.html', context)

        elif request.method == 'POST':
            write_form = BoardWriteForm(request.POST)

            if write_form.is_valid():

                board_number.title = write_form.title
                board_number.content = write_form.content
                board_number.save()
                return redirect('list')
            else:
                context['forms'] = write_form
                if write_form.errors:
                    for value in write_form.errors.values():
                        context['error'] = value
                return render(request, 'community/community_update.html', context)


def new_comment(request, communityid, board_id):
    if communityid == 4:
        filled_form = CommentStudyForm(request.POST)
        print("댓글 달기", filled_form.is_valid())
        if filled_form.is_valid():
            finished_form = filled_form.save(commit=False)
            # board_id = Post.objects.get(id=boardid)
            finished_form.board_id = Study.objects.get(study_id=board_id)
            finished_form.user_id = User.objects.get(user_id=request.session['user'])
            finished_form.save()
            print("댓글 달기 성공")
            return redirect(f'/community/community_post/{communityid}/{board_id}')
        else:
            print("댓글작성안됨")
            print(board_id)
        return redirect(f'/community/community_post/{communityid}/{board_id}')
    else:
        filled_form = CommentForm(request.POST)
        print("댓글 달기", filled_form.is_valid())
        if filled_form.is_valid():
            finished_form = filled_form.save(commit=False)
            # board_id = Post.objects.get(id=boardid)
            finished_form.board_id = Board.objects.get(board_id=board_id)
            finished_form.user_id = User.objects.get(user_id=request.session['user'])
            finished_form.save()
            print("댓글 달기 성공")
            return redirect(f'/community/community_post/{communityid}/{board_id}')
        else:
            print("댓글작성안됨")
            print(board_id)
        return redirect(f'/community/community_post/{communityid}/{board_id}')


def comment_update(request, communityid, board_id, reply_id):
    if communityid == 4:
        if request.method == "POST":
            reply = StudyReply.objects.get(pk=reply_id)
            reply.content = request.POST['content']
            reply.save()
            return redirect(f'/community/community_post/{communityid}/{board_id}')
        else:
            return redirect(f'/community/community_post/{communityid}/{board_id}')

    else:
        if request.method == "POST":
            print('POST')
            reply = Reply.objects.get(pk=reply_id)
            reply.content = request.POST['content']
            reply.save()
            return redirect(f'/community/community_post/{communityid}/{board_id}')
        else:
            return redirect(f'/community/community_post/{communityid}/{board_id}')


def comment_delete(request, communityid, board_id, reply_id):
    print(communityid, type(communityid))
    if communityid == '4':
        if request.method == "POST":
            reply = StudyReply.objects.get(pk=reply_id)
            reply.delete()
            return redirect(f'/community/community_post/{communityid}/{board_id}')
        else:
            return redirect(f'/community/community_post/{communityid}/{board_id}')

    else:
        if request.method == "POST":
            print('POST')
            reply = Reply.objects.get(pk=reply_id)
            reply.delete()
            return redirect(f'/community/community_post/{communityid}/{board_id}')
        else:
            return redirect(f'/community/community_post/{communityid}/{board_id}')

@csrf_exempt
def mypost(request):
    boardList1 = Board.objects.filter(board_type=1, user_id=request.session['user']).order_by('board_id')
    boardList2 = Board.objects.filter(board_type=2, user_id=request.session['user']).order_by('board_id')
    boardList3 = Board.objects.filter(board_type=3, user_id=request.session['user']).order_by('board_id')
    studyList = Study.objects.filter(user_id=request.session['user']).order_by('study_id')
    return render(request, 'community/mypost.html',{'boardList1': boardList1, 'boardList2': boardList2, 'boardList3': boardList3, 'studyList':studyList })