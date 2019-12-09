# from aloe import *
# from aloe import tools
# import requests
# from .. import config, logger
# from .. import call
#
# # region successful add cities
# @step('Adding cities with data')
# def add_cities(self):
#     results = list()
#     for row in tools.guess_types(self.hashes):
#         res = requests.post(f"{config.base_api_uri}/cities", json=row)
#         results.append(res.status_code)
#     world.cities = results
#     logger.info(world.cities)
#
#
# @step(r'Status code must be (\d+)')
# def check_result_add_cities(_, status_code):
#     result = True
#     for item in world.cities:
#         result = result and item == int(status_code)
#     assert result
#
#
# @step(r'Cities row with slug (\S+) must be')
# def check_city_added(self, slug: str):
#     rows = tools.guess_types(self.hashes)
#     res = requests.get(f"{config.base_api_uri}/cities/{slug}", headers={"Accept-Language": "en-US"})
#     result2 = res.json()
#     assert all(rows[0][key] == result2[key] for key in rows[0])
#
#
# # endregion
