import json

from google import genai

from config import settings


MODEL = "gemini-2.5-flash"


SYSTEM_PROMPT = """
You are a professional short video writer.

Return ONLY JSON.

{
 "title":"",
 "voiceover":"",
 "cta":"",
 "hashtags":[],
 "scenes":[
   {
      "id":1,
      "duration":6,
      "video_prompt":""
   }
 ]
}
"""


class GeminiClient:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, topic: str):

        response = self.client.models.generate_content(
            model=MODEL,
            contents=f"""
Topic:

{topic}

Language:
{settings.LANGUAGE}

Length:
18 seconds
""",
            config={
                "system_instruction": SYSTEM_PROMPT
            }
        )

        return json.loads(response.text)
