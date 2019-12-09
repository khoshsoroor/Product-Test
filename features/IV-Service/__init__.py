from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call


# region  Successful Register new service
@step('Register a service with data:')
def add_service(self):
    call.delete_services()
    results = list()
    for row in tools.guess_types(self.hashes):
        logger.info(row)
        if "tags" in row:
            filed = row["tags"].split(",")
            row["tags"] = filed
            logger.info(row)
            res = requests.post(f"{config.base_api_uri}/services", json=row)
            results.append(res.status_code)
        else:
            res = requests.post(f"{config.base_api_uri}/services", json=row)
            results.append(res.status_code)
    world.post_srv = results
    logger.info(world.post_srv)


@step(r'Successfully register service code must be (\d+)')
def check_result_add_services(_, status_code):
    result = True
    for item in world.post_srv:
        result = result and item == int(status_code)
    assert result


@step(r'service detail with slug (\S+) must be')
def check_service_list_added(self, slug: str):
    table = tools.guess_types(self.hashes)
    check = list()
    for row in table:
        filed = row["tags"].split(",")
        row["tags"] = filed
        check.append(row)
        logger.info(check)
    res = requests.get(f"{config.base_api_uri}/services/{slug}")
    result2 = res.json()
    logger.info(result2)
    logger.info(check)
    logger.info(tuple((key for key in check[0] if check[0][key] != result2[key])))
    assert all((check[0][key] == result2[key] for key in check[0]))
# endregion

# region Getting Services list
@step('Getting the list of services')
def get_services_list(_):
    res = requests.get(f"{config.base_api_uri}/services")
    logger.info(res.text)
    world.services_list = res.json()
    logger.info(world.services_list)
    world.services_status = res.status_code


@step(r"Result code services must be (\d+)")
def check_result_code_list(_, status_code):
    logger.info(world.services_status)
    assert world.services_status == int(status_code)
# endregion

# region show Service details from specific slug
@step(r'Getting a services by (\S+)')
def get_service_detail(_, slug: str):
    res = requests.get(f"{config.base_api_uri}/services/{slug}")
    world.srv = res.status_code
    logger.info(world.srv)


@step(r"detail code services must be (\d+)")
def check_service_code_list(_, status_code):
    assert world.srv == int(status_code)
# endregion

# region Unsuccessful Register services with empty data
@step('add service with invalid data')
def add_empty_service(self):
    res = requests.post(f"{config.base_api_uri}/services", json=tools.guess_types(self.hashes)[0])
    world.empty_service = res.status_code
    logger.info(world.empty_service)


@step(r'status code for invalid data service must be (\d+)')
def check_invalid_result_service(_, status_code):
    assert world.empty_service == int(status_code)
# endregion

# region Successfully modified the services
@step(r'update service row with slug (\S+)')
def success_modify_services(self, slug: str):
    results = list()
    for row in tools.guess_types(self.hashes):
        if "tags" in row:
            filed = row["tags"].split(",")
            logger.info(filed)
            del row['tags']
            row.update({"tags": filed})
            res = requests.put(f"{config.base_api_uri}/services/{slug}", json=row)
            results.append(res.status_code)
        else:
            res = requests.put(f"{config.base_api_uri}/services/{slug}", json=row)
            results.append(res.status_code)
    world.put_srv = results


@step(r'result code for update must be (\d+)')
def check_modified_success_code(_, status_code):
    logger.info(world.put_srv)
    result = True
    for item in world.put_srv:
        result = result and item == int(status_code)
    assert result


@step(r'services row with slug (\S+) must be')
def check_services_modified(self, slug: str):
    table = tools.guess_types(self.hashes)
    chk = list()
    for row in table:
        filed = row["tags"].split(",")
        row['tags'] = filed
        chk.append(row)
    logger.info(chk)
    res = requests.get(f"{config.base_api_uri}/services/{slug}")
    result2 = res.json()
    logger.info(result2)
    # logger.info(tuple((k for k in chk[0] if chk[0][k] != result2[k])))
    assert all((chk[0][k] == result2[k] for k in chk[0]))
# endregion

# region Successfully Delete row in services
@step(r'Delete service row with slug (\S+)')
def successfully_deleted_service(self, slug: str):
    res = requests.delete(f"{config.base_api_uri}/services/{slug}")
    logger.info(res.status_code)
    world.service_deleted = res.status_code


@step(r'Successfully disabled code for service must be (\d+)')
def check_service_code_deleted(_, status_code):
    logger.info(world.service_deleted)
    assert world.service_deleted == int(status_code)
# endregion

# region Check Unique in slug field services
@step('Add services with same slug services')
def check_unique_service_list(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        res = requests.post(f"{config.base_api_uri}/services", json=row)
        results.append(res.status_code)
    world.uni_service = results
    logger.info(world.uni_service)


@step(r'services unique code should be (\d+)')
def check_result_uni_service(_, status_code):
    result = True
    for item in world.uni_service:
        if item == int(status_code):
            result = int(status_code)

    assert result == int(status_code)
# endregion
