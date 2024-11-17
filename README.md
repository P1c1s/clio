```mermaid

classDiagram
    direction LR
    core --|> libraries
    core --|> components
    core --|> modules
    class core{
        the heart of clio
    }
    class libraries{
        os
        sys
    }

    class components{
        c
    }
    class modules{
        c
    }
```


## Core
The core is the main file

## Libraries 
Sys and Os

## Componets
Coponents are (python file) ...

## Modules
The modules are components (python file) that the core can use. 
in order for the core to correctly load the modules they must be in the appropriate folder (modules)
Anyway each module can work standalone. 
