import numpy as np
import cellpose.models as m

# Force caching
m.CellposeModel("cyto")
model = m.CellposeModel("cyto2")

# Force pre-compilation of numba functions
arr = np.random.normal(size=(128, 128))
model.eval(arr, diameter=20)
