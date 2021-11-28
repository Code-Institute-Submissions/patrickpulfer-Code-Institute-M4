from django.test import TestCase
from .models import Discussion, Forum
from .forms import CommentForm
from django.contrib.auth.models import User


class Testing(TestCase):

    def test_get_home_page(self):
        print('Testing homepage view... ')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/index.html')

    def test_create_instance_of_model(self):
        print('Testing creation of a forum model instance... ')
        forum = Forum.objects.create(
            forum_name='Test',
            topic='Test Topic',
            description='Test Description'
        )
        forum.save()

    def test_get_discussion_view_page(self):
        print('Testing of a complex view that requires chain of FK...')
        forum = Forum.objects.create(
            forum_name='Test',
            topic='Test Topic',
            description='Test Description'
        )
        forum.save()
        user = User.objects.create(
            username='Test Username',
            email='test@test.com',
            password='ComplexPasswordTest1!',
        )
        discussion = Discussion.objects.create(
            title='Test Title', forum=forum, poster=user)
        discussion.save()
        response = self.client.get(f'/forum/discussion/{discussion.title}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/discussion_view.html')

    def test_if_comment_field_is_required(self):
        print('Testing if form of comment is valid...')
        form = CommentForm({
            'body': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_if_model_instance_can_be_deleted(self):
        print('Testing if model instance can be deleted...')
        forum = Forum.objects.create(
            forum_name='Test',
            topic='Test Topic',
            description='Test Description'
        )
        forum.save()
        user = User.objects.create(
            username='Test Username',
            email='test@test.com',
            password='ComplexPasswordTest1!',
        )
        discussion = Discussion.objects.create(
            title='Test Title', forum=forum, poster=user)
        discussion.save()
