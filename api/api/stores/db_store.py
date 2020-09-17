from api.stores.base_store import BaseStore


class DbStore(BaseStore):
    """
    Just in case we want to add db access at some point.
    """

    @classmethod
    def get_foods(cls) -> list:
        return super().get_foods()

    @classmethod
    def get_nutrients(cls) -> list:
        return super().get_ingredients()
