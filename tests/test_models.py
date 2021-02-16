import unittest
from datetime import datetime
from sdk_dados_abertos_camara import models
from sdk_dados_abertos_camara.models import DATE_FORMAT


class TestModel(unittest.TestCase):
    def test_model_get_date_datetime_format(self):
        m = models.Model({})
        date = m.get_date('2021-01-01T23:59')
        self.assertTrue(isinstance(date, datetime))

    def test_model_get_date_date_format(self):
        m = models.Model({})
        date = m.get_date('2021-01-01', DATE_FORMAT)
        self.assertTrue(isinstance(date, datetime))

    def test_model_get_date_invalid_format(self):
        m = models.Model({})
        date = m.get_date('2021-01-01')
        self.assertEqual(date, '')

    def test_model_get_date_return_empty_string_when_empty(self):
        m = models.Model({})
        date = m.get_date('')
        self.assertEqual(date, '')

    def test_model_get_date_return_empty_string_for_none(self):
        m = models.Model({})
        date = m.get_date(None)
        self.assertEqual(date, '')
