from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call

# region Successfully assign a service to a category
@step(r'assign service (\S+) to category (\S+)')
def success_add_category_service(self, service_slug: str, category_slug: str):
    call.delete_cat_services()
    res = requests.put(f"{config.base_api_uri}/categories/{category_slug}/services/{service_slug}")
    world.su_modify_cat_srv = res.status_code


@step(r'return code for category services must be (\d+)')
def check_modified_category_service(_, status_code):
    logger.info(world.su_modify_cat_srv)
    assert world.su_modify_cat_srv == int(status_code)
# endregion

# region Return list of Services are assigned to a Category
@step(r'Get the list of services for category (\S+)')
def get_category_services_list(_, category_slug):
    res = requests.get(f"{config.base_api_uri}/categories/{category_slug}/services")
    world.cat_srv_status = res.status_code


@step(r"category service code must be (\d+)")
def code_category_service_list(_, status_code):
    logger.info(world.cat_srv_status)
    assert world.cat_srv_status == int(status_code)
# endregion


# region  Un-Assign a Service from a City
@step(r'Delete service (\S+) from category (\S+)')
def success_delete_category_service(self, service_slug: str, category_slug):
    res = requests.delete(f"{config.base_api_uri}/categories/{category_slug}/services/{service_slug}")
    logger.info(res.status_code)
    world.cat_srv_deleted = res.status_code


@step(r'Successfully return code for category services must be (\d+)')
def check_category_service_deleted(_, status_code):
    logger.info(world.cat_srv_deleted)
    assert world.cat_srv_deleted == int(status_code)
# endregion


# region add data entry for service to a category
@step(r'add below services to category (\S+)')
def add_data_for_category(self, category_slug: str):
    result = list()
    for row in tools.guess_types(self.hashes):
        link = row["service_slug"]
        res = requests.put(f"{config.base_api_uri}/categories/{category_slug}/services/{link}")
        logger.info(res.status_code)
        result.append(res.status_code)
    world.add_data_category_services = result
    logger.info(world.add_data_category_services)


@step(r'result code in data entry first category services must be (\d+)')
def check_data_entry_category_service(_, status_code):
    result = True
    for item in world.add_data_category_services:
        result = result and item == int(status_code)
    assert result
# endregion
