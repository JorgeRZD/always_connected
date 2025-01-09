# always_connected
Random mouse and keyboard inputs

def pretend_function(duration, leaving=False, leaving_time=19)

The argument 'duration' is the amount of minutes that the script will run. Each minute, a set of randomized mouse movements and key pushes will be executed. The key pushes will be generated based on a random line picked from the file sample.txt, which must exist in the same location as the executable.

Arguments 'leaving' and 'leaving_time' are optional and should always be declared together. 'leaving' is a boolean argument which defines if the shutdown subscript should be executed. 'leaving time' is the hour on which the leaving subscript will run.

Whenever 'leaving' is true, if the hour of the system clock is equal or later than the one specified in the function, the leaving subscript will be executed, turning down the system.
