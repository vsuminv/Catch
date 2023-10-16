from django.db import models


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    regdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, to_field='user_id')
    board_type = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)
    board_id = models.ForeignKey('Board', on_delete=models.CASCADE, to_field='board_id')
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, to_field='user_id')


class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    contact = models.CharField(max_length=45)  # 연락방법
    process = models.CharField(max_length=45)  # 진행방식
    members = models.CharField(max_length=20)  # 인원수
    start_date = models.CharField(max_length=45)  # 시작예정
    study_period = models.CharField(max_length=45)  # 예상기간
    due_date = models.CharField(max_length=45)  # 모집 기간
    title = models.CharField(max_length=200)  # 스터디 제목
    content = models.CharField(max_length=200)  # 스터디 컨텐츠
    tag = models.CharField(max_length=200) #태그
    regdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, to_field='user_id')



class StudyReply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)
    board_id = models.ForeignKey('Study', on_delete=models.CASCADE, to_field='study_id')
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, to_field='user_id')
