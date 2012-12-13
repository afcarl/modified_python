"""
    A test python file for our const keyword
"""

# # This doesn't error out
# y = 5
# const y = 6

# # This one doesn't either
# const x = 8
# x = 4

# # This does error out
# def a():
#     const x = 6
#     x = 5

# # This one too
# def b():
#     y = 8
#     const y = 3

# # You can still use const variables as regular variables
# def c(x):
#     const z = 3
#     return x + z

# # Mixing scopes is weird though
# const z = 5
# def d():
#     global z
#     z += 1
#     return z

# print a()
# print b()
# print c(3)
# print d()