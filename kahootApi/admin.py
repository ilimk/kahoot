from django.contrib import admin
from .models import User, Group, Test, Question, Answer, UserAnswer

from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter

class FilterBySortingGoup(admin.SimpleListFilter):
    title = _('group_name')
    parameter_name = 'group_name'
# list(Group.objects.all().filter(id = list(User.objects.all().filter(user_name = 'ilim').values('group_name')[0].values())[0]).values()[0].values())[1]

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        # print(Group.objects.all().filter(id = i))
        return [(i, Group.objects.all().get(id = i)) for i in qs.values_list('group_name', flat=True) \
            .distinct().order_by('-group_name')]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(group_name__exact=self.value())

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'user_surname',
        'group_name',
        'phone_number',
        'login',
        'rating',
        'score',
    )

    search_fields = ['user_name', 'user_surname', 'phone_number']

    list_filter = (FilterBySortingGoup,)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'group_name',
    )

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'test_name',
        'group',
        'active',
        'count_questions',
        'count_partisipant',
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'test_name',
        'question',
        'image',
    )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'timer',
        'is_right',
        'score'
    )

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'test_name',
        'questions',
        'answer',
        'second',
    )