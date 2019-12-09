from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call

# region check odata filter for tags in categories
@step(r'check category tags that has (\S+)')
def check_tags_filter(_, filter_tags):
    res = requests.get(f"{config.base_api_uri}/categories?$filter=tags has '{filter_tags}'")
    world.tags_filter = res.status_code
    world.tags_filter_data = res.json()
    logger.info(world.tags_filter)
    logger.info(world.tags_filter_data['value'])


@step(r'return code status for tags must be (\d+)')
def check_result_status_tags(_, status_code):
    assert world.tags_filter == int(status_code)


@step(r'row in categories for tags must be')
def check_result_filter_tags(self):
    rows = list()
    for row in tools.guess_types(self.hashes):
        filed = row["tags"].split(",")
        row["tags"] = filed
        rows.append(row)
        logger.info(rows)
    result2 = world.tags_filter_data['value']
    logger.info(result2)
    logger.info(tuple((key for key in rows[0] if rows[0][key] != result2[0][key])))
    assert all((rows[0][key] == result2[0][key] for key in rows[0]))


# endregion


# region check odata filter for indexes in categories
@step(r'list categories that index is equal (\d+)')
def check_index_filters(_, filter_index):
    res = requests.get(f"{config.base_api_uri}/categories?$filter=index eq '{filter_index}'")
    world.index_filter = res.status_code
    world.index_filter_data = res.json()
    logger.info(world.index_filter)


@step(r'result status code for index must be (\d+)')
def check_result_status_index(_, status_code):
    assert world.index_filter == int(status_code)
# endregion

# region check odata filter for not equal in categories
@step(r'categories list that index is not equal (\d+)')
def check_not_equal_filters(_, not_eq_index):
    res = requests.get(f"{config.base_api_uri}/categories?$filter=index ne '{not_eq_index}'")
    world.not_equal_filter = res.status_code
    logger.info(world.not_equal_filter)


@step(r'status code for not equal must be (\d+)')
def check_result_status_index(_, status_code):
    assert world.not_equal_filter == int(status_code)
# endregion

# region check odata filter for greater than and less than in categories
@step(r'categories list that index is grater equal than (\d+) and is less equal than (\d+)')
def check_and_filters(_,index_eq,index_ne):
    res = requests.get(f"{config.base_api_uri}/categories?$filter=index ge {index_eq} and index le {index_ne}")
    world.and_filter = res.status_code
    logger.info(world.and_filter)


@step(r'check code for and equal must be (\d+)')
def check_result_and_index(_, status_code):
    assert world.and_filter == int(status_code)
# endregion

# region check odata filter for g or g not in categories
@step(r'categories list that index is grater equal than (\d+) or is less equal than (\d+)')
def check_or_filters(_, index_eq, index_ne):
    res = requests.get(f"{config.base_api_uri}/categories?$filter=index ge {index_eq} or index le {index_ne}")
    world.or_filter = res.status_code
    logger.info(world.or_filter)


@step(r'check code for or filter must be (\d+)')
def check_result_or_index(_, status_code):
    assert world.or_filter == int(status_code)
# endregion

# region check odata orderby index categories
@step(r'categories list orderby (\S+)')
def check_orderby_filters(_, orderby):
    res = requests.get(f"{config.base_api_uri}/categories?$orderby={orderby} asc")
    world.orderby_filter = res.status_code
    logger.info(world.orderby_filter)


@step(r'check code for orderby categories must be (\d+)')
def check_result_orderby_index(_, status_code):
    assert world.orderby_filter == int(status_code)
# endregion


# region check odata top count for categories
@step(r'categories list top (\d+) and orderby (\S+)')
def check_top_filters(_,top , orderby):
    res = requests.get(f"{config.base_api_uri}/categories?$top={top}&$orderby={orderby}")
    world.top_filter = res.status_code
    logger.info(world.top_filter)


@step(r'check code top count categories must be (\d+)')
def check_result_top_index(_, status_code):
    assert world.top_filter == int(status_code)
# endregion

# region check odata skip for categories
@step(r'categories list skip (\d+)')
def check_skip_filters(_, skip):
    res = requests.get(f"{config.base_api_uri}/categories?$skip={skip}")
    world.skip_filter = res.status_code
    logger.info(world.skip_filter)


@step(r'check code for list of categories by skip must be (\d+)')
def check_result_skip_index(_, status_code):
    assert world.skip_filter == int(status_code)
# endregion

# region check odata expand for categories
@step(r'categories list expand (\S+)')
def check_expand_filters(_, expand):
    res = requests.get(f"{config.base_api_uri}/categories?$expand={expand}")
    world.expand_filter = res.status_code
    logger.info(world.expand_filter)


@step(r'check code for expand categories must be (\d+)')
def check_result_expand_index(_, status_code):
    assert world.expand_filter == int(status_code)
# endregion

# region check odata select for categories
@step(r'categories list for select (\S+)')
def check_select_filters(_, select1):
    res = requests.get(f"{config.base_api_uri}/categories?$select={select1}")
    world.select_filter = res.status_code
    logger.info(world.select_filter)


@step(r'check code selected categories must be (\d+)')
def check_result_select_index(_, status_code):
    assert world.select_filter == int(status_code)
# endregion
