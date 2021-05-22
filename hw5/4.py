import os
import logging



def log(path, multipleLocs=False):
    from person import Person
    from sample import logging
    fname = os.path.splitext(path)[0]
    logger = logging.getLogger(fname)
    # if path == 'F:\me\Maktab Sharif\جنگو\hw5\sample.log':
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(path)
    formatter = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    # elif path == 'F:\me\Maktab Sharif\جنگو\hw5\person.log':
    #     logger.setLevel(logging.DEBUG)
    #     fh = logging.FileHandler(path)
    #     formatter = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(msecs)s-%(message)s")
    #     fh.setFormatter(formatter)
    #     logger.addHandler(fh)

    if multipleLocs:
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)
        frmt = logging.Formatter("%(asctime)s-%(levelname)-s-%(message)s")
        console.setFormatter(frmt)
        logger.addHandler(console)


log('F:\me\Maktab Sharif\جنگو\hw5\sample.log', multipleLocs=True)
log('F:\me\Maktab Sharif\جنگو\hw5\person.log')


