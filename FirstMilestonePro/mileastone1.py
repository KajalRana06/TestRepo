Menu_Prompt="Enter 'a' to add movie,'l' to list movie,'f' to search movie,'q' to quit:"
movies= []

def add_movie():
    title = input("Enter the movie name:")
    director = input("Enter the movie director:")
    year = input("Enter movie release year:")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    }
    )

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")

def find_movie():
    search_title = input("Enter movie title you are looking for:")

    for movie in movies:
        if movie["title"] == search_title:
            print(movie)

def menu():
    selection= input(Menu_Prompt)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            show_movies()
        elif selection == "f":
            find_movie()
        else:
            print("Unknown Command")

        selection = input(Menu_Prompt)

menu()

