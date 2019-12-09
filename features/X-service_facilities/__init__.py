from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call

# region assign specified facility to a service
@step(r'specify facility for service (\S+) with slug (\S+)')
def assign_facility_services_success(self, service_slug: str, facility_slug: str):
    call.delete_facility_service()
    res = requests.put(f"{config.base_api_uri}/services/{service_slug}/facilities/{facility_slug}")
    logger.info(res)
    world.facility_services_details_code = res.status_code


@step(r'return facility code must be (\d+)')
def check_code_facility_services(_, status_code):
    logger.info(world.facility_services_details_code)
    assert world.facility_services_details_code == int(status_code)
# endregion


# region Getting list of facilities assigned to a service
@step(r'Get list of facilities by service slug (\S+)')
def get_facility_services_list(_, service_slug):
    res = requests.get(f"{config.base_api_uri}/services/{service_slug}/facilities")
    world.service_facility_status = res.status_code


@step(r"return code in facility service must be (\d+)")
def check_code_facility_services(_, status_code):
    logger.info(world.service_facility_status)
    assert world.service_facility_status == int(status_code)
# endregion

# region Delete facility from a service
@step(r'Delete facility (\S+) with service slug (\S+)')
def delete_success_service_facility(self, facility_slug: str, service_slug):
    res = requests.delete(f"{config.base_api_uri}/services/{service_slug}/facilities/{facility_slug}")
    logger.info(res.status_code)
    world.service_facility_deleted = res.status_code


@step(r'result code for facility service deleted must be (\d+)')
def check_code_service_facility_deleted(_, status_code):
    logger.info(world.service_facility_deleted)
    assert world.service_facility_deleted == int(status_code)
# endregion
