from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call
import json
import geojson
from shapely.geometry import Point

# region  Successfully add offices
@step(r'add specify offices with city slug (\S+) office')
def add_offices(self, city_slug: str):
    call.delete_offices()
    row = tools.guess_types(self.hashes)[0]
    location = json.loads(geojson.dumps(Point(*map(float, row["location"].split(",")))))
    row['location'] = location
    logger.info(row)
    res = requests.post(f"{config.base_api_uri}/cities/{city_slug}/offices", json=row)
    logger.info(res.text)
    world.post_offices = res.status_code
    logger.info(world.post_offices)


@step(r'create offices code must be (\d+)')
def check_result_add_office(_, status_code):
    logger.info(world.post_offices)
    assert world.post_offices == int(status_code)


@step(r'office detail with slug (\S+) in city (\S+) must be')
def check_office_added(self, slug, city_slug: str):
    table = tools.guess_types(self.hashes)
    l = list()
    for row in table:
        location = json.loads(geojson.dumps(Point(*map(float, row["location"].split(",")))))
        row['location'] = location
        logger.info(row)
        l.append(row)
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/offices/{slug}")
    result2 = res.json()
    logger.info(result2)
    # logger.info(tuple((k for k in l[0] if l[0][k] != result2[k])))
    assert all((l[0][key] == result2[key] for key in l[0]))
# endregion


# region Return list of offices inside a city
@step(r'Getting the list of offices in city (\S+)')
def get_offices_list(_, city_slug):
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/offices")
    world.offices_status = res.status_code


@step(r"Result code offices must be (\d+)")
def check_offices_code_list(_, status_code):
    logger.info(world.offices_status)
    assert world.offices_status == int(status_code)
# endregion

# region return an office detail with a city
@step(r'Get detail of office (\S+) in city (\S+)')
def get_office_detail(_, office_slug: str, city_slug):
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/offices/{office_slug}")
    world.office_code_status = res.status_code


@step(r"detail code offices must be (\d+)")
def check_code_list_office(_, status_code):
    logger.info(world.office_code_status)
    assert world.office_code_status == int(status_code)
# endregion

# region Successfully edit an office information
@step(r'edit office row in city (\S+) with slug (\S+)')
def edit_offices(self, city_slug: str, office_slug):
    row = tools.guess_types(self.hashes)[0]
    location = json.loads(geojson.dumps(Point(*map(float, row["location"].split(",")))))
    row['location'] = location
    logger.info(row)
    res = requests.put(f"{config.base_api_uri}/cities/{city_slug}/offices/{office_slug}", json=row)
    logger.info(res.text)
    world.put_offices = res.status_code
    logger.info(world.put_offices)


@step(r'return code for edit office must be (\d+)')
def check_result_edit_offices(_, status_code):
    logger.info(world.put_offices)
    assert world.put_offices == int(status_code)


@step(r'office detail with city_slug (\S+) and slug (\S+) must be')
def check_offices_edited(self, city_slug, slug: str):
    table = tools.guess_types(self.hashes)
    l = list()
    for row in table:
        location = json.loads(geojson.dumps(Point(*map(float, row["location"].split(",")))))
        row['location'] = location
        logger.info(row)
        l.append(row)
    res = requests.get(f"{config.base_api_uri}/cities/{city_slug}/offices/{slug}")
    result2 = res.json()
    logger.info(result2)
    logger.info(tuple((k for k in l[0] if l[0][k] != result2[k])))
    assert all((l[0][key] == result2[key] for key in l[0]))
# endregion

# region Successfully Delete an office from a city
@step(r'Delete office row in city (\S+) and office (\S+)')
def delete_success_offices(self, city_slug: str, office_slug):
    res = requests.delete(f"{config.base_api_uri}/cities/{city_slug}/offices/{office_slug}")
    logger.info(res.status_code)
    world.office_deleted = res.status_code


@step(r'Successfully deleted code offices must be (\d+)')
def check_city_offices_code_deleted(_, status_code):
    logger.info(world.office_deleted)
    assert world.office_deleted == int(status_code)
# endregion
