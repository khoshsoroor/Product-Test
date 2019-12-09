from aloe import *
import requests
from .. import config, logger

# region Return category from city
@step(r'Get list of categories for city (\S+)')
def get_all_list_city_category(_, slug):
    res = requests.get(f"{config.base_api_uri}/cities/{slug}/categories")
    world.city_category_status = res.status_code


@step(r"return code city categories must be (\d+)")
def check_code_city_category(_, status_code):
    logger.info(world.city_category_status)
    assert world.city_category_status == int(status_code)
# region

# region not found any category from city
@step(r'Get categories for a city (\S+)')
def not_found_category_city(_, slug):
    res = requests.get(f"{config.base_api_uri}/cities/{slug}/categories")
    world.city_category_not_found_status = res.status_code


@step(r"result code for category city must be (\d+)")
def check_code_city_category(_, status_code):
    logger.info(world.city_category_not_found_status)
    assert world.city_category_not_found_status == int(status_code)
# region
