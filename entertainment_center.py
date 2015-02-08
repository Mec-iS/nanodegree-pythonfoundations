import media
import fresh_tomatoes 

# Dictionary of all the instances displayed
case_dict = {"toy_story": media.Movie("Toy Story",
                                      "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                       "A story of a kid whose toys comes to life"),
             "fitzcarraldo": media.Movie("Fitzcarraldo",
                                         "https://www.youtube.com/watch?v=foRcsU4aXno",
                                         "http://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Fitzcarraldo.jpg/220px-Fitzcarraldo.jpg",
                                         "An Irishman known as Fitzcarraldo in Peru, \
                                         who is determined to transport a steamship over \
                                         a steep hill in order to access a rich rubber \
                                         territory"),
             "airbag": media.MusicVideo("Airbag",
                                        "https://www.youtube.com/watch?v=KgE29oRPhrI",
                                        "http://upload.wikimedia.org/wikipedia/en/thumb/a/a1/Radiohead.okcomputer.albumart.jpg/220px-Radiohead.okcomputer.albumart.jpg",
                                        "Radiohead"),
             "off the rails": media.MusicVideo("Off The Rails",
                                               "https://www.youtube.com/watch?v=iWOJlLYJiA4",
                                               "http://upload.wikimedia.org/wikipedia/en/d/d0/The_Notwist_Neon_Golden.jpg",
                                               "The Notwist"),
             "the x-files": media.TvSeries("The X-Files",
                                           "https://www.youtube.com/watch?v=mlZIVpVNgpI",
                                           "http://upload.wikimedia.org/wikipedia/en/e/e1/Thexfiles.jpg",
                                           "1"),
             "silicon valley": media.TvSeries("Silicon Valley",
                                              "https://www.youtube.com/watch?v=69V__a49xtw",
                                              "http://upload.wikimedia.org/wikipedia/en/thumb/3/33/Silicon_valley_title.png/250px-Silicon_valley_title.png",
                                              "1")
}

# Creating Object from dictionary
showcase = [case_dict[k] for k in case_dict.keys()]

# Launch Webpage
fresh_tomatoes.open_page(showcase)