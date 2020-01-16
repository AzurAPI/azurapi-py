# Azur Lane API
[![Discord](https://discordapp.com/api/guilds/648206344729526272/embed.png)](https://discord.gg/aAEdys8)

Repository for the Python library for the unofficial Azur Lane API

## Example

### Importing module and instancing the api
```py
from azurapi import AzurApi
api = AzurApi()
```

### Getting ship information

#### Type: Multilingual
```py
api.get_ship(ship="Enterprise")
```
or
```py
api.get_ship_by_name(name="Enterprise")
```

#### Type: ID
Works with string or integer. Do not use integer if the id is less than 100 since integers such as 077 is a syntax error in Python
```py
api.get_ship(ship=115)
api.get_ship(ship="115")
```
or
```py
# sid stands for "ship id" since id is a reserved function name in Python
api.get_ship_by_id(sid=115)
api.get_ship_by_id(sid="115")
```

## Maintainers
- [August](https://github.com/auguwu)
- [Spimy](https://github.com/Spimy)

## In Collaboration With
- [synopNode()](https://www.youtube.com/channel/UCEw406qZnsdCEpRgVvCJzuQ)

## Support Server

[![](https://discordapp.com/api/guilds/648206344729526272/widget.png?style=banner2)](https://discord.gg/aAEdys8)

Discord Link: https://discord.gg/aAEdys8
