def get_table(file_name):
    #table = []
    
    #with open(file_name) as file:
    #   for line in file:
    #        row = line.split("\t")
    #       table.append(row)
    

    table_named = []

    with open(file_name) as file:
        for line in file:
            row = line.split("\t")
            columns_named = {
                "title" : row[0],
                "sales_amount" : row[1],
                "year" : row[2],
                "genre" : row[3],
                "publisher" : row[4]

            }
            table_named.append(columns_named)
    return table_named        

def count_games(file_name):
    #counter = 0
    #data = get_table(file_name)
    
    #for lini in data:
    #    counter =+ 1
    counter = len(get_table(file_name))
    return counter        
  

print(count_games("game_stats.txt"))

def decide(file_name, year):
    
    #if year in get_table(file_name)[2]:
     #   return True
    for row in get_table(file_name):
           if(int(row["year"] == year)):
                return True
    return False            
decide("game_stat.txt", 2000)    
    


def get_latest(file_name):
    
    year = 0 
    for row in get_table(file_name):
        if int(row["year"]) > year:
            year = int(row["year"])
            title = row["title"]
    
    return title
    #temp = 0
    #temp_name = " "            
    #with open(file_name) as file:
    #    for line in file:
    #        columns = line.split("\t")
    #        if int(columns[2]) > temp:
    #            temp = int(columns[2])
    #            temp_name = columns[0] 
    #return temp_name


def count_by_genre(file_name, genre):
    
    counter = 0
    for row in get_table(file_name):
        if row["genre"] == genre:
            counter += 1 

    return counter

def get_line_number_by_title(file_name, title):
    
    counter = 0
    for row in get_table(file_name):
        counter += 1

        if row["title"] == title:
            return counter
   
    raise ValueError


def sort_abc(file_name):
    pass


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass
