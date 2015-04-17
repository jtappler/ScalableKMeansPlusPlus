version=0.1

pyproject_$(version).tgz:       function.tmp Data.tmp
        tar czf pyproject_$(version).tgz project
        @echo "BUILD COMPLETED"

functions.tmp:      ScalableKMeansPlusPlus/InitialCode.py
        python ScalableKMeansPlusPlus/InitialCode.py
        @touch functions.tmp

third.tmp:      ScalableKMeansPlusPlus/DataSimulation.py
        python ScalableKMeansPlusPlus/DataSimulation.py
        @touch Data.tmp

clean:
        @rm -f *.tmp
        @rm -f *.tgz
        @echo "cleaned up"