from unittest import TestCase
from weblib import GpxPoint
from weblib import WebTrackConverter


class TestGpxPoint(TestCase):
    def test_parse_from_string(self):
        gpx_point = GpxPoint()
        gpx_point.parse_from_string('54.306409%2C29.130936&')
        self.assertEqual(gpx_point.x, 54.306409)
        self.assertEqual(gpx_point.y, 29.130936)


class TestWebTrackConverter(TestCase):
    def test_create_instance(self):
        yandex_url_two_points = 'https://yandex.ru/maps/213/moscow/?ll=37.817951%2C55.992476&mode=routes&rtext=55.956503%2C37.810247~56.028409%2C37.816743&rtt=bc&ruri=~&z=12.69'
        web_converter = WebTrackConverter.create_instance_from_url(yandex_url_two_points)
        self.assertTrue(len(web_converter.points) == 2)
        yandex_url_tree_points = 'https://yandex.ru/maps/213/moscow/?ll=37.843082%2C55.992476&mode=routes&rtext=55.956503%2C37.810247~55.986895%2C37.878763~56.028409%2C37.816743&rtt=bc&ruri=~~&z=12.69'
        web_converter = WebTrackConverter.create_instance_from_url(yandex_url_tree_points)
        self.assertTrue(len(web_converter.points) == 3)