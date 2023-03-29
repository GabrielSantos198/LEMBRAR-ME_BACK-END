from django.urls import path
from . views import SiteContentView, AnnotationListView, AnnotationCreateView, AnnotationDeleteView, AnnotationDetailView, AnnotationUpdateView

urlpatterns = [
    path('', SiteContentView.as_view(), name='site-content'),
    path('annotations/', AnnotationListView.as_view(), name='annotations'),
    path('annotations/<int:pk>/', AnnotationDetailView.as_view(), name='annotation-detail'),
    path('annotations/update/<int:pk>/', AnnotationUpdateView.as_view(), name='update-annotation'),
    path('create/annotation/', AnnotationCreateView.as_view(), name='create-annotation'),
    path('delete/annotation/<int:pk>/', AnnotationDeleteView.as_view(), name='delete-annotation'),
]

