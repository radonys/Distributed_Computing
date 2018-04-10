from mrjob.job import MRJob
from mrjob.step import MRStep
import argparse

class MultiCategoryImages(MRJob):
      
      n = 3

      #Defines the way in which the mapper and reducer functions would be executed. Here, the MRSteps are executed from the first to last MRStep in the list.
      def steps(self):
            
            return [MRStep(mapper=self.mapper_get_images, reducer=self.reducer_sum_categories), MRStep(reducer=self.reducer_threshold)]

      #Mapper Function
      #Splitting the CSV files in words, then taking the image name and count as 1.
      def mapper_get_images(self, _, line):
       
            line = str(line)
            values = line.split(',')

            if values[0]!='ImageID':
                  yield(values[0], 1)

      #Reducer Function
      #Taking sum of occurence of each image
      def reducer_sum_categories(self, word, counts):
            
            yield None, (sum(counts), word)

      #Reducer Function 2
      #Prints only those images which belong to more n classes
      def reducer_threshold(self,_,image_count):

            temp = sorted(image_count)

            for i in range(0,len(temp)):
                  if temp[i][0]>self.n:
                        print temp[i][1], " ", temp[i][0]

if __name__ == '__main__':

      MultiCategoryImages.n = 5
      MultiCategoryImages.run()