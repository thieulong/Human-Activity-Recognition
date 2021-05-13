file = "links.txt"


with open(file) as f:

    links_list = f.read().splitlines()

link = input("Enter a Youtube's video URL: ")

if link in links_list:

    print("\nThis video is already existed! PLease choose another one.\n")

elif link not in links_list:

    print("\nValid video!\n")