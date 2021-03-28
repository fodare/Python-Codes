# Functions with output are functions which returns a result
# Sample 1
def format_name(fname, lname):
    """Return the first and last name in a title case!"""
    if fname == "" or lname == "":
        return "Please enter a valid input!"
    new_fname = fname.title()
    new_lname = lname.title()
    return (f"Welcome {new_fname} {new_lname}.")


formated_name = format_name("", "")
print(formated_name)
