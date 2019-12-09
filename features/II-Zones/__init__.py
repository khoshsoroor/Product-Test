from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call

# region Successful add zones
@step(r'adding zones for (\S+) with info')
def add_zones(self, city_slug: str):
    call.delete_zones()
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities/{city_slug}/zones", json=row)
        results.append(res.status_code)
    world.add_zones = results
    logger.info(world.add_zones)


@step(r'check code for zones must be (\d+)')
def check_result_add_zone(_, status_code):
    result = True
    for item in world.add_zones:
        result = result and item == int(status_code)
    assert result


@step(r'show zone detail with city_slug (\S+) and slug (\S+) must be')
def check_zones_added(self, city_slug, slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/zones/{slug}", headers={"Accept-Language": "en-US"})
    logger.info(res.json())
    result2 = res.json()
    logger.info(result2)
    assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion

# region Getting zones list
@step(r'Getting the list of zones from (\S+)')
def get_zones_list(_, city_slug: str):
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/zones")
    world.zones_list = res.json()
    logger.info(world.zones_list)
    world.zones_status = res.status_code


@step(r"zones get code must be (\d+)")
def check_res_code_zone(_, status_code):
    logger.info(world.zones_status)
    assert world.zones_status == int(status_code)
# endregion

# region show zones details from specific slug
@step(r'Getting the list of zones by zone_slug (\S+) and city (\S+)')
def get_zone_detail(_, slug: str, city_slug: str):
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/zones/{slug}", headers={"Accept-Language": "en-US"})
    world.list_zone_status = res.status_code


@step(r"detail of zones code must be (\d+)")
def check_detail_zone(_, status_code):
    logger.info(world.list_zone_status)
    assert world.list_zone_status == int(status_code)
# endregion

# region Unsuccessful Register zones with empty data
@step(r'add zone with invalid data for city (\S+)')
def add_empty_zone(self, city_slug: str):
    res = requests.post(f"{config.base_api_uri}/cities/{city_slug}/zones", json=tools.guess_types(self.hashes)[0])
    world.invalid = res.status_code
    logger.info(world.invalid)


@step(r'status code for zone with invalid data must be (\S+)')
def check_result_empty_zone(_, status_code):
    assert world.invalid == int(status_code)
# endregion

# region Successfully modified the zones
@step(r'modify zones row with city (\S+) and slug (\S+)')
def success_modify_zone(self, city_slug: str, slug: str):
    res = requests.put(f"{config.base_api_uri}/cities/{city_slug}/zones/{slug}", json=tools.guess_types(self.hashes)[0])
    world.su_modify_zone = res.status_code


@step(r'Modify code for zones must be (\d+)')
def check_modify_zone(_, status_code):
    logger.info(world.su_modify_zone)
    assert world.su_modify_zone == int(status_code)


@step(r'Modified zone row with city (\S+) and zone slug (\S+) must be')
def modified_zones_list(self, city_slug: str, slug: str):
    rows = tools.guess_types(self.hashes)
    logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/zones/{slug}", headers={"Accept-Language": "en-US"})
    result2 = res.json()
    logger.info(result2)
    # logger.info(tuple((key for key in rows[0] if rows[0][key] != result2[key])))
    assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion

# region Successfully Delete row in zone
@step(r'Delete zone row in (\S+) with slug (\S+)')
def success_delete_zone(self, city_slug: str, slug: str):
    res = requests.delete(f"{config.base_api_uri}/cities/{city_slug}/zones/{slug}")
    logger.info(res.status_code)
    world.zone_deleted = res.status_code


@step(r'Successfully deleted code for zone must be (\d+)')
def check_zone_code_deleted(_, status_code):
    logger.info(world.zone_deleted)
    assert world.zone_deleted == int(status_code)
# endregion

# region Check Unique in slug field zones
@step(r'Add zone with same city (\S+)')
def check_unique_zone(self, city_slug: str):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities/{city_slug}/zones", json=row)
        results.append(res.status_code)
    world.uni_zone = results
    logger.info(world.uni_zone)


@step(r'zone unique code should be (\d+)')
def check_result_unique_zone(_, status_code):
    result = True
    for item in world.uni_zone:
        if item == int(status_code):
            result = int(status_code)

    assert result == int(status_code)
# endregion

# region add new zone for data entry
@step(r'add zones for city (\S+) with')
def add_zone_data_entry(self, city_slug: str):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/cities/{city_slug}/zones", json=row)
        results.append(res.status_code)
    world.data_entry_zone = results
    logger.info(world.data_entry_zone)


@step(r'return code for added zone must be (\d+)')
def check_result_zone_data(_, status_code):
    result = True
    for item in world.data_entry_zone:
        result = result and item == int(status_code)
    assert result

# endregion
