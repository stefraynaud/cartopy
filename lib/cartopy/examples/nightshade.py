"""
Nightshade feature
------------------

Draws a polygon where there is no sunlight for the given datetime.

"""
__tags__ = ['Lines and polygons']

import datetime
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature.nightshade import Nightshade


ax = plt.axes(projection=ccrs.PlateCarree())

date = datetime.datetime(1999, 12, 31, 12)

ax.set_title('Night time shading for {}'.format(date))
ax.stock_img()
ax.add_feature(Nightshade(date, alpha=0.2))
plt.show()