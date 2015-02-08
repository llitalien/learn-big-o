import random

class DifferentSortingAlgorithms:

    m_MergeSortReadInstructions = 0
    m_MergeSortInsertInstructions = 0

    def generate_array(self, size):
        array = random.sample(xrange(1,size*2), size)
        return array

    def naiveSort(self, array):
        nb_read_instructions = 0
        nb_substitutions = 0

        # First pass over the entire array
        for x in range(len(array)-1,0,-1):
            # Pass over the non sorted values
            for t in range(x):
                if array[t] > array[t+1]:
                    temp = array[t]
                    # Swap
                    array[t] = array[t+1]
                    array[t+1] = temp
                    nb_substitutions += 1
                # On lit deux valeurs a chaque fois
                nb_read_instructions += 2 

        print "Read Instructions required to naive sort array -> " + str(nb_read_instructions)
        print "Swap Instructions required to naive sort array -> " + str(nb_substitutions)
        print(array)

    def insertSort(self, array):

        nb_read_instructions = 0
        nb_inserts = 0

        # First pass over the entire array from 1 to the length
        for i in range(1,len(array)):
            # Save current
            current = array[i]
            nb_read_instructions += 1
            pos = i

            # Assume anything below index has been sorted
            while pos > 0 and array[pos-1] > current:
                # Insert
                array[pos] = array[pos-1]
                pos -= 1
                nb_read_instructions += 1
                nb_inserts += 1

            array[pos] = current
        
        print "Read Instructions required to insert sort array -> " + str(nb_read_instructions)
        print "Insert Instructions required to insert sort array -> " + str(nb_inserts)
        print(array)

    def mergeSort(self, array):

        if len(array) > 1:
            mid = len(array)//2
            lefthalf = array[:mid]
            righthalf = array[mid:]
            self.m_MergeSortReadInstructions +=2
            self.m_MergeSortInsertInstructions += 3
               
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    array[k]=lefthalf[i]
                    i=i+1
                    self.m_MergeSortReadInstructions += 2
                    self.m_MergeSortInsertInstructions += 1
                else:
                    array[k]=righthalf[j]
                    j=j+1
                    self.m_MergeSortReadInstructions += 1
                    self.m_MergeSortInsertInstructions += 1
                    k=k+1

            while i<len(lefthalf):
                array[k]=lefthalf[i]
                self.m_MergeSortReadInstructions += 1
                self.m_MergeSortInsertInstructions += 1
                i=i+1
                k=k+1

            while j<len(righthalf):
                array[k]=righthalf[j]
                j=j+1
                k=k+1
                self.m_MergeSortReadInstructions += 1
	    
      

if __name__ == "__main__":

    sorting_app = DifferentSortingAlgorithms();

    array = sorting_app.generate_array(50)
    print(array)
    
    # Average / Random case
    print "Average (random) case!"
    sorting_app.naiveSort(list(array))
    sorting_app.insertSort(list(array))
    sorting_app.mergeSort(list(array))

    # Alright, let's see worst case
    print "Worst case run!"
    array_worst = list(array)
    array_worst.sort()
    array_worst.reverse()

    sorting_app.m_MergeSortReadInstructions = 0
    sorting_app.m_MergeSortInsertInstructions = 0

    #sorting_app.naiveSort(list(array_worst))
    #sorting_app.insertSort(list(array_worst))
    sorting_app.mergeSort(list(array_worst))

    print "Read Instructions required to MergeSort array -> " + str(sorting_app.m_MergeSortReadInstructions)
    print "Insert Instructions required to MergeSort array -> " + str(sorting_app.m_MergeSortInsertInstructions)
    
    sorting_app.m_MergeSortReadInstructions = 0
    sorting_app.m_MergeSortInsertInstructions = 0

   # Alright, let's see best case
    print "Best case run!"
    array_best = list(array)
    array_best.sort()

    #sorting_app.naiveSort(list(array_best))
    #sorting_app.insertSort(list(array_best))
    sorting_app.mergeSort(list(array_best))

    print "Read Instructions required to MergeSort array -> " + str(sorting_app.m_MergeSortReadInstructions)
    print "Insert Instructions required to MergeSort array -> " + str(sorting_app.m_MergeSortInsertInstructions)

