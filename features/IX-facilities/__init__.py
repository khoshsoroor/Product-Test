from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call

# region Successfully add facilities
@step('add specify facilities')
def add_facilities(self):
    call.delete_facilities()
    results = list()
    for row in tools.guess_types(self.hashes):
        logger.info(row)
        res = requests.post(f"{config.base_api_uri}/facilities", json=row)
        results.append(res.status_code)
    world.post_facilities = results
    logger.info(world.post_facilities)


@step(r'return code facilities must be (\d+)')
def check_result_add_facilities(_, status_code):
    result = True
    for item in world.post_facilities:
        result = result and item == int(status_code)
    assert result


@step(r'facilities detail with slug (\S+) must be')
def check_facilities_added(self, facility_slug):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/facilities/{facility_slug}", headers={"Accept-Language": "en-US"})
    logger.info(res.json())
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion


# region Check Unique in slug facilities
@step(r'Add facility with same slug')
def check_unique_facility(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/facilities", json=row)
        results.append(res.status_code)
    world.unique_facility = results
    logger.info(world.unique_facility)


@step(r'facilities unique code must be (\d+)')
def check_result_unique_facility(_, status_code):
    result = True
    for item in world.unique_facility:
        if item == int(status_code):
            result = int(status_code)

    assert result == int(status_code)
# endregion


# region Return list of facilities
@step('Getting the list of facilities')
def get_list_facilities(_):
    res = requests.get(f"{config.base_api_uri}/facilities")
    world.facilities_status = res.status_code


@step(r"Result code facilities must be (\d+)")
def check_category_code_list(_, status_code):
    logger.info(world.facilities_status)
    assert world.facilities_status == int(status_code)
# endregion


# region show details of facilities
@step(r'the list of facilities by slug (\S+)')
def get_facilities_detail(_, facility_slug):
    res = requests.get(f"{config.base_api_uri}/facilities/{facility_slug}")
    world.check_facilities_detail = res.status_code


@step(r"detail code of facilities must be (\d+)")
def check_facilities_code_list(_, status_code):
    logger.info(world.check_facilities_detail)
    assert world.check_facilities_detail == int(status_code)
# endregion


# region Successfully update a facility information
@step(r'update facility row with slug (\S+)')
def update_facility(self, facility_slug: str):
    row = tools.guess_types(self.hashes)[0]
    logger.info(row)
    res = requests.put(f"{config.base_api_uri}/facilities/{facility_slug}", json=row)
    logger.info(res.text)
    world.put_facility = res.status_code
    logger.info(world.put_facility)


@step(r'return code for update facilities should be (\d+)')
def check_result_edit_facility(_, status_code):
    logger.info(world.put_facility)
    assert world.put_facility == int(status_code)


@step(r'facility row with slug (\S+) must be')
def check_updated_facilities(self, facility_slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/facilities/{facility_slug}")
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion


# region Successfully Delete row facilities
@step(r'Delete facilities row with slug (\S+)')
def delete_success_offices(self, facility_slug: str):
    res = requests.delete(f"{config.base_api_uri}/facilities/{facility_slug}")
    logger.info(res.status_code)
    world.facility_deleted = res.status_code


@step(r'code in delete method facilities must be (\d+)')
def check_code_facility_deleted(_, status_code):
    logger.info(world.facility_deleted)
    assert world.facility_deleted == int(status_code)
# endregion
