import random

class DifferentSortingAlgorithms:

    def __init__(self):
        self.array = []

    def generate_array(self, size):
        self.array = random.sample(xrange(1,size*2), size)
        print(self.array)

    def naiveSort(self):
        nb_read_instructions = 0
        nb_substitutions = 0
        index = 0
        current = 0
        resulting_array = []

        # First pass over the entire array
        for x in range(len(self.array)-1,0,-1):
            # Pass over the non sorted values
            for t in range(x):
                if self.array[t] > self.array[t+1]:
                    temp = self.array[t]
                    # Swap
                    self.array[t] = self.array[t+1]
                    self.array[t+1] = temp
                    nb_substitutions += 1
                # On lit deux valeurs a chaque fois
                nb_read_instructions += 2 

        print "Read Instructions required to sort array -> " + str(nb_read_instructions)
        print "Swap Instructions required to sort array -> " + str(nb_substitutions)
        print(self.array)

if __name__ == "__main__":

    sorting_app = DifferentSortingAlgorithms();

    sorting_app.generate_array(50)
    sorting_app.naiveSort()
