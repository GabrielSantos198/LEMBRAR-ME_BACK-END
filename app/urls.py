from django.urls import path
from app import views

urlpatterns = [
    path('', views.SiteContentView.as_view(), name='site-content'),
    path('annotations/', views.AnnotationListView.as_view(), name='annotations'),
    path('annotations/search/', views.AnnotationSearchView.as_view(), name='search-annotations'),
    path('annotations/<int:pk>/', views.AnnotationDetailView.as_view(), name='annotation-detail'),
    path('annotations/update/<int:pk>/', views.AnnotationUpdateView.as_view(), name='update-annotation'),
    path('create/annotation/', views.AnnotationCreateView.as_view(), name='create-annotation'),
    path('delete/annotation/<int:pk>/', views.AnnotationDeleteView.as_view(), name='delete-annotation'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('auth/google/', views.GoogleLogin.as_view(), name='socialaccount_signup')
]

