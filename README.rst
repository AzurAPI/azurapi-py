Azur Lane API
=============

|Discord| |Downloads|

Repository for the Python library for the unofficial Azur Lane API

Example
-------

Importing module and instancing the api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

    from azurlane.azurapi import AzurAPI
    api = AzurAPI()

Getting ship information
~~~~~~~~~~~~~~~~~~~~~~~~

Type: Multilingual
^^^^^^^^^^^^^^^^^^

.. code:: py

    api.get_ship(ship="Enterprise")

or

.. code:: py

    api.get_ship_by_name(name="Enterprise")

Type: ID
^^^^^^^^

Works with string or integer. Do not use integer if the id is less than
100 since integers such as 077 is a syntax error in Python

.. code:: py

    api.get_ship(ship=115)
    api.get_ship(ship="115")

or

.. code:: py

    # sid stands for "ship id" since id is a reserved function name in Python
    api.get_ship_by_id(sid=115)
    api.get_ship_by_id(sid="115")

Maintainers
-----------

-  `August <https://github.com/auguwu>`__
-  `Spimy <https://github.com/Spimy>`__

In Collaboration With
---------------------

-  `synopNode() <https://www.youtube.com/channel/UCEw406qZnsdCEpRgVvCJzuQ>`__

Support Server
--------------

|image1|

Discord Link: https://discord.gg/aAEdys8

.. |Discord| image:: https://discordapp.com/api/guilds/648206344729526272/embed.png
   :target: https://discord.gg/aAEdys8
.. |image1| image:: https://discordapp.com/api/guilds/648206344729526272/widget.png?style=banner2
   :target: https://discord.gg/aAEdys8
.. |Downloads| image:: https://pepy.tech/badge/azurlane
   :target: https://pepy.tech/project/azurlane
