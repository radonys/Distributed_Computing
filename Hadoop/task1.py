from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class ConfidenceScore(MRJob):

    list_item = ['car']
    
    #Defines the way in which the mapper and reducer functions would be executed. Here, the MRSteps are executed from the first to last MRStep in the list.
    def steps(self):
        return [MRStep(mapper=self.mapper_get_images, reducer=self.reducer_sum_categories), MRStep(reducer=self.reducer_threshold)]

    #Mapper Function
    #Splitting the CSV files in words, then taking the category with author and count as 1.
    def mapper_get_images(self, _, line):
       
        line = str(line)
        values = line.split(',')

        if values[0]!='ImageID':
           
            for word in self.list_items:

            	if str(word) in values[7].split(' '):

                	yield(values[6], 1)

    #Reducer Function
    #Taking sum of occurence of each author
    def reducer_sum_categories(self, word, counts):
            
        yield None, (sum(counts), word)

    #Reducer Function 2
    #Prints author with maximum images in the category
    def reducer_threshold(self,_,image_count,n=0):
            
        temp = max(image_count)
        print temp

if __name__ == '__main__':

   #The category can be changed here
   ConfidenceScore.list_items = ['car']
   ConfidenceScore.run()