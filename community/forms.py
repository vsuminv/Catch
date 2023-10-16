from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget
from .models import Board, Reply, StudyReply


class BoardWriteForm(forms.ModelForm):
    title = forms.CharField(
        label='게시글 제목:',

        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력해 주세요.'
            }),
        required=True,
    )

    content = SummernoteTextField()

    field_order = [
        'title',
        'content'
    ]

    class Meta:
        model = Board
        fields = [
            'title',
            'content'
        ]
        widgets = {
            'content': SummernoteWidget()
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content = cleaned_data.get('content', '')

        if title == '':
            self.add_error('title', "글 제목을 입력하세요. ")
        elif content == '':
            self.add_error('content', '글 내용을 입력하세요.')
        else:
            self.title = title
            self.content = content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']


class CommentStudyForm(forms.ModelForm):
    class Meta:
        model = StudyReply
        fields = ['content']