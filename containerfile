# 1. Use python 3.12.5 base image
FROM python:3.12.5

# 2. Clone the core dependency, the solvent-accessible-area-analyzer package, and install it

# 3. Set a new WORKDIR 

# 4. Install typer (dependency for sasa.py)

# 5. Move the data folder, python script and jupyter notebook into the container

# 6. Invoke an entrypoint command, typically bash
CMD ["bash"]

# 7. Install jupyterlab, expose the port it runs on (incoming connections from HOST, your computer)
# Run a container using this image that allows you to run the visualizing_sasa.ipynb
# notebook on the host (your local computers browser!)
# HINT: The command is a jupyter lab command
