from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class ConfidenceScore(MRJob):
      
      threshold = 0.5
      #Defines the way in which the mapper and reducer functions would be executed. Here, the MRSteps are executed from the first to last MRStep in the list.
      def steps(self):
            
            return [MRStep(mapper=self.mapper_get_images, reducer=self.reducer_sum_categories), MRStep(reducer=self.reducer_threshold)]

      #Mapper Function
      #Splitting the CSV files in words, then taking the class name and count as 1. Only Images with confidence score above 0.5 are considered.
      def mapper_get_images(self, _, line):
       
            line = str(line)
            values = line.split(',')

            if values[3]>self.threshold and values[0]!='ImageID':
                yield(values[2], 1)


      #Reducer Function
      #Taking sum of images of each class
      def reducer_sum_categories(self, word, counts):
            
            yield None, (sum(counts), word)

      #Reducer Function 2
      #Prints only those classes which have atleast 1 image above 0.5 confidence score.
      def reducer_threshold(self,_,image_count):
            
            temp = sorted(image_count)

            for i in range(0,len(temp)):
                  if temp[i][0]>0:
                        print temp[i][1], " ", temp[i][0]

if __name__ == '__main__':

   ConfidenceScore.threshold = 0.5
   ConfidenceScore.run()