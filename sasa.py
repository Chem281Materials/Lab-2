from pathlib import Path
from typing import Annotated, Optional
import typer
import sasa_viz as sv

app = typer.Typer(
    name="sasa-cli",
    help="Compute SASA and map to atomic B-factors using sasa_viz.",
    add_completion=False,
)

@app.command()
def analyze(
    target: Annotated[
        str, 
        typer.Argument(
            help="PDB ID (e.g. '1CRN') or a direct path to a local PDB file (e.g. 'data/2DAN.pdb')."
        )
    ],
    output_dir: Annotated[
        Path, 
        typer.Option(
            "--output-dir", "-o", 
            help="Directory to save downloaded PDB files."
        )
    ] = Path("data"),
) -> None:
    """Analyze Solvent Accessible Surface Area (SASA) from a PDB ID or file."""
    path_candidate = Path(target)

    if path_candidate.is_file():
        # Input is an existing local file
        filepath = str(path_candidate)
        structure_id = path_candidate.stem
        typer.echo(f"Loading local file: {filepath}")
    else:
        # Input is assumed to be a PDB ID to fetch online
        structure_id = target.upper()
        typer.echo(f"Fetching PDB '{structure_id}' into '{output_dir}'...")
        filepath = sv.fetch_pdb(structure_id, output_dir=str(output_dir))

    # Load structure and compute SASA
    structure = sv.load_structure(filepath, structure_id=structure_id)
    analyzed_struct, total_area = sv.analyze_sasa(structure, filepath)

    typer.secho(
        f"Total SASA for {structure_id}: {total_area:.2f} Å²", 
        fg=typer.colors.GREEN, 
        bold=True
    )

if __name__ == "__main__":
    app()