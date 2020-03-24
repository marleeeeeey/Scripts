from urllib.parse import urlparse


class GpxPoint:
    def __init__(self):
        self.x : float = 0
        self.y : float = 0

    def parse_from_string(self, str_point):
        str_point = str_point.replace("%2C", ",").replace("&", "")
        xy = str_point.split(',')
        if len(xy) != 2:
            raise Exception("Can't construct point")
        self.x = float(xy[0])
        self.y = float(xy[1])

    def _print_str(self):
        return "(x=" + str(self.x) + "; y=" + str(self.y) + ")"

    def __str__(self):
        return self._print_str()

    def __repr__(self):
        return self._print_str()


class WebTrackConverter:
    def __init__(self):
        self.points = []
        self.center = GpxPoint()
        self.zoom = 0.0

    @staticmethod
    def create_instance(url):
        if "google" in url:
            return WebTrackConverter._url_parse_google(url)
        elif "graphhopper" in url:
            return WebTrackConverter._url_parse_graphhopper(url)
        elif "yandex" in url:
            return WebTrackConverter._url_parse_yandex(url)
        else:
            raise Exception("Unknown route provider(url)")

    @staticmethod
    def _url_parse_google(url):
        url_path = urlparse(url).path
        split_points_and_center = url_path.split("dir/")[1].split("@")
        str_points = split_points_and_center[0].split('/')
        str_center_and_zoom = split_points_and_center[1].split('/')[0].split(',')
        center = GpxPoint()
        center.x = str_center_and_zoom[0]
        center.y = str_center_and_zoom[1]
        zoom = float(str_center_and_zoom[2].replace('z', '').replace('m', ''))
        gpx_points = []
        for str_point in str_points:
            try:
                gpx_point = GpxPoint()
                gpx_point.parse_from_string(str_point)
            except:
                continue
            gpx_points.append(gpx_point)
        gpx_route = WebTrackConverter()
        gpx_route.points = gpx_points
        gpx_route.center = center
        gpx_route.zoom = zoom
        return gpx_route

    @staticmethod
    def _url_parse_graphhopper(url):
        url_query = urlparse(url).query
        str_points = url_query.split("&locale")[0].split("point=")
        gpx_points = []
        for str_point in str_points:
            gpx_point = GpxPoint()
            try:
                gpx_point.parse_from_string(str_point)
            except:
                continue
            gpx_points.append(gpx_point)
        gpx_route = WebTrackConverter()
        gpx_route.points = gpx_points
        return gpx_route

    @staticmethod
    def _url_parse_yandex(url):
        url_query = urlparse(url).query
        split_center_and_points_str = url_query.split("&rtt=")[0].split("&rtext=")
        center_xy_str = split_center_and_points_str[0].split("ll=")[1].split("&mode")[0].replace("%2C", ",")
        center = GpxPoint()
        center.parse_from_string(center_xy_str)
        str_points = split_center_and_points_str[1].split("~")
        gpx_points = []
        for str_point in str_points:
            gpx_point = GpxPoint()
            try:
                gpx_point.parse_from_string(str_point)
            except:
                continue
            gpx_points.append(gpx_point)
        gpx_route = WebTrackConverter()
        gpx_route.points = gpx_points
        gpx_route.center = center
        return gpx_route

    def export_url_graphhopper(self):
        url = "https://graphhopper.com/maps/?"
        for point in self.points:
            url += "point=" + str(point.x) + "%2C" + str(point.y) + "&";
        url += "locale=en-US&vehicle=bike&weighting=fastest&elevation=true&turn_costs=false&use_miles=false&layer=OpenStreetMap"
        return url

    def __str__(self):
        return "(points_number=" + str(len(self.points)) + "; center=" + str(self.center) + "; zoom=" + str(
            self.zoom) + ")"

class WebPointSearchEngine:
    def __init__(self):
        # TODO
        pass

    def find_by_name(self, name):
        # TODO
        pass