from tqdm import tqdm
import asyncio
import math
import types


class Downloader(object):
    
    def __init__(self, handlers=[], batch=10):
        """
        init attributes
        :param handlers:
        """
        self.handlers = handlers
        self.batch = batch
    
    def add_handler(self, handler):
        """
        add one handler
        :param handler: handler object
        :return:
        """
        self.handlers.append(handler)
    
    def set_handlers(self, handlers):
        """
        set handlers
        :param handlers:
        :return:
        """
        self.handlers = handlers
    
    def get_handlers(self):
        """
        get handlers of downloader
        :return:
        """
        return self.handlers
    
    def update_progress(self, _):
        """
        update progress bar
        :return:
        """
        self.bar.update(1)
    
    async def process_item(self, obj):
        """
        process item
        :param obj: single obj
        :return:
        """
        raise NotImplementedError
    
    def process_items(self, objs):
        """
        process items
        :param objs: objs
        :return:
        """
        # define progress bar
        with tqdm(total=len(objs)) as self.bar:
            # init event loop
            loop = asyncio.get_event_loop()
            # get num of batches
            total_step = int(math.ceil(len(objs) / self.batch))
            # for every batch
            for step in range(total_step):
                start, end = step * self.batch, (step + 1) * self.batch
                print('Processing %d-%d of files' % (start + 1, end))
                # get batch of objs
                objs_batch = objs[start: end]
                # define tasks and run loop
                tasks = [asyncio.ensure_future(self.process_item(obj)) for obj in objs_batch]
                for task in tasks:
                    task.add_done_callback(self.update_progress)
                loop.run_until_complete(asyncio.wait(tasks))
    
    def download(self, inputs):
        """
        download video or video lists
        :param data:
        :return:
        """
        if isinstance(inputs, types.GeneratorType):
            temps = []
            for result in inputs:
                print('Processing', result, '...')
                temps.append(result)
                if len(temps) == self.batch:
                    self.process_items(temps)
                    temps = []
            self.process_item(temps)
        else:
            inputs = inputs if isinstance(inputs, list) else [inputs]
            self.process_items(inputs)
