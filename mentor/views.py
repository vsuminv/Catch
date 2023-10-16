from collections import Counter
# from datetime import datetime

import MySQLdb
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .message import Message
from django.db import models
from datetime import timedelta
import datetime
# from .models import Chat_Propose
from django.utils.dateformat import DateFormat
from user.models import User
from mentor.room import Room
import json
from . import room_join, chat_room_service


def mentor_new_message(request):
    print('입장 5초')
    jsonObject = json.loads(request.body)
    print(jsonObject.get('findUser'))
    find_User = jsonObject.get('findUser')
    test = '123'
    print(test)
    session_email = request.session['user']
    login_user = User.objects.get(user_id=session_email)
    my_role = login_user.role
    conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
    cur = conn.cursor()
    cur.nextset()
    session_email2 = "'" + session_email + "'"
    print(session_email2)
    if my_role == 1:
        print('parents')
        query = "select user_user.nickname, room_join.user_id, user_user.img, date_format(date_add(message.updated_at, interval 9 hour),'%Y년%m월%d일 %H시%i분') as currenttime, message.message, message.room_id, user_user.school, user_user.department, user_user.status, user_user.intro_title, user_user.intro_body, user_user.student_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and user_user.role != 1 and room_join.room_id in (select room_id from roomjoin where user_id =" + session_email2 + " ) and user_user.nickname like '%" + find_User + "%' order by date_add(message.updated_at, interval 9 hour) desc"
        # query = "select user_user.name, room_join.email, message.updated_at, message.message, message.room_id from user_user as user_user inner join roomjoin as room_join on user_user.email = room_join.email inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and user_user.role = 'Parents' and room_join.room_id in (select room_id from roomjoin where email =" + myEmail2 + ")"

    else:
        print('not parents')
        query = "select user_user.nickname, user_user.user_id, user_user.img, date_format(date_add(message.updated_at, interval 9 hour),'%Y년%m월%d일 %H시%i분') as currenttime, message.message, message.room_id, user_user.school, user_user.department, user_user.status, user_user.intro_title, user_user.intro_body, user_user.student_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in (select max(id) from message group by room_id) and user_user.role = 1 and room_join.room_id in (select room_id from roomjoin where user_id =" + session_email2 + " ) and user_user.nickname like '%" + find_User + "%' order by date_add(message.updated_at, interval 9 hour) desc"

    result_query2 = cur.execute(query)
    result_query2 = cur.fetchall()

    ajaxOutMessage = []
    for data in result_query2:
        row = {'nickname': data[0],
               'user_id': data[1],
               'user_img': data[2],
               'updated_at': data[3],
               'message': data[4],
               'room_id': data[5],
               'school': data[6],
               'status': data[7],
               'intro_title': data[8],
               'intro_body': data[9],
               'intro_student_id': data[10],
               }

        ajaxOutMessage.append(row)

    return HttpResponse(json.dumps(ajaxOutMessage))


def mentor(request):
    mentorList = User.objects.filter(role=1).order_by('createdTime')
    page = request.GET.get('page', '1')
    paginator = Paginator(mentorList, 99)
    page_obj = paginator.get_page(page)
    IsLogin = request.session.get('user')
    print(IsLogin)
    if IsLogin:
        session_email = request.session['user']
        login_user = User.objects.get(user_id=session_email)
        if login_user.role == 2:
            chat_button = True
            print(chat_button)
        else:
            chat_button = False
            print(chat_button)
        context = {'mentorList': page_obj, "myEmail": session_email, 'chat_button': chat_button}
        print(session_email)
        print(mentorList)
        return render(request, 'mentor/mentor.html', context)
    else:
        chat_button = False
        print(chat_button)
        notemail = ''
        context = {'mentorList': page_obj, "myEmail": notemail, 'chat_button': chat_button}
        return render(request, 'mentor/mentor.html', context)


# def mentor_chatrooms(request):
#     return render(request, 'mentor/mentor_chatrooms.html')

#
def mentor_chatrooms(request: HttpRequest, myEmail: str, user_id: str) -> HttpResponse:
    print('id:' + user_id)
    login_user = User.objects.get(user_id=myEmail)
    print(login_user)
    #  채팅방생성
    print('여기 입장')
    if myEmail != user_id:
        # if id != 'mypage':
        user1 = User.objects.get(user_id=myEmail)
        user2 = User.objects.get(user_id=user_id)
        print(user1, user2)
        print(user1.user_id, user2.user_id)
        room_id = 0

        # conn = MySQLdb.connect(host='localhost', user='root', passwd='etoile0320!@#', db='Catch')


        # conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
        

        conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
        cur = conn.cursor()
        cur.nextset()
        compareEmail1 = "'" + user1.user_id + "'"
        compareEmail2 = "'" + user2.user_id + "'"
        # query = "select roomjoin.room_id from roomjoin as roomjoin inner join user_user as user on user.user_id = roomjoin.user_id where user.user_id in (" + compareEmail1 + ", " + compareEmail2 + ") group by roomjoin.room_id "
        query = "select roomjoin.room_id as room_id from roomjoin where roomjoin.user_id in (" + compareEmail1 + ", " + compareEmail2 + ")"
        print(query)
        result_query = cur.execute(query)
        result_query = cur.fetchall()
        print(result_query)

        result_out = []
        for data in result_query:
            row = {'room_id': data[0]}
            result_out.append(row)

        print(result_out)

        find_room_list = []
        for find_room in result_out:
            print(find_room.get('room_id'))
            find_room_list.append(find_room.get('room_id'))

        result = Counter(find_room_list)
        room_id = 0

        for key, value in result.items():
            if value >= 2:
                print('이미 있다')
                print(key)
                print(str(key))
                print(user1.user_id)
                room_id = key
                break
                # return redirect("../chat/" + str(key.id) + "/" + str(user1.email))

        if room_id == 0:
            room = chat_room_service.creat_an_chat_room()
            room_id = room.id
            # chat_room_service.creat_an_room_join(user1, user2, room)
            chat_room_service.creat_an_room_join(user1.user_id, user2.user_id, room)
            print('여기도 입장 + 채팅글귀 공백입력')
            conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
            cur = conn.cursor()
            cur.nextset()
            compareEmail1 = "'" + user1.user_id + "'"
            compareEmail2 = "'" + user2.user_id + "'"

            currenttime = str(datetime.datetime.now())
            # nowStr = "'" + currenttime + "'"
            print(currenttime)
            User.objects.get(user_id=user1.user_id)
            currenttime2 = "'" + currenttime + "'"

            Message(
                user_id=User.objects.get(user_id=user1.user_id),
                room_id=Room.objects.get(id=room_id),
                message='멘토님에게 채팅을 신청합니다.',
                created_at=currenttime2,
                updated_at=currenttime2
            ).save()

            Message(
                user_id=User.objects.get(user_id=user2.user_id),
                room_id=Room.objects.get(id=room_id),
                message='멘토님과 채팅을 시작하세요!',
                created_at=currenttime2,
                updated_at=currenttime2
            ).save()

            # currenttime2 = str(currenttime)

            # print(currenttime3)
            # query2 = "insert into message (id,updated_at, created_at, message, user_id, room_id) values (" + '12' + "," + str(currenttime2) + "," + str(currenttime2) + ",'ddd'," + compareEmail1 + "," + str(room_id) + ");"
            # # # # # # query2 = "insert into catch.message (updated_at, created_at, room_id) values (" + now + "," + now + ",''," + room_id + ");"
            # result_query2 = cur.execute(query2)
            # result_query2 = cur.fetchall()
            # print(result_query2)

        # result_out = []
        # for data in result_query:
        #     row = {'room_number': data[0]
        #             }
        #     result_out.append(row)
        # print(result_out[0])
        # print(result_out.__len__())

        # if result_out.__len__() >= 2:
        #     print('이미 있다')
        #     print(str(result_out[0].room_number))
        #     print(user1.user_id)
        #     room_id = result_out[0].room_number
        #     # return redirect("../chat/" + str(key.id) + "/" + str(user1.email))

        # if result_out.__len__() == 1:
        #
        #     room = chat_room_service.creat_an_chat_room()
        #     room_id = room.id
        #     # chat_room_service.creat_an_room_join(user1, user2, room)
        #     chat_room_service.creat_an_room_join(user1.user_id, user2.user_id, room)
        #     print('여기도 입장')

        # find_room_qs = room_join.RoomJoin.objects.filter(user_id__in=[user1.user_id, user2.user_id])
        # find_room_qs = room_join.RoomJoin.objects.filter(user_id=[user1.user_id])
        # 이러면 1번 유저가 참여한 모든 방, 2번 유저가 모두 참여한 방 가져옴
        # print(find_room_qs)
        # find_room_list = []
        # for find_room in find_room_qs:
        #     find_room_list.append(find_room.room_id)
        #
        # result = Counter(find_room_list)
        # room_id = 0
        # result = 1
        # for key, value in result.items():
        #     if value >= 2:
        #         print('이미 있다')
        #         print(str(key.id))
        #         print(user1.user_id)
        #         room_id = key.id
        #         break
        #         # return redirect("../chat/" + str(key.id) + "/" + str(user1.email))

        # if room_id == 0:
        #
        #     room = chat_room_service.creat_an_chat_room()
        #     room_id = room.id
        #     chat_room_service.creat_an_room_join(user1, user2, room)
        #     print('여기도 입장')

        print('최종관문')

        my_role = login_user.role
        conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
        cur = conn.cursor()
        cur.nextset()
        myEmail2 = "'" + myEmail + "'"
        print(myEmail2)
        if my_role == 1:
            print('parents')
            query = "select user_user.nickname, room_join.user_id, user_user.img, date_format(date_add(message.updated_at, interval 9 hour),'%Y년%m월%d일 %H시%i분') as currenttime, message.message, message.room_id, user_user.school, user_user.department, user_user.status, user_user.intro_title, user_user.intro_body, user_user.student_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and user_user.role != 1 and room_join.room_id in (select room_id from roomjoin where user_id =" + myEmail2 + " ) order by date_add(message.updated_at, interval 9 hour) desc"
            # query = "select user_user.name, room_join.email, message.updated_at, message.message, message.room_id from user_user as user_user inner join roomjoin as room_join on user_user.email = room_join.email inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and user_user.role = 'Parents' and room_join.room_id in (select room_id from roomjoin where email =" + myEmail2 + ")"

        else:
            print('not parents')
            query = "select user_user.nickname, user_user.user_id, user_user.img, date_format(date_add(message.updated_at, interval 9 hour),'%Y년%m월%d일 %H시%i분') as currenttime, message.message, message.room_id, user_user.school, user_user.department, user_user.status, user_user.intro_title, user_user.intro_body, user_user.student_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in (select max(id) from message group by room_id) and user_user.role = 1 and room_join.room_id in (select room_id from roomjoin where user_id =" + myEmail2 + " ) order by date_add(message.updated_at, interval 9 hour) desc"

        result_query = cur.execute(query)
        result_query = cur.fetchall()

        result_out = []
        for data in result_query:
            row = {'nickname': data[0],
                   'user_id': data[1],
                   'user_img': data[2],
                   'updated_at': data[3],
                   'message': data[4],
                   'room_id': data[5],
                   'school': data[6],
                   'status': data[7],
                   'intro_title': data[8],
                   'intro_body': data[9],
                   'intro_student_id': data[10],
                   }

            result_out.append(row)

        print(result_query)

        return render(request, 'mentor/mentor_chatrooms.html',
                      {'result_query': result_out, 'room_name': room_id, 'login_user': login_user, 'myEmail': myEmail})
    # 마이페이지일때
    else:
        print('마이페이지 아이디 두개' + myEmail + ' ' + user_id)
        roommyemail = "'" + myEmail + "'"
        conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
        cur = conn.cursor()
        cur.nextset()
        # roomquery = "select user_user.name, room_join.user_id, date_add(message.updated_at, interval 9 hour) as currenttime, message.message, message.room_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and room_join.room_id in (select room_id from roomjoin where user_id = 'jaesok') and user_user.user_id = 'jaesok' order by currenttime desc limit 1")
        roomquery = "select message.room_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and room_join.room_id in (select room_id from roomjoin where user_id = " + roommyemail + ") and user_user.user_id = " + roommyemail + " order by date_add(message.updated_at, interval 9 hour) desc limit 1;"
        result_roomquery = cur.execute(roomquery)
        result_roomquery = cur.fetchall()
        real_roomnum = 0
        print(real_roomnum)

        result_roomout = []
        for data in result_roomquery:
            real_roomnum = data[0]
        print(real_roomnum)
        my_role = login_user.role
        conn = MySQLdb.connect(host='localhost', user='root', passwd='catch2022!@#', db='Catch')
        cur = conn.cursor()
        cur.nextset()
        myEmail2 = "'" + myEmail + "'"
        print(myEmail2)
        if my_role == 1:
            print('parents')
            query = "select user_user.nickname, room_join.user_id, user_user.img, date_format(date_add(message.updated_at, interval 9 hour),'%Y년%m월%d일 %H시%i분') as currenttime, message.message, message.room_id, user_user.school, user_user.department, user_user.status, user_user.intro_title, user_user.intro_body, user_user.student_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and user_user.role != 1 and room_join.room_id in (select room_id from roomjoin where user_id =" + myEmail2 + ") order by date_add(message.updated_at, interval 9 hour) desc"
            # query = "select user_user.name, room_join.email, message.updated_at, message.message, message.room_id from user_user as user_user inner join roomjoin as room_join on user_user.email = room_join.email inner join message as message on room_join.room_id = message.room_id where message.id in ( select max(id) from message group by room_id) and user_user.role = 'Parents' and room_join.room_id in (select room_id from roomjoin where email =" + myEmail2 + ")"

        else:
            print('not parents')
            query = "select user_user.nickname, user_user.user_id, user_user.img, date_format(date_add(message.updated_at, interval 9 hour),'%Y년%m월%d일 %H시%i분') as currenttime, message.message, message.room_id, user_user.school, user_user.department, user_user.status, user_user.intro_title, user_user.intro_body, user_user.student_id from user_user as user_user inner join roomjoin as room_join on user_user.user_id = room_join.user_id inner join message as message on room_join.room_id = message.room_id where message.id in (select max(id) from message group by room_id) and user_user.role = 1 and room_join.room_id in (select room_id from roomjoin where user_id =" + myEmail2 + ") order by date_add(message.updated_at, interval 9 hour) desc"

        result_query = cur.execute(query)
        result_query = cur.fetchall()

        result_out = []
        for data in result_query:
            row = {'nickname': data[0],
                   'user_id': data[1],
                   'user_img': data[2],
                   'updated_at': data[3],
                   'message': data[4],
                   'room_id': data[5],
                   'school': data[6],
                   'status': data[7],
                   'intro_title': data[8],
                   'intro_body': data[9],
                   'intro_student_id': data[10],
                   }

            result_out.append(row)

        print(result_query)

        return render(request, 'mentor/mentor_chatrooms.html',
                      {'result_query': result_out, 'room_name': real_roomnum, 'login_user': login_user,
                       'myEmail': myEmail})

    # Chat_Propose.objects.select_related('mentor').filter(my_email=myEmail, Mentor_number=1)
    # bothPropose = Chat_Propose.objects.filter(my_email=myEmail, Mentor_number=1)

    # return render(request, 'mentor/mentor_chatrooms.html',
    #               {'bothPropose': bothPropose})

    #
    # def chat_propose(request, email):
    #     print('입장')
    #     session_email = request.session['user']
    #     mentoUser = User.objects.filter(role='Mentor')
    #     session_user = request.session['user']
    #     login_user = User.objects.get(email=session_user)
    #     if login_user.role == 'Parents':
    #         isParents = True
    #         bothPropose = Chat_Propose.objects.filter(my_email=session_user, Mentor_number=1)
    #     else:
    #         isParents = False
    #         bothPropose = Chat_Propose.objects.filter(email_id=session_user, Mentor_number=1)
    #
    #     myPropose = Chat_Propose.objects.filter(my_email=session_user, Mentor_number=0)
    #     receivePropose = Chat_Propose.objects.filter(email_id=session_user, Mentor_number=0, Parents_number=1)
    #     # conn = MySQLdb.connect(host='localhost', user='root', passwd='Fleur0320!@#', db='django_insta')
    #     # cur = conn.cursor()
    #     # cur.nextset()
    #     # cur.execute('call propose_chat(%s, %s)', {session_email, email})
    #     if Chat_Propose.objects.filter(my_email=session_email, email=email).exists():
    #         return render(request, 'mypage/mypage.html',
    #                       {'mentoUser': mentoUser, 'isParents': isParents, 'myPropose': myPropose,
    #                        'receivePropose': receivePropose, 'bothPropose': bothPropose})
    #     else:
    #         login_user = User.objects.get(email=session_email)
    #         Chat_Propose(
    #             email_id=email,
    #             name=login_user.name,
    #             nickname=login_user.nickname,
    #             my_email=session_email,
    #             Parents_number=1,
    #             Mentor_number=0
    #         ).save()
    #
    #         return render(request, 'mypage/mypage.html')
    #         # return redirect('mypage')
    #         # return redirect('reservationChat')

    # def api_create_room(request: HttpRequest, email: str) -> HttpResponse:
    print('여기 입장')
    user1 = User.objects.get(user_id=user_id)
    session = request.session['user']
    user2 = User.objects.get(user_id=session)

    find_room_qs = room_join.RoomJoin.objects.filter(user_id=[user1.user_id, user2.user_id])
    # 이러면 1번 유저가 참여한 모든 방, 2번 유저가 모두 참여한 방 가져옴

    find_room_list = []
    for find_room in find_room_qs:
        find_room_list.append(find_room.room_id)

    result = Counter(find_room_list)
    for key, value in result.items():
        if value >= 2:
            print('이미 있다')
            print(str(key.id))
            print(user1.user_id)
            return redirect("../chat/" + str(key.id) + "/" + str(user1.user_id))

    room = chat_room_service.creat_an_chat_room()
    room_id = room.id
    chat_room_service.creat_an_room_join(user1, user2, room)
    print('여기도 입장')
    return redirect(("../chat/" + str(room_id) + "/" + str(user1.user_id)))
    # return redirect(("/chat/" + str(room_id)))

    # def search(request):
    context = dict()
    mentorList = Mentor.objects.filter(mentor__icontains="")
