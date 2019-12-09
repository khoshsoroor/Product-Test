from aloe import *
from aloe import tools
import requests
from .. import config, logger
from .. import call


# region Successful create specified categories
@step('Create specify category information:')
def add_category_success(self):
    call.delete_categories()
    results = list()
    for row in tools.guess_types(self.hashes):
        if "tags" in row:
            filed = row["tags"].split(",")
            row["tags"] = filed
            res = requests.post(f"{config.base_api_uri}/categories", json=row)
            results.append(res.status_code)
        else:
            res = requests.post(f"{config.base_api_uri}/categories", json=row)
            results.append(res.status_code)
    world.post_cat = results
    logger.info(world.post_cat)


@step(r'create category code must be (\d+)')
def check_result_added_category(_, status_code):
    result = True
    for item in world.post_cat:
        result = result and item == int(status_code)
    assert result


@step(r'category detail with slug (\S+) must be')
def check_categories_added(self, slug: str):
    rows = list()
    for row in tools.guess_types(self.hashes):
        filed = row["tags"].split(",")
        row["tags"] = filed
        rows.append(row)
        logger.info(rows)
    res = requests.get(f"{config.base_api_uri}/categories/{slug}", headers={"Accept-Language": "en-US", 'Content-type': 'application/json'})
    result2 = res.json()
    # logger.info(tuple((key for key in rows[0] if rows[0][key] != result2[key])))
    assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion

# region Getting category list
@step('Getting the list of categories')
def get_category_list(_):
    res = requests.get(f"{config.base_api_uri}/categories")
    world.cat_status = res.status_code


@step(r"categories code must be (\d+)")
def check_category_code_list(_, status_code):
    logger.info(world.cat_status)
    assert world.cat_status == int(status_code)
# endregion

# region show category details from specific slug
@step(r'Getting the list of category by slug (\S+)')
def get_category_detail(_, slug: str):
    res = requests.get(f"{config.base_api_uri}/categories/{slug}")
    world.cat_code_status = res.status_code


@step(r"detail of category code must be (\d+)")
def check_code_list_category(_, status_code):
    logger.info(world.cat_code_status)
    assert world.cat_code_status == int(status_code)
# endregion

# region Unsuccessful Register categories with empty data
@step('add category with invalid data')
def add_category_empty(self):
    res = requests.post(f"{config.base_api_uri}/categories", json=tools.guess_types(self.hashes)[0])
    world.empty_cat = res.status_code


@step(r'category code with invalid data must be (\d+)')
def check_invalid_category(_, status_code):
    assert world.empty_cat == int(status_code)
# endregion

# region Successfully modified the categories
@step(r'for update modify category row with slug (\S+)')
def update_category(self, slug: str):
    row = tools.guess_types(self.hashes)[0]
    if "tags" in row:
        filed = row["tags"].split(",")
        del row['tags']
        row.update({"tags": filed})
        res = requests.put(f"{config.base_api_uri}/categories/{slug}", json=row)
        world.stat_update_cat = res.status_code
    else:
        res = requests.put(f"{config.base_api_uri}/categories/{slug}", json=tools.guess_types(self.hashes)[0])
        world.stat_update_cat = res.status_code


@step(r'Modify code for categories must be (\d+)')
def check_category_code_updated(_, status_code):
    logger.info(world.stat_update_cat)
    assert world.stat_update_cat == int(status_code)


@step(r'check row in category with slug (\S+) must be')
def check_category_updated_list(self, slug: str):
    rows = tools.guess_types(self.hashes)
    if "tags" in rows:
        filed = rows["tags"].split(",")
        del rows['tags']
        rows.update({"tags": filed})
        res = requests.get(f"{config.base_api_uri}/categories/{slug}")
        result2 = res.json()
        # logger.info(tuple((key for key in rows[0] if rows[0][key] != result2[key])))
        assert all((rows[0][key] == result2[key] for key in rows[0]))
# endregion

# region Successfully Delete row in categories
@step(r'Delete category row with slug (\S+)')
def delete_category_success(self, slug: str):
    res = requests.delete(f"{config.base_api_uri}/categories/{slug}")
    logger.info(res.status_code)
    world.cat_deleted = res.status_code


@step(r'Successfully deleted code for category must be (\d+)')
def check_code_deleted(_, status_code):
    logger.info(world.cat_deleted)
    assert world.cat_deleted == int(status_code)
# endregion

# region Check Unique in slug field category
@step(r'Adding category with same slug categories')
def check_unique_category(self):
    results = list()
    for row in tools.guess_types(self.hashes):
        filed = row["tags"].split(",")
        row["tags"] = filed
        res = requests.post(f"{config.base_api_uri}/categories", json=row)
        results.append(res.status_code)
    world.uni_cat_stat = results
    logger.info(world.uni_cat_stat)


@step(r'categories unique code should be (\d+)')
def check_result_unique_category(_, status_code):
    result = True
    for item in world.uni_cat_stat:
        if item == int(status_code):
            result = int(status_code)

    assert result == int(status_code)
# endregion
