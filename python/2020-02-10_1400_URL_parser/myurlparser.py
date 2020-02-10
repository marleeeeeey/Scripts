from urllib.parse import urlparse
import argparse
import webbrowser


class GpxPoint:
    def __init__(self, str_point = None):
        if (str_point == None):
            self.x = 0
            self.y = 0
            return
        xy = str_point.split(',')
        if len(xy) != 2:
            raise Exception("Can't parse point")
        self.x = xy[0]
        self.y = xy[1]

    def __str__(self):
        return "(x=" + str(self.x) + "; y=" + str(self.y) + ")"

    def __repr__(self):
        return "(x=" + str(self.x) + "; y=" + str(self.y) + ")" # TODO fix dublication


class GpxRoute:
    def __init__(self):
        self.points = []
        self.center = GpxPoint()
        self.zoom = 0.0

    @staticmethod
    def url_parse_google(url):
        url_path = urlparse(url).path
        split_points_and_center = url_path.split("dir/")[1].split("@")
        str_points = split_points_and_center[0].split('/')
        str_center_and_zoom = split_points_and_center[1].split('/')[0].split(',')
        center = GpxPoint()
        center.x = str_center_and_zoom[0]
        center.y = str_center_and_zoom[1]
        zoom = float(str_center_and_zoom[2].replace('z', ''))
        gpx_points = []
        for str_point in str_points:
            try:
                gpx_point = GpxPoint(str_point)
            except:
                continue
            gpx_points.append(gpx_point)
        gpx_route = GpxRoute()
        gpx_route.points = gpx_points
        gpx_route.center = center
        gpx_route.zoom = zoom
        return gpx_route

    @staticmethod
    def url_parse_graphhopper(url):
        url_query = urlparse(url).query
        str_points = url_query.split("&locale")[0].split("point=")
        gpx_points = []
        for str_point in str_points:
            try:
                str_point = str_point.replace("%2C", ",").replace("&", "")
                gpx_point = GpxPoint(str_point)
            except:
                continue
            gpx_points.append(gpx_point)
        gpx_route = GpxRoute()
        gpx_route.points = gpx_points
        return gpx_route

    @staticmethod
    def url_parse_yandex(url):
        url_query = urlparse(url).query
        split_center_and_points_str = url_query.split("&rtt=")[0].split("&rtext=")
        center_xy_str = split_center_and_points_str[0].split("ll=")[1].split("&mode")[0].replace("%2C", ",")
        center = GpxPoint(center_xy_str)
        str_points = split_center_and_points_str[1].split("~")
        gpx_points = []
        for str_point in str_points:
            try:
                str_point = str_point.replace("%2C", ",")
                gpx_point = GpxPoint(str_point)
            except:
                continue
            gpx_points.append(gpx_point)
        gpx_route = GpxRoute()
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
        return "(points_number=" + str(len(self.points)) + "; center=" + str(self.center) + "; zoom=" + str(self.zoom) + ")"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_url", type=str, required=True, help="url")
    parser.add_argument("-e", "--export_format", type=str, required=True, help = "graphhopper/yandex/google")
    args = parser.parse_args()

    input_url = args.input_url
    gpx_route = GpxRoute
    if 'yandex' in input_url:
        gpx_route = GpxRoute.url_parse_yandex(input_url)
    elif 'graphhopper' in input_url:
        gpx_route = GpxRoute.url_parse_graphhopper(input_url)
    elif 'google' in input_url:
        gpx_route = GpxRoute.url_parse_google(input_url)
    else:
        raise Exception("Unknow type of input url")

    export_format = args.export_format
    export_url = ''
    if export_format == 'graphhopper':
        export_url = gpx_route.export_url_graphhopper()
    else:
        raise Exception("Unknown type of export url")

    webbrowser.open(export_url)


main()
