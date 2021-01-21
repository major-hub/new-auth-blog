from django.urls import path
from .views import contact, HomeListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserNewsView

app_name = 'blog'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('user/<str:username>', UserNewsView.as_view(), name='user-news'),
    path('post/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('post/create', PostCreateView.as_view(), name='create'),
    path('contact/', contact, name='contact'),
]
