from functions.get_file_content import get_file_content


# Test large file
result = get_file_content("calculator", "lorem.txt")

print("lorem.txt truncated:", "truncated" in result)
print("Length:", len(result))


# Test main.py
print("\nContents of main.py:")
print(get_file_content("calculator", "main.py"))


# Test pkg/calculator.py
print("\nContents of pkg/calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py"))


# Test file outside working directory
print("\nContents of /bin/cat:")
print(get_file_content("calculator", "/bin/cat"))


# Test file that doesn't exist
print("\nContents of pkg/does_not_exist.py:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))










