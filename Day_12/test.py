""" Scopes"""
# Local variable = Variables accessible with the creation container
# Global variable = Variable accessible anywhere within a program
# Constants in python are declared in uppercase variable names

enemies = 0
def increase_enemies():
    return enemies + 2

print(f"Modified enemies is: {increase_enemies()}")


