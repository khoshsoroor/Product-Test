from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call


# region Successfully add the city_services
@step(r'add city services for city (\S+) and service (\S+)')
def add_city_services_success(self, city_slug: str, service_slug: str):
    call.delete_city_services()
    res = requests.put(f"{config.base_api_uri}/cities/{city_slug}/services/{service_slug}/details", json=tools.guess_types(self.hashes)[0])
    world.city_services_details_code = res.status_code


@step(r'result code for city services must be (\d+)')
def check_success_code_modified_city_services(_, status_code):
    logger.info(world.city_services_details_code)
    assert world.city_services_details_code == int(status_code)


@step(r'Modified city services with city (\S+) and service (\S+) must be')
def modified_city_services(self, city_slug: str, services_slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/services/{services_slug}/details", headers={"Accept-Language": "en-US"})
    logger.info(res.json())
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion

# region Getting city_services all list
@step(r'Getting the list of services for city (\S+)')
def get_city_services_list(_, city_slug):
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/services")
    world.cs_status = res.status_code


@step(r"return city_services code must be (\d+)")
def check_code_city_services(_, status_code):
    logger.info(world.cs_status)
    assert world.cs_status == int(status_code)
# endregion

# region show city_services details from specific city
@step(r'Get the list of service (\S+) by slug (\S+)')
def get_city_service_detail(_, service_slug: str, city_slug: str):
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/services/{service_slug}/details")
    world.list_cs_status = res.status_code


@step(r"detail of city_services code must be (\d+)")
def check_detail_city_services_list(_, status_code):
    logger.info(world.list_cs_status)
    assert world.list_cs_status == int(status_code)
# endregion


# region Successfully Delete row in city_services
@step(r'Delete city_services row with slug (\S+) and service (\S+)')
def delete_city_service(self, city_slug: str, service_slug):
    res = requests.delete(f"{config.base_api_uri}/cities/{city_slug}/services/{service_slug}/details")
    logger.info(res.status_code)
    world.city_services_deleted = res.status_code


@step(r'Successfully deleted code for city_services must be (\d+)')
def check_city_service_code_deleted(_, status_code):
    logger.info(world.city_services_deleted)
    assert world.city_services_deleted == int(status_code)
# endregion

# region data entry for city_services
@step(r'adding data city services for city (\S+) and service (\S+)')
def add_data_city_services(self, city_slug: str, service_slug: str):
    res = requests.put(f"{config.base_api_uri}/cities/{city_slug}/services/{service_slug}/details", json=tools.guess_types(self.hashes)[0])
    world.city_services_data = res.status_code


@step(r'code for data city services must be (\d+)')
def check_code_data_city_services(_, status_code):
    logger.info(world.city_services_data)
    assert world.city_services_data == int(status_code)
# endregion
