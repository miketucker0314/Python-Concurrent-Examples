import asyncio

# define a coroutine for a task
async def task_coroutine(number):
    # report a message
    print('executing the task: ', number)
    # block for a moment
    await asyncio.sleep(1)
    return number*2
 
# custom coroutine
async def test_tasks():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine(0))
    # wait for the task to complete
    await task
    # report a final message
    print('main coroutine done')

async def test_many_tasks():
    values = []
    # report a message
    print('main coroutine started')
    # create and schedule many tasks
    tasks = [asyncio.create_task(task_coroutine(i)) for i in range(20)]
    # wait for each task to complete
    for task in tasks:
        values.append(await task)
    # report a final message
    print('main coroutine done, values: ', values) 
