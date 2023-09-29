from rest_framework import viewsets

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # Новая запись в БД создаётся при вызове метода save() 
    # сериализатора, а этот метод вызывается из метода вьюсета perform_create().
    # Чтобы передать новое значение для какого-то поля в метод save(), 
    # нужно переопределить метод perform_create(). 
    # При подобных операциях с PUT- и PATCH-запросами
    # следует переопределить метод perform_update(), а в остальном всё работает так же.

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
