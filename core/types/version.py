from typing import TypedDict


_IVersion = TypedDict('_IVersion', {
    'version-number': int,
    'last-data-refresh-date': int,
    'hash': str
})


class IVersionTypes(TypedDict):
    ships: _IVersion
    equipments: _IVersion
