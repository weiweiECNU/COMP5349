from pyspark import SparkContext
from ml_utils import *
import argparse

if __name__ == "__main__":
    sc = SparkContext(appName="Controversial Trending Videos Identification")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='~/comp5349/assignment')
    parser.add_argument("--output", help="the output path", 
                        default='dislike_output') 
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output

    videos = sc.textFile(input_path + "AllVideos_short.csv")
    #videos = sc.textFile("AllVideos_short.csv")
    videoslikes = videos.map(extractData)#.collect()
    #a = videoslikes.map(list)
    # data = sc.parallelize(videoslikes)

    grouplist = videoslikes.groupByKey().mapValues(list)
    videoGrowth = grouplist.map(sort_and_calculate)
    videoGrowth_all = videoGrowth.map( add_country )
    top10 = videoGrowth_all.top(10, key=lambda x: x[1])
    top = sc.parallelize(top10)

    #top.saveAsTextFile(output_path)
    top.saveAsTextFile("output")


    #videosGroup = videoslikes.groupByKey().map( sort_and_calculate )
    #videosGroup.foreach(print)
    
    #top10.foreach(print)
