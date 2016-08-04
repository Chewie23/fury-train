#***PYTHON 3***

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import NewPost
import getpass

pw = getpass.getpass("Please type your password: ")
wp = Client('https://chewie23.wordpress.com/xmlrpc.php', 'Chewie23', pw)
print ("Got Client")

while True:    
    title = ''
    usr_choice = input("""Please enter your category:
(Defaults to [1] 100 word stories)
[1] 100 word stories
[2] Long Form
[3] Quit
> """)
    if usr_choice == "3" or usr_choice == "q":
        print ("Goodbye!")
        break
    elif usr_choice == "2":
        choice = "Long Form"
        title = input("Enter a title for the Long Form story: ")
    else:
        usr_choice = "1"
        choice = "100 word stories"
    print ("You chose [%s]" % usr_choice)
    
    print ("""Accessing WPS.txt...
Please note that you can only use 'single quotes' for the file to be valid""")
    with open("WPS.txt", "r") as f:
        story = f.read()
        print (story)
        
    post = WordPressPost()
    post.title = title
    post.content = story
    post.terms_names = {
        'category': [choice]
    }
    print ("Connecting...")
    post.id = wp.call(posts.NewPost(post))
    print ("Posting...")
    post.post_status = 'publish'
    wp.call(posts.EditPost(post.id, post))
    print ("Finished!")