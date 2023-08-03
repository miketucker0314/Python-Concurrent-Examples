import asyncio
import async_examples
import asyncio_tasks_examples
import threading_examples
import multiprocessing_asyncio

test_async = False
test_threading = False
test_multiprocessing_asyncio = True

if __name__ == "__main__":

    if (test_async == True):

        asyncio.run(async_examples.count_test())

        asyncio.run(asyncio_tasks_examples.test_tasks())

        asyncio.run(asyncio_tasks_examples.test_many_tasks())

    if(test_threading == True):
        threading_examples.test_threading()

    if(test_multiprocessing_asyncio == True):
        multiprocessing_asyncio.test_multiprocessing_asyncio()


