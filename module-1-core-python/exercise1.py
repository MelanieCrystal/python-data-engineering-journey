# ### 🎯 Exercise — Do This Yourself

# Create a new file: `module-1-core-python/exercise1.py`

# Write Python code that does the following — **no copy pasting, type it yourself:**

# 1. Create a variable called `your_name` with your actual name
# 2. Create a variable called `current_role` with value `"Support Engineer Trainee"`
# 3. Create a variable called `target_role` with value `"Data Engineer"`
# 4. Create a variable called `months_to_goal` with value `6`
# 5. Create a variable called `is_learning` with value `True`
# 6. Print this sentence using an **f-string**:
# ```
# Hi, my name is [your_name]. I am currently a [current_role] and I will become a [target_role] in [months_to_goal] months.
# ```
# 7. Print the **type** of `months_to_goal` and `is_learning`
# 8. Take `target_role` and print it in **uppercase**
# 9. Split `target_role` by the space and print the result

# ---

# ### 📤 Push to GitHub After Completing

# Once your exercise file is done, open Command Prompt and run:
# ```
# git add .
# git commit -m "Module 1 Lesson 1 - Variables and Data Types"
# git push

your_name = "Melanie Crystal Miranda"
current_role = "Support Engineer Trainee"
target_role = "Data Engineer"
months_to_goal = 6
is_learning = True

print(f"Hi, my name is '{your_name}'. I am currently a '{current_role}' and I will become a '{target_role}' in '{months_to_goal}' months.")

print(type(months_to_goal))
print(type(is_learning))

print(target_role.upper())

role = target_role.split(" ")
print(role)
