from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call

# region city list is empty
@step(r'Get the list of all city and specify city (\S+)')
def get_not_found_city_list(_, city_slug):
    call.delete_cities()
    res = requests.get(f"{config.base_api_uri}/cities")
    world.city_not_found_list_status = res.status_code
    result2 = requests.get(f"{config.base_api_uri}/cities/{city_slug}")
    world.city_not_found_status = result2.status_code


@step(r"not found code for city must be (\d+)")
def check_not_found_city_list(_, status_code):
    logger.info(world.city_not_found_list_status)
    assert world.city_not_found_list_status and world.city_not_found_status == int(status_code)


# endregion


# region successful add cities
@step('Adding cities with data')
def add_cities(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities", json=row)
        results.append(res.status_code)
    world.cities = results
    logger.info(world.cities)


@step(r'Status code must be (\d+)')
def check_result_add_cities(_, status_code):
    result = True
    for item in world.cities:
        result = result and item == int(status_code)
    assert result


@step(r'Cities row with slug (\S+) must be')
def check_city_added(self, slug: str):
    rows = tools.guess_types(self.hashes)
    res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language": "en-US"})
    result2 = res.json()
    assert all(rows[0][key] == result2[key] for key in rows[0])


# endregion

# region Successfully modified the city
@step(r'modify city row with slug (\S+)')
def modify_city_successfully(self, slug: str):
    res = requests.put(f"{config.base_api_uri}/cities/{slug}", json=tools.guess_types(self.hashes)[0])
    world.modify = res.status_code


@step(r'Modified code must be (\d+)')
def check_modified_cities(_, status_code):
    logger.info(world.modify)
    assert world.modify == int(status_code)


@step(r'Modified cities row with slug (\S+) must be')
def modified_city_checklist(self, slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language": "en-US"})
    logger.info(res.json())
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))


# endregion

# region Unsuccessful add cities
@step('Add cities with empty data')
def add_cities_empty(self):
    res = requests.post(f"{config.base_api_uri}/cities", json=tools.guess_types(self.hashes)[0])
    world.added_empty = res.status_code


@step(r'Failure code must be (\d+)')
def check_cities_empty(_, status_code):
    assert world.added_empty == int(status_code)


# endregion

# region Get all City lists
@step(r'Getting the list of cities')
def get_city_list(_):
    res = requests.get(f"{config.base_api_uri}/cities")
    logger.info(res.text)
    world.city_list = res.json()
    logger.info("city list json", world.city_list)
    world.city_list_status = res.status_code


@step(r"Result code city must be (\d+)")
def check_city_list(_, status_code):
    logger.info(world.city_list_status)
    assert world.city_list_status == int(status_code)


@step('List must not be empty')
def check_len_city_list(_):
    assert len(world.city_list) > 0


# endregion

# region Successfully Delete row in cities
@step(r'Delete city row with slug (\S+)')
def deleted_city_success(self, slug: str):
    res = requests.delete(f"{config.base_api_uri}/cities/{slug}")
    logger.info(res.status_code)
    world.deleted = res.status_code


@step(r'Successfully disabled code must be (\d+)')
def check_deleted_city_code(_, status_code):
    logger.info(world.deleted)
    assert world.deleted == int(status_code)

# endregion

# region Check Unique in slug field city
@step('Add cities with same slug city')
def check_unique_cities(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities", json=row)
        results.append(res.status_code)
    world.unique = results
    logger.info(world.unique)


@step(r'after code should be (\d+)')
def check_code_city_unique(_, status_code):
    result = True
    for item in world.unique:
        if item == int(status_code):
            result = int(status_code)
    assert result == int(status_code)


# endregion

# region Delete wrong row in cities
@step(r'Delete city row with wrong slug (\S+)')
def delete_wrong_city(_, slug: str):
    res = requests.delete(f"{config.base_api_uri}/cities/{slug}")
    world.wrong = res.status_code


@step(r'wrong slug for disable code must be (\d+)')
def check_code_empty_deleted(_, status_code):
    logger.info(world.wrong)
    assert world.wrong == int(status_code)
# endregion
