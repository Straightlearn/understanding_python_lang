def take(funt):
    print('inside take function')
    def show():
        print('inside show function')
        funt()
    return show
    def greeting():
        print('hi')
    

@take
def details():
    name=input('Full Name: ')
    age=input('Age: ')
    school=input('School: ')
    course=input('Course: ')
    reg_num=input('Registration number: ')

details()
obj=take
obj(details)
