import sys
import types
import unittest


langchain_openai = types.ModuleType("langchain_openai")


class ChatOpenAI:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def invoke(self, *args, **kwargs):
        return {"args": args, "kwargs": kwargs}


langchain_openai.ChatOpenAI = ChatOpenAI
sys.modules.setdefault("langchain_openai", langchain_openai)


langchain_anthropic = types.ModuleType("langchain_anthropic")


class ChatAnthropic:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def invoke(self, *args, **kwargs):
        return {"args": args, "kwargs": kwargs}


langchain_anthropic.ChatAnthropic = ChatAnthropic
sys.modules.setdefault("langchain_anthropic", langchain_anthropic)


from utils.llm_pick import pick_llm


class PickLlmTests(unittest.TestCase):
    def test_pick_low_model(self):
        llm = pick_llm("low")
        self.assertEqual(llm.__class__.__name__, "ChatOpenAI")

    def test_pick_claude_model(self):
        llm = pick_llm("claude")
        self.assertEqual(llm.__class__.__name__, "ChatAnthropic")

    def test_rejects_unknown_level(self):
        with self.assertRaises(ValueError):
            pick_llm("unknown")


if __name__ == "__main__":
    unittest.main()
