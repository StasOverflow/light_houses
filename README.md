# test-houses

Please write the implementation for the logic described below. Don't try to rush,
and don't try to polish your solution either. I'd prefer to see a good sane implementation,
just like you would do that if it was a real task for a real project.


### Logic

There is a set of Power Plants and a set of Households. Every Household can be
connected to any number of Power Plants. Power Plant feeds the Household with the
Electricity. The Household has Electricity if it's connected to one or more
Power Plants.

Each Power Plant is alive by default, but can be killed. The Power Plant which
is not Alive will not generate any Electricity.

Household can be connected to Household. The Household which has the Electricity
also passes it to all the connected Households.

The Power Plant can be repaired after killed.

### TODO
1. clone this project
2. install requirements `pip install -r requirements.txt`
3. write some logic in `world.py`
4. check yourself with ```pytest```
