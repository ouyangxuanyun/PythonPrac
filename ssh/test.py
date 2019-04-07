from __future__ import print_function

import functools
import random
import sys
import time

import progressbar

examples = []


def example(fn):
    '''Wrap the examples so they generate readable output'''

    @functools.wraps(fn)
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % fn.__name__)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')
            # Sleep a bit to make killing the script easier
            time.sleep(0.2)

    examples.append(wrapped)
    return wrapped

@example
def basic_file_transfer():
    widgets = [
        'Test: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker='0', left='[', right=']'),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=500)
    bar.start()
    # Go beyond the max_value
    for i in range(100, 501, 50):
        time.sleep(0.1)
        bar.update(i)
    bar.finish()



def test(*tests):
    for example in examples:
        if not tests or example.__name__ in tests:
            example()
        else:
            print('Skipping', example.__name__)

if __name__ == '__main__':
    try:
        test(*sys.argv[1:])
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')