import multiprocessing
import asyncio

# each time a class is created, a new thread is started with its own event loop
#  Each thread creates a number of tasks on its own event loop

class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, id, durations):
        super(MultiprocessingAsync, self).__init__()
        self._durations = durations
        self._id = id

    @staticmethod
    async def async_sleep(id, duration):
        await asyncio.sleep(duration)
        return id, duration

    async def consecutive_sleeps(self):
        pending = set()

        for duration in self._durations:
            pending.add(asyncio.create_task(self.async_sleep(self._id, duration)))  

        while len(pending) > 0:
            done, pending = await asyncio.wait(pending, timeout=1) 
            for done_task in done:
                print(await done_task)

    # run is called when start is called on an instance of the class
    def run(self):
        asyncio.run(self.consecutive_sleeps())
        print('Processed Finished:', self._id)

def test_multiprocessing_asyncio():

    durations = []
    durations0 = [1,4,6,2]
    durations1 = [2,3,2,1]
    
    durations.append(durations0)
    durations.append(durations1)

    processes = []
    for i in range(2):
        processes.append(MultiprocessingAsync(i, durations[i]))

    for p in processes:
        p.start()

    for p in processes:
        p.join()
