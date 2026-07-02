import json

from pathlib import Path

from gemini_client import GeminiClient


class Pipeline:

    def __init__(self):

        self.ai = GeminiClient()

    def run(self, topic):

        data = self.ai.generate(topic)

        Path("output").mkdir(exist_ok=True)

        with open(
            "output/story.json",
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
            )

        print()

        print("Scenariusz zapisany.")

        print("output/story.json")

        return data
