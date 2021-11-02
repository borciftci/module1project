from eca import *

import random

# define a normal python function
def clip(lower, value, upper):
    return max(lower, min(value, upper))

# binds the 'setup' function as the function for the 'init' event
# the action willbe called with the context and the event
@event('init')
def setup(ctx, e):
    ctx.count = 0
    fire('sample', {'previous':0.0})

@event('sample')
@condition(lambda c,e: c.count < 100)
def generate_sample(ctx, e):
    ctx.count += 1

    # base sample on previous one
    sample = clip(-100, e.get('previous') + random.uniform(+5.0, -5.0), 100)

    # print the sample on the console
    print('Sample ' + str(ctx.count)+': '+str(sample))

    # chain event
    fire('sample', {'previous': sample}, delay = 0.05)
    

