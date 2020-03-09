# function
def welcome():
    print('Hello World')
    for x in range(10):
        print('Hi', str(x))
welcome()

# parameter 
def sayWelcome(name):
    print('Welcome {name}'.format(name=name))
sayWelcome('Shahriar')

# Lambda 