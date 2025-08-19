from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import asyncio


class FastAPIStreamingCallbackHandler(StreamingStdOutCallbackHandler):
    def __init__(self):
        self.queue = asyncio.Queue()

    def on_llm_new_token(self, token: str, **kwargs):
        self.queue.put_nowait(token)

    async def get_stream(self):
        while True:
            token = await self.queue.get()
            if token is None:
                break
            yield token
