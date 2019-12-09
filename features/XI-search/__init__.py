from aloe import *
import requests
from .. import config, logger


# region list of services with short keyword tags
@step(r'Get services with keyword (\S+)')
def get_list_keyword(_, search_item):
    res = requests.get(f"{config.base_api_uri}/search/{search_item}")
    world.search_keyword_status = res.status_code


@step(r"second return code search must be (\d+)")
def check_code_keyword_search(_, status_code):
    logger.info(world.search_keyword_status)
    assert world.search_keyword_status == int(status_code)
# endregion

# region list of services with short keyword
@step(r'Get list of services with keyword (\S+)')
def get_list_short_key(_, search_item):
    res = requests.get(f"{config.base_api_uri}/search/{search_item}")
    world.search_short_key_status = res.status_code


@step(r"third search must be (\d+)")
def check_code_list_search(_, status_code):
    logger.info(world.search_short_key_status)
    assert world.search_short_key_status == int(status_code)
# endregion


# region search services with title
@step(r'list of services with keyword (\S+)')
def get_search_keyword(_, search_item):
    res = requests.get(f"{config.base_api_uri}/search/{search_item}")
    world.search_short_status = res.status_code


@step(r"first code for search must be (\d+)")
def check_code_search(_, status_code):
    logger.info(world.search_short_status)
    assert world.search_short_status == int(status_code)
# endregion
