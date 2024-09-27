from django.test import TestCase
from todo.models import TodoModel


class TodoTest(TestCase):
    def setUp(self):
        TodoModel.objects.create(name="Sumit", desc="Very handsome man")
        TodoModel.objects.create(name="Richa", desc="Very beautiful woman")

    def test_model_with_descriptions(self):
        _sumit = TodoModel.objects.get(name="Sumit")
        _richa = TodoModel.objects.get(name="Richa")

        self.assertEqual(_sumit.desc, "Very handsome man")
        self.assertEqual(_richa.desc, "Very beautiful woman")
