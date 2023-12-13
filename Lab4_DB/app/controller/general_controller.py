# general_controller.py
from abc import ABC
from typing import List, Dict, Any

from http import HTTPStatus
from flask import abort


class GeneralController(ABC):

    _service = None

    def find_all(self) -> List[object]:
        return list(map(lambda x: x.to_dict(), self._service.find_all()))

    def find_by_id(self, key: int) -> object:
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.to_dict()

    def create(self, obj: object) -> object:
        return self._service.create(obj).to_dict()

    def create_all(self, obj_list: List[object]) -> List[object]:
        return list(map(lambda x: x.to_dict(), self._service.create(obj_list)))

    def update(self, key: int, new_obj: object) -> None:
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(key, new_obj)

    def patch(self, key: int, value_dict: Dict[str, Any]) -> None:
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        for field_name, value in value_dict.items():
            self._service.patch(key, field_name, value)

    def delete(self, key: int) -> None:
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(key)

    def delete_all(self) -> None:
        self._service.delete_all()
