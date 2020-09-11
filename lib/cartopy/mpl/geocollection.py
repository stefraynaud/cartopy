# Copyright Cartopy Contributors
#
# This file is part of Cartopy and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
from matplotlib.collections import QuadMesh
import numpy as np


class GeoQuadMesh(QuadMesh):
    """
    A QuadMesh designed to help handle the case when the mesh is wrapped.

    """
    # No __init__ method here - most of the time a GeoQuadMesh will
    # come from GeoAxes.pcolormesh. These methods morph a QuadMesh by
    # fiddling with instance.__class__.

    def set_array(self, A):
        # raise right away if A is 2-dimensional.
        if A.ndim > 1:
            raise ValueError('Collections can only map rank 1 arrays. '
                             'You likely want to call with a flattened array '
                             'using collection.set_array(A.ravel()) instead.')

        # Only use the mask attribute if it is there.
        if hasattr(self, '_wrapped_mask'):
            # Update the pcolor data with the wrapped masked data
            self._wrapped_collection_fix.set_array(A[self._wrapped_mask])
            # If the input array was a masked array, keep that data masked
            if hasattr(A, 'mask'):
                A = np.ma.array(A, mask=self._wrapped_mask | A.mask)
            else:
                A = np.ma.array(A, mask=self._wrapped_mask)

        # Now that we have prepared the collection data, call on
        # through to the underlying implementation.
        super(QuadMesh, self).set_array(A)
