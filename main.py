from file_handler import File

f = File()
photos = f.read_input("input/a_example.txt")
print("\n".join([str(photo) for photo in photos]))

slideshow = [1, (2,3), 5]
f.write_output("test", slideshow)