import logging
from time import time
from multiprocessing import Pool, cpu_count, current_process


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*numbers):

    result = []

    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        result.append(factors)
    
    return tuple(result)


if __name__ == '__main__':

    timer = time()
    numbers = [100572682, 100372682, 100072682, 109972682, 100572682, 100372682, 100072682, 109972682, 100572682, 100372682, 100072682, 109972682, 100572682, 100372682, 100072682, 109972682]
    factorize(*numbers)
    logging.debug(f"Done {time() - timer}")
    
    cores = cpu_count()
    
    print(cores)

    timer2 = time()
    with Pool(processes=cores) as pool:
        logger.debug(pool.map(factorize, numbers))
    logging.debug(f"Done {time() - timer2}")
    