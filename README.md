# The framework for models of thermodynamic equilibrium systems
[![DOI](https://zenodo.org/badge/399795756.svg)](https://zenodo.org/badge/latestdoi/399795756)

Model-framework is a framework for chemical equilibrium models that utilizes a general derivation method capable of generating custom models for complex molecular systems, based on the simple, reversible reactions describing these systems. Some case studies illustrating the framework are described in doi: https://doi.org/10.1101/2021.11.18.469126 with details on the procedure in the accompanying Supplementary Material.

## Installation:
1) Download the package. E.g. using:  
   `git clone https://github.com/TUe-chemical-biology/model-framework.git`  
   or by downloading and extracting the zip-file from [zenodo](https://doi.org/10.5281/zenodo.5531622).
2) If not yet available, install the dependencies, e.g. using Anaconda Navigator or via the command prompt:  
   `pip install numpy scipy pandas matplotlib sympy openpyxl`

## Usage:
Elaborate instructions on how to generate your own models is provided in the Supplementary Material, section Procedure, of the [publication](https://doi.org/10.1101/2021.11.18.469126). Below is a short description how to quickly run the example case which uses the default values in the different scripts after downloading. The example corresponds to the second case described in the publication.

## Running the example model:
1) Go to the folder 'model-framework' that was created during installation.
2) Creating the model:  
   a) Open the file 'model_builder.py' in your favourite Python IDE and run it, or run it from the command prompt:  
      `python model_builder.py`  
   b) As a result of the previous step, a file 'output/example_model.py' has been generated. Move this file from the folder 'output' to the folder 'model' using your file explorer or from the command prompt:  
      `mv output/example_model.py model/`
3) Providing the experimental data  
   For the example system, the experimental data and the 'config.ini' file, defining the experimental conditions, are already placed in the folder 'input'.
4) Finally, open the file 'main.py' in your favourite Python IDE and run it, or run it from the command prompt:  
   `python main.py`
5) Inspect the console for the determined parameters estimates and the generated images in order to verify the fit accuracy. For this system, the determined values should be Kd2: 3.894E-4 and Alpha: 1.335E3. Note that small variations in the final decimal position are possible between runs. 
6) Congratulations! You have analysed your first model using the model framework!

## What's next?
Gain more insight into the capabilities of the framework by following along with one of the cases in the [publication](https://doi.org/10.1101/2021.11.18.469126) and the corresponding tutorials or start working on your own data right away by using the detailed procedure in the Supplementary Material. An overview of all analysis functions included in the model can be found [here](https://2022-model-framework.readthedocs.io/).

## License
Please see the file LICENSE for details about the "GNU GPL" license which covers this software and its associated data and documents.
