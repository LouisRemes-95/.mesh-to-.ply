# mesh_to_ply

Convert volumetric meshes (e.g. `.mesh`) to surface `.ply` files.

This tool reads a volumetric mesh using `meshio`, extracts the external surface, and writes it as a `.ply` mesh. The conversion accounts for **element region IDs**, allowing surfaces belonging to different regions to be handled consistently.

The module is designed as a small reusable step in a larger research workflow for CT-based mesh processing and simulation.

## Installation

This project uses **uv** for environment and dependency management.

### Option 1 — Clone the repository

```bash
git clone https://github.com/<username>/mesh_to_ply.git
cd mesh_to_ply
uv sync
```

### Option 2 — Install directly from GitHub

You can also install the tool directly into a project environment:

```bash
uv add git+https://github.com/<username>/mesh_to_ply.git
```

This makes the `mesh-to-ply` command available in the environment.

## Usage

Run the command line interface:

```bash
uv run mesh-to-ply input.mesh
```

Specify an output file:

```bash
uv run mesh-to-ply input.mesh -o output.ply
```

If no output path is provided, the `.ply` file is written next to the input mesh using the same name.

## Python Usage

The conversion function can also be used directly in Python:

```python
from pathlib import Path
from mesh_to_ply.convert import convert

convert(Path("input.mesh"), Path("output.ply"))
```

## Context

This module is intended to be used as one step in a larger processing pipeline:

```
CT scan → cleaning → smoothing → meshing → mesh_to_ply → simulation
```

Each step of the workflow is implemented as a separate module to keep the pipeline modular and reproducible.