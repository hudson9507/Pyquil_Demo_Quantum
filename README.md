This is a small collection of python scripts utilizing the pyQuil library to create quantum circuits. It is suggested to use the Quantum Virtual Machine and Quil Compiler. First install python, pyQuil, and Docker, then use the following commands in seperate terminals.  
docker run --rm -it -p 5555:5555 rigetti/quilc -P -S  
docker run --rm -it -p 5000:5000 rigetti/qvm -S  
As of 11/7/2026, pyQuil 4 is the stable version, but pyQuil 5 will make the Quantum Virtual Machine and Quil Compiler depricated.  
https://pyquil-docs.rigetti.com/en/stable/getting_started.html
