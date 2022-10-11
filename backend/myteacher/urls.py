from django.contrib import admin
from django.urls import path
from teacher.views import ProfessorList, CadastrarAulaAPIView
from app.views import HomeAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeAPIView.as_view()),
    path('professores/', ProfessorList.as_view()),
    path('professores/<int:id>/aulas', CadastrarAulaAPIView.as_view())
]