my_name='Zed A. Shaw'
my_age=35
my_height=74
my_weight=180
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print 'Let\'s talk about %s.' %my_name
print 'He\'s %d inches tall.' %my_height
print 'He\'s %d pounds heavy.' %my_weight
print 'Actually that\'s not too heavy.'
print 'He\'s got %s eyes and %s hair.' %(my_eyes,my_hair)
print 'His teeth are usually %s depending on the coffee.' % my_teeth

print 'If I add %d, %d, and %d I get %d.' %(my_age, my_height, my_weight, my_age+my_height+my_weight) 

x='There are %d types of people.' %10
binary='binary'
do_not='don\'t'
y='Those who know %s and those who %s.' %(binary, do_not)

print x
print y

print 'I said: %r.' %x
print 'I also said: %s.' %y

hilarious=False
joke_evaluation='Is\'nt that joke so funny?! %r'

print joke_evaluation % hilarious

w='This is the left side of...'
e='a string with a right side.'

print w+e