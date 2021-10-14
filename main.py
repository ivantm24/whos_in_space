from printer import CliPrinter, SORT
from service import SpaceService

if __name__ == '__main__':
    url = "api.open-notify.org"
    path = "/astros.json"
    max_width = 200

    ss = SpaceService(url, path)

    res = ss.get_crews()

    print(CliPrinter(res, max_width).get_table(SORT.BY_LAST_NAME))
