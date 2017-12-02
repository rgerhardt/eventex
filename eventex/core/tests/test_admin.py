from django.contrib import admin
from django.test import TestCase

from eventex.core.admin import TalkModelAdmin
from eventex.core.models import Talk, Course


class TalkModelAdminListTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title='Título da Palestra')
        self.course = Course.objects.create(title='Título do Curso', slots=20)

        self.model_admin = TalkModelAdmin(Talk, admin.site)

        self.qs = self.model_admin.get_queryset(None)

    def test_should_only_list_talks(self):
        self.assertQuerysetEqual(self.qs, [self.talk.pk], transform=lambda t: t.pk)

    def test_should_not_list_any_course(self):
        self.assertNotIn(self.course, self.qs)