

from django import forms
from .models import Game, Genre_list

class GameCreateForm(forms.ModelForm):

    genre_choice = forms.ModelMultipleChoiceField(queryset=Genre_list.objects.all(),
                                                  widget=forms.CheckboxSelectMultiple())
    # exclude = ['genre']



    class Meta:
        model = Game
        # fields = "__all__"
        # fields = ['title','content']
        #exclude = ['title'] #title 필드만 빼고 나머지 필드드로로 Form Field를 생성
        fields = ['title','genre_choice','developer','release_at','info','pc_requirements_minimum','pc_requirements_recommended',
                'thumbnail','steam','origin','uplay','epic_games','drmfree','video']
    
    
    def save(self, commit=True):
        # genre 리스트 읽어 하나의 문자열로 변환 뒤 Game(모델)의 genre에 추가
        game = self.instance #모델 조회
        genre_list = '/'.join([qs.genre_list for qs in self.cleaned_data['genre_choice']])
        # print(genre_list)
        # Game 모델에 genre 추가
        game.genre = genre_list
        game.save()#모델.salve() => insert
        # print(game.name, game.price, game.genre)
        return game                

# class GameListForm(forms.ModelForm):

#     genre_choice2 = forms.ModelMultipleChoiceField(queryset=Genre_list.objects.all(),
#                                                   widget=forms.CheckboxSelectMultiple())
#     # exclude = ['genre']

#     class Meta:
#         model = Genre_list
#         # fields = "__all__"
#         # fields = ['title','content']
#         #exclude = ['title'] #title 필드만 빼고 나머지 필드드로로 Form Field를 생성
#         fields = ['genre_choice2']