from pathlib import Path
import meshio
import numpy as np

def convert(in_path, out_path: Path, data_label: str = None) -> None:
    """ 
    Convert a meshio mesh file (used for .mesh) to .obj
    Intended for a tetrahedral mesh with cell data
    
    Inputs
    ------
    in_path:
        Input mesh path
    out_path:
        Output .obj path
    """

    mesh = meshio.read(in_path)

    faces = mesh.cells_dict['tetra'][:, [[0,1,2],[0,3,1],[1,3,2],[0,2,3]]].reshape(-1,3)

    _, inverse, counts = np.unique(np.sort(faces), axis = 0, return_inverse = True, return_counts = True)
    is_boundary_face = counts[inverse] == 1

    boundary_faces = faces[is_boundary_face, :]

    key = next(iter(mesh.cell_data), None)
    if key is not None:
        data_label = key if data_label is None else data_label

        data = np.tile(mesh.cell_data_dict[data_label]['tetra'][:,None], (1, 4))

    meshio.write(out_path, mesh, file_format="obj")