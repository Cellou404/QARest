from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AnswerCreate, AnswerDeleteUpdate, AnswerList, QuestionViewSet


router = DefaultRouter()
router.register('question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('question/<slug:slug>/answercreate/', AnswerCreate.as_view()),
    path('question/<slug:slug>/answers/', AnswerList.as_view()),
    path('answers/<int:pk>/', AnswerDeleteUpdate.as_view()),
]