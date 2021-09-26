from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls.base import reverse_lazy

from polls import models

HTTP_200_OK = 200
USERNAME = "jackm"
PASSWORD = "qwerty"
class BaseTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.site = models.Site.objects.create(domain="test")
        models.ProfileForm.objects.create(
            form_fields={
                "fields" :[
                    {
                        "label": "City",
                        "id": "city",
                        "type": "text",
                        "required": True,
                    },
                    {
                        "label": "Function",
                        "type": "select",
                        "id": "function",
                        "choices": [
                        ["", "Select a department"],
                        ["development", "Development"],
                        ["sales", "Sales"],
                        ["marketing", "Marketing"]
                        ],
                        "required": True
                    }
                ]
            },
            site=self.site
        )
        user = User.objects.create_user(
            username=USERNAME,
            first_name="Jack",
            last_name="Mosley",
            password=PASSWORD,
        )
        self.profile = models.Profile.objects.create(
            site=self.site,
            user=user,
            dynamic_fields={
                "city": "London",
                "function": "development",
            },
        )
        self.poll = models.Poll.objects.create(
            title="What is your favourite color?",
        )
        self.answer = models.Answer.objects.create(
            poll=self.poll,
            user=user,
            value="Red is my favourite color",
        )
        self.client = Client()

class TestLogin(BaseTestCase):
    def test_login_template(self):
        response = self.client.get(path=reverse("login"))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_success(self):
        login_success = self.client.login(username=USERNAME, password=PASSWORD)
        assert login_success, "Login Failed"

    def test_login_failure(self):
        login_success = self.client.login(username=USERNAME, password="random")
        assert not login_success, "Login did not fail"

class TestIndexView(BaseTestCase):
    def setUp(self):
        super().setUp()
        login_success = self.client.login(username=USERNAME, password=PASSWORD)
        assert login_success, "Login failed"

    def test_polls_displayed(self):
        response = self.client.get(reverse("index"), follow=True)
        assert response.status_code == HTTP_200_OK, response.status_code
        self.assertTemplateUsed(response, 'polls/index.html')
        self.assertContains(response, "What is your favourite color?")
        self.assertContains(response, "Red is my favourite color")
        self.assertContains(response, "Jack")
        self.assertContains(response, "Mosley")

    def test_profile_page(self):
        response = self.client.get(reverse("my_profile"), follow=True)
        assert response.status_code == HTTP_200_OK, response.status_code
        self.assertTemplateUsed(response, 'polls/current_user.html')
        first_name_input = (
            '<input type="text" '
            'name="first_name" '
            'value="Jack" required '
            'id="id_first_name">'
        )
        last_name_input = (
            '<input type="text" '
            'name="last_name" '
            'value="Mosley" required '
            'id="id_last_name">'
        )

        self.assertContains(response, first_name_input)
        self.assertContains(response, last_name_input)


class TestPerformance(BaseTestCase):
    ANSWER_COUNT = 5

    def setUp(self):
        super().setUp()
        User.objects.bulk_create([
            User(username=f"user+{i}")
            for i in range(self.ANSWER_COUNT)
        ])
        self.users = models.User.objects.all()
        self.answers = models.Answer.objects.bulk_create([
            models.Answer(poll=self.poll, user=self.users[i], value='x')
            for i in range(self.ANSWER_COUNT)
        ])
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_querycount(self):
        with self.assertNumQueries(13):
            self.client.get(reverse('index'))


class TestPollsMiddleware(BaseTestCase):
    def test_redirect(self):
        user = models.User.objects.create_user(
            username="random",
            password="random",
        )
        models.Profile.objects.create(user=user, site=self.site, dynamic_fields=[])
        login = self.client.login(username="random", password="random")
        assert login, "Login Failed"
        response = self.client.get(reverse("index"), follow=True)
        self.assertRedirects(response, reverse("my_profile"))
