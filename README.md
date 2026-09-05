# 💻 CHEM 281 Lab: Containerization for Reproducibility

## 🧪 Goal

The goal of this lab is to:

1. Familiarize yourself with **containers and containerfiles**.
2. Learn how to use **container commands and ports**. 
3. Practice using the **data and files provided to work inside a container**.

---

## 🗂️ Provided

- An empty `container` file that you will set up.
- A CLI based python application to calculate solvent accessible surface area (SASA).
- A jupyter notebook that can calculate and visualize the SASA.

---

## 💻 Setup
```bash
podman build -t lab2 . # Creates the image using containerfile
podman run --rm -it lab2 # Runs the container from the image

# --rm removes the container once you exist 
# -it runs the container interactively so you can enter inside
```

Inside the container you will start with nothing!

## ✅ Tasks

You are a computational chemist who has recently created a module to analyze the solvent accessible surface area in python using open-source tools. You want to publish this and make it easy for others to run calculations without having to worry about dependencies or requirements. To do this you plan to use docker to precisely define an image which others can use as a container to run their calculations and analyses.

### Investigate the Solvent-Accessible-Area-Analyzer repo
This is the repo that contains the `sasa_viz` python library. You should clone it and install it using the instructions provided in the README.md. When you try to run `test_script.py` you'll notice that it is currently broken. Instead of trying to fix it, we will use the last working commit `19efc53b8df7e09e10831901c07b115f381c21ef` to install.

```
git checkout 19efc53b8df7e09e10831901c07b115f381c21ef
pip install -e .
```

Verify that the `test_script.py` works.

### Update the containerfile to support running the python app and notebook!
The python app and notebook both depend on the `sasa_viz` python library. For the container to run the app and notebook we would need to install the working version of the `sasa_viz` library and any dependencies. Follow the steps in the containerfile to set up an image that can support running the `sasa.py` app and `visualizing_sasa.ipynb` from a container.

```
# Running the app
python3 sasa.py --help

# Running jupyter lab to run the notebook
jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root
```

### Extra time
As we have currently designed the container, we need to update the data folder and re-build the container image if we or another user want to add new local PDBs. There is a better way to do this! Investigate volume mounting (bind mounts) and see how you can update the image and container run command to avoid adding a frozen copy of the data directory.
