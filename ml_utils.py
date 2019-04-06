import csv
import datetime 
#def ex


def extractData(record):
    """ This function converts entries of ratings.csv into key,value pair of the following format
    (movieID, rating)
    Args:
        record (str): A row of CSV file, with four columns separated by comma
    Returns:
        The return value is a tuple (movieID, genre)
    """
    try:

        videoID, trending_date, category_id, category,publish_time,views,likes, dislikes,comment_count, ratings_disabled,video_error_or_removed,country = record.split(",")
        
        videoID_counry = videoID + "$" + country
        like = float(likes)
        dislike = float(dislikes)

        year,date,month = [ int(x) for x in trending_date.split(".")]
        year += 2000
        trending_date = datetime.date(year,month,date)

    #return ( videoID_counry, [likes, dislikes,trending_date,category] )
        return ( videoID_counry, [like, dislike,trending_date,category] )
    except:
        return (videoID_counry, [ 0, 0, datetime.date(1900,1,1) ,"" ] )
    
def sort_and_calculate( inputs ):
    try:
        # v_id_country = groups[0]

        # data_list = groups[1].tolist()

        # output=()
        # input_bag = sorted(inputs, key=lambda x: x[2], reverse=False)
        # loc0 = input_bag[0]
        # for loc in input_bag[1:]:
        #     output.append((loc0[2],loc[2]))
        #     loc0 = loc
        v_id_country = inputs[0]
        if len(inputs[1]) < 2:
            return(v_id_country, 0, inputs[1][0][3] )
    
        else:
            sorted_list = sorted( inputs[1], key = lambda x: x[2] )    
            temp = []
            for i in sorted_list[:2]:
                temp.append( i[1] - i[0] )

            growth_value = temp[1] - temp[0] 

            return (v_id_country, growth_value, inputs[1][0][3])


    except:
        return ()

def add_country( inputs ):
    video_id_country, growth_value, category  = inputs[:]
    
    video_id, country = video_id_country.split("$")

    return (video_id, growth_value, category, country)