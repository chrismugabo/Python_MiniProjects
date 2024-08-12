 # Step 1: Read the starting letter template
with open("/Users/user/Desktop/Python/Python_MiniProjects/Mail Merge/Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

# Step 2: Read the list of names from invited_names.txt
with open("/Users/user/Desktop/Python/Python_MiniProjects/Mail Merge/Input/Names/invited_names.txt") as file:
    names = file.readlines()

# Step 3: Create personalized letters
for name in names:
    stripped_name = name.strip()  # Remove any leading/trailing whitespace
    personalized_letter = letter_template.replace("[name]", stripped_name)
    
    # Step 4: Save the personalized letter in the "ReadyToSend" folder
    output_path = f"/Users/user/Desktop/Python/Python_MiniProjects/Mail Merge/Output/ReadyToSend/letter_for_{stripped_name}.txt"
    with open(output_path, "w") as output_file:
        output_file.write(personalized_letter)

    print(f"Letter created for {stripped_name}")
