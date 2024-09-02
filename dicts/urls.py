from django.urls import path

from dicts.views.dicts import GendersView, AgeTypeView

urlpatterns = [
    path('dicts/genders/', GendersView.as_view(), name='genders'),
    path('dicts/age-types/', AgeTypeView.as_view(), name='age_types'),
]
