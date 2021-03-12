#!/usr/bin/env python
# coding: utf-8

# In[7]:


class MovieNode:

    def __init__(self, movieName, relDate):
        self.movieName = movieName
        self.relDate = relDate
        self.next = None
        return
class NetflixMovieList:
    def __init__(self):
        self.head = None
    def addMovie(self, movieName, relDate):
        new = MovieNode(movieName, relDate)
        if self.head == None:
            self.head = new
            return
        new.next = self.head
        self.head = new
        return
    def displayMovies(self):
        if self.head == None:
            print("No movies to show right now")
            return
        temp = self.head
        while(temp != None):
            print(temp.movieName, temp.relDate, '->', end = "")
            temp = temp.next
        print('None')
        return
    def DeleteMovie(self):
        if self.head == None:
            print("There are no movies currently")
            return
        temp = self.head
        while(temp != None):
            temp1 = temp.next
            if(temp1.relDate < temp.relDate):
                temp.next = temp1.next
            else:
                temp= temp.next
        return
            
            

movie_list = NetflixMovieList()
movie_list.addMovie('Iron Man', '12-06-2011')
movie_list.addMovie('Thor', '15-07-2012')
movie_list.displayMovies()


# In[ ]:




