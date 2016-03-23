from json import loads

from courseaffils.models import Course
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from django.test.testcases import TestCase

from mediathread.discussions.utils import get_course_discussions
from mediathread.discussions.views import \
    discussion_create, DiscussionView
from mediathread.main.tests.factories import (
    MediathreadTestMixin, ProjectFactory
)
from structuredcollaboration.models import Collaboration


class DiscussionViewsTest(MediathreadTestMixin, TestCase):

    def test_create_discussions(self):
        self.setup_sample_course()
        self.setup_alternate_course()

        self.create_discussion(self.sample_course, self.instructor_one)
        self.create_discussion(self.alt_course, self.alt_instructor)

        discussions = get_course_discussions(self.sample_course)
        self.assertEquals(1, len(discussions))
        self.assertEquals(discussions[0].title, "Sample Course Discussion")

        discussions = get_course_discussions(self.alt_course)
        self.assertEquals(1, len(discussions))
        self.assertEquals(discussions[0].title, "Alternate Course Discussion")

    def test_create_instructor_feedback(self):
        self.setup_sample_course()
        project = ProjectFactory.create(
            course=self.sample_course, author=self.student_one,
            policy='InstructorShared')

        data = {
            'publish': 'PrivateStudentAndFaculty',
            'inherit': 'true',
            'app_label': 'projects',
            'model': 'project',
            'obj_pk': project.id,
            'comment_html': 'Instructor Feedback'
        }
        request = RequestFactory().post('/discussion/create/', data)
        request.user = self.instructor_one
        request.course = self.sample_course
        request.collaboration_context, created = \
            Collaboration.objects.get_or_create(
                content_type=ContentType.objects.get_for_model(Course),
                object_pk=str(self.sample_course.pk))
        discussion_create(request)

        discussion = project.feedback_discussion()
        self.assertIsNotNone(discussion)

    def test_delete_discussions(self):
        self.setup_sample_course()
        self.create_discussion(self.sample_course, self.instructor_one)
        discussions = get_course_discussions(self.sample_course)
        self.assertEquals(1, len(discussions))

        discussion = discussions[0]
        discussion_id = discussions[0].id
        ctype = ContentType.objects.get(model='threadedcomment',
                                        app_label='threadedcomments')
        coll = Collaboration.objects.get(content_type=ctype,
                                         object_pk=str(discussion_id))
        self.assertEquals(coll.content_object, discussion)

        url = reverse('discussion-delete', args=[discussion_id])

        # anonymous
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 302)

        # non-faculty
        self.client.login(username=self.student_one.username, password='test')
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 403)

        # faculty
        self.client.login(username=self.instructor_one.username,
                          password='test')
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 302)
        discussions = get_course_discussions(self.sample_course)
        self.assertEquals(0, len(discussions))

        with self.assertRaises(Collaboration.DoesNotExist):
            Collaboration.objects.get(content_type=ctype,
                                      object_pk=str(discussion_id))

    def test_view_discussions(self):
        self.setup_sample_course()
        self.create_discussion(self.sample_course, self.instructor_one)
        discussions = get_course_discussions(self.sample_course)
        self.assertEquals(1, len(discussions))

        request = RequestFactory().get('/discussion/', {})
        request.user = self.instructor_one
        request.course = self.sample_course
        request.collaboration_context, created = \
            Collaboration.objects.get_or_create(
                content_type=ContentType.objects.get_for_model(Course),
                object_pk=str(self.sample_course.pk))

        view = DiscussionView()
        view.request = request
        response = view.get(request, discussion_id=discussions[0].id)
        self.assertEquals(response.status_code, 200)

    def test_view_discussions_ajax(self):
        self.setup_sample_course()
        self.create_discussion(self.sample_course, self.instructor_one)
        discussions = get_course_discussions(self.sample_course)
        self.assertEquals(1, len(discussions))

        request = RequestFactory().get('/discussion/', {},
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.instructor_one
        request.course = self.sample_course
        request.collaboration_context, created = \
            Collaboration.objects.get_or_create(
                content_type=ContentType.objects.get_for_model(Course),
                object_pk=str(self.sample_course.pk))

        view = DiscussionView()
        view.request = request
        response = view.get(request, discussion_id=discussions[0].id)
        self.assertEquals(response.status_code, 200)

        the_json = loads(response.content)
        self.assertEquals(the_json['space_owner'],
                          self.instructor_one.username)
