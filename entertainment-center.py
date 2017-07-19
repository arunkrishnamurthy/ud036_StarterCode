"""
This file is the main file in the project-1. It crates a list of movies and generates a HTML file that would be opened in the browser to display the output required for the project-1
"""
from media import Movie
import fresh_tomatoes

#creating the Movie objects
thevar_magan = Movie("Thevar Magan", "145 mins", "The urbane son of a village chieftain struggles between his personal aspirations and those of his family.","https://images-na.ssl-images-amazon.com/images/M/MV5BNTY5YmE3MDQtM2JlYi00YWE1LWE2MWUtYTZlNDY2NThmMDQ4XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY268_CR3,0,182,268_AL__QL50.jpg", "https://www.youtube.com/watch?v=hnO00KHphQc")
					   
bahubali = Movie("Bahubali 2", "167 mins", "When Shiva, the son of Bahubali, learns about his heritage, he begins to look for answers. His story is juxtaposed with past events that unfolded in the Mahishmati Kingdom.","https://images-na.ssl-images-amazon.com/images/M/MV5BYmE1MTg0MDMtZmFlMC00ZGM3LTlkYWItNzEzOWRmODlhNDQ2XkEyXkFqcGdeQXVyNzMxMzYyOTI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg", "https://www.youtube.com/watch?v=qD-6d8Wo3do")

dhuruvangal_pathinaaru = Movie("Dhuruvangal Pathinaaru", "105 mins", "Deepak retires after an accident cuts off his right leg. Five years down the line, he is forced to revisit all the events leading to the accident.","https://images-na.ssl-images-amazon.com/images/M/MV5BZTNmZTg0ODUtZWRiZi00OTczLWJmOTYtMGI0MGQwZjNjMTk2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjE2MDg0NjI@._V1_UY268_CR6,0,182,268_AL__QL50.jpg", "https://www.youtube.com/watch?v=xpt2jfiL5GY")

thani_oruvan = Movie("Thani Oruvan", "160 mins", "A police officer makes it his mission to destroy the most corrupt person in the country, Siddharth Abimanyu.","https://images-na.ssl-images-amazon.com/images/M/MV5BNzgxMDc2Mjg3M15BMl5BanBnXkFtZTgwMzU4NTkxNzE@._V1_UY268_CR9,0,182,268_AL__QL50.jpg", "https://www.youtube.com/watch?v=r5Lih8rKd6k")

thalapathi = Movie("Thalapathi", "157 mins", "Surya (Rajnikanth) is an orphan raised in a slum. He finds a friend in the local Godfather (Mamooty). They rule the town and forms a parallel government.","https://images-na.ssl-images-amazon.com/images/M/MV5BZGE5NzVjNTEtMGUwYi00YzU0LWIyYTctNDc0ZjMxNGNhYzg5XkEyXkFqcGdeQXVyMjMwODI3NDE@._V1_QL50_.jpg", "https://www.youtube.com/watch?v=GJnQVMbNa_Y")


#creating a list of movies which is required as an input for open_movies_page function in the fresh_tomatoes module
movies_list = [thevar_magan, bahubali, dhuruvangal_pathinaaru, thani_oruvan, thalapathi]

#Generates the html file and opens browser to display it
fresh_tomatoes.open_movies_page(movies_list) 
