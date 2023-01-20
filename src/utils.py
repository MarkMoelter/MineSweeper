import src.settings as settings


def calc_percent_length(percentage: int, length: int):
    return length * percentage // 100


def percent_height(percentage: int):
    return calc_percent_length(percentage, settings.HEIGHT)


def percent_width(percentage: int):
    return calc_percent_length(percentage, settings.WIDTH)
