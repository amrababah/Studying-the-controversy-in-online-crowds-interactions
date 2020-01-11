#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv



def buildRetweetGraph(sourceFile, outputFile):
    users = set()
    edges = {}
    
    c=0
    
    user = None
    otheruser = None
    
     
    try:
        reader = csv.reader(open("c:/datasets/"+ sourceFile +".csv", 'rU'), delimiter = ',' ,lineterminator='\n')
        for row in reader:
            if( not row ):
                continue
            else:
                try:
                    '''
                    row[0].isdigit() is to make sure that the line begin with tweet id
                    the line structure in the file as follow:
                               row[0] tweet.id_str , row[1] tweet.author.screen_name,
                               row[2] tweet.author.id, row[3] tweet.text
                    '''
                    if( row[0].isdigit()):
                        if ("RT @" in row[3]):
                            start = row[3].index("RT @") + len( "RT @" )
                            end = row[3].index( ":", start )
        #                   rint row[3][start:end], row[1]
                           
                            otheruser=row[3][start:end]
                            
                            c +=1
                            user=row[1]
                            users.add(user)
                            users.add(otheruser)
                            edges[(user,otheruser)]  = edges.get((user,otheruser), 0) + 1
                            print c
                except:
                    continue                        
                             
             
             
    finally:
        pass
    
    print("Found " + str(len(users)) + " users in " +  str(len(edges)) + " events.")
    
    # Write out GML now
    f = open("c:/Graphs/"+ outputFile +"Graph.gml", "w")
    f.write("graph\n[\n")
     
    for n in users:
        f.write("  node\n  [\n    id " + n + "\n    label \"" + n + "\"\n  ]\n")
     
    for (a,b) in edges:
        if(edges[(a,b)]>1):
            f.write("  edge\n  [\n    source " + a + "\n    target " + b + "\n    weight " + str(edges[(a,b)]) + "\n  ]\n")
     
    f.write("]\n")
     
     
    edges_for_csv = [[a,b, str(edges[(a,b)])] for (a,b) in edges if edges[(a,b)]>1]
     
    print "writing to {0}_tweets.csv"
    with open("c:/Graphs/" + outputFile + "Graph.csv", 'a') as f:
        writer = csv.writer(f, delimiter = ',', lineterminator='\n')
        writer.writerows(edges_for_csv)

buildRetweetGraph("beefbansall","beefbansall")