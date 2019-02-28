from file_handler import File

f = File()
photos = f.read_input("input/a_example.txt")
print("\n".join([str(photo) for photo in photos]))