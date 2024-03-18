def write_and_read_file():
  """Writes content to a file, reads it back, and appends additional lines with error handling."""

  try:
    # Open the file "my_file.txt" in write mode ("w")
    with open("my_file.txt", "w") as file:
      # Write three lines of text, including a mix of strings and numbers
      file.write("This is the first line.\n")
      file.write(str(42) + " is the answer to the ultimate question of life, the universe, and everything.\n")
      file.write("Here's some more text for good measure.\n")

    # Open the file "my_file.txt" in read mode ("r")
    with open("my_file.txt", "r") as file:
      # Read the contents and print them
      contents = file.read()
      print("Contents of the file:\n", contents)

    # Open the file "my_file.txt" in append mode ("a")
    with open("my_file.txt", "a") as file:
      # Append three additional lines
      file.write("\nAppending some more content...\n")
      file.write("Line 4: New information!\n")
      file.write("Line 5: The end (for now).")

    # Read the entire file again and print the contents (including appended lines)
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print("\nContents of the file after appending:\n", contents)

  except FileNotFoundError:
    print("The file 'my_file.txt' does not exist yet. It has been created.")

# Run the function
write_and_read_file()
