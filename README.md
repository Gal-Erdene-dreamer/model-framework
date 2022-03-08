# The framework for models of thermodynamic equilibrium systems
[![DOI](https://zenodo.org/badge/399795756.svg)](https://zenodo.org/badge/latestdoi/399795756)

Model-framework is a framework for chemical equilibrium models that utilizes a
general derivation method capable of generating custom models for complex
molecular systems, based on the simple, reversible reactions describing
these systems. Some case studies illustrating the framework are described in
doi: https://doi.org/10.1101/2021.11.18.469126 with details on the procedure
in the accompanying Supplementary Material.


INSTALLATION:
1) Download the package. E.g. using:
   git clone https://github.com/TUe-chemical-biology/model-framework.git
   or by downloading and extracting the zip-file from 10.5281/zenodo.5531622
2) If not yet available, install the dependencies, e.g. using Anaconda
   Navigator or via the command prompt:
   pip install numpy scipy pandas matplotlib sympy openpyxl

USAGE:
Elaborate description of the usage to generate your own models is
provided in the Supplementary Material, section Procedure, of
https://doi.org/10.1101/2021.11.18.469126. Below is a short description
how to run a first example case.

USAGE TO RUN FIRST EXAMPLE:
1) Go to the folder 'model-framework' that was created during installation.
2) Creating the model:
   a) Open the file 'model_builder.py' in your favourite Python IDE and
      run it, or run it from the command prompt:
      python model_builder.py
   b) As a result of the previous step, a file output/example_name.py has been
      generated. Move this file from the folder 'output' to the folder 'model'.
      E.g. from the command prompt:
      mv output/example_model.py model/
---- Stap 3 moet denk ik weggelaten en zorgen dat er al goede config.ini staat.
3) Preparing config for experimental data:
   a) Open the file 'config_generator.py' in your favourite Python IDE and
      run it, or run it from the command prompt:
      python config_generator.py
   b) As a result of the previous step, a file output/config.ini has been
      generated. Move this file from the folder 'output' to the folder 'input'.
      E.g. from the command prompt:
      mv output/config.ini input/
4) Open the file 'main.py' in your favourite Python IDE and run it,
   or run it from the command prompt:
   python main.py

...



Please see the file LICENSE for details about the "GNU GPL"
license which covers this software and its associated data and
documents.
