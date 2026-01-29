users = {}            # username -> user info
posts = []            # list of post dictionaries
post_id = 1           # numbering posts for easy reference
    
def create_username():
    print('Type a username')
    username = input()
    if username in users:
        print("That username already exists.")
        return None
    print(f'{username} nice to meet you!')
    print(f'{username} please input your short bio!')
    bio = input()
    users[username] = {"bio": bio, "followers": 0}
    print(f'users[{username}] = {users[username]}')
create_username()
#2
def create_post():
    global post_id
    username = input("Who is posting?")
    content = input("What do you want to say? ")

    post_id += 1

    post = {
        "id": post_id,
        "user": username,
        "content": content,
        "likes": 0
    } 
    posts.append(post) 
    print(f"Post created with ID {post_id}!")
create_post()

#3
def view_feed():
  if len(posts) == 0:
        print("Sorry there is no posts in the feed as of right now!")
  else:
      for post in posts:
        print(f"ID for {post['id']}")
        print(f"User: {post['user']}")
        print(f"Content: {post['content']}")
        print(f"Likes: {post['likes']}")


#1
def change_bio():
    username = input("What would you like to put it as")
    new_bio = input("Enter your new bio: ")
    users[username]["bio"] = new_bio
    print(f"Bio updated for {username}.")


#4
def like_a_post():
    post_id_like = int(input("Please put the id of the post you would wish to like:"))
    for post in posts:
        if post["id"]== post_id_like:
            post["likes"] = post["likes"] + 1
            print("Thank you the post is liked by you!")
            return

    
def menu():
    while True:
        print("Mini Twitter Menu")
        print("1. Change bio")
        print("2. Write a post")
        print("3. View the feed")
        print("4. Like a post")
        print("5. Exit")
        choice = input("Pick the number with the action that you want to do:")
        if choice == "1":
            change_bio()
        elif choice == "2":
            create_post()
        elif choice == "3":
            view_feed()
        elif choice == "4":
            like_a_post()
        elif choice == "5":
            print("Good bye! Have an amazing day")
            break
        else:
            print("Nice try, rewrite the number and action you want!")
            #5
menu()





    
