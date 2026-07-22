import os
import json
import requests

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from langchain_core.language_models.llms import LLM

load_dotenv()

class CompanyLLM(LLM):

    @property
    def _llm_type(self):
        return "company_llm"

    def _call(self, prompt, stop=None, run_manager=None, **kwargs):

        url = os.getenv("LLAMA_BASE_URL") + "/chat"

        payload = {

            "model": os.getenv("LLAMA_MODEL"),

            "messages": [

                {
                    "role":"user",
                    "content":prompt
                }

            ],

            "stream":False

        }

        response = requests.post(

            url,

            json=payload,

            auth=HTTPBasicAuth(

                os.getenv("LLAMA_USERNAME"),

                os.getenv("LLAMA_PASSWORD")

            ),

            verify=False,

            timeout=120

        )

        response.raise_for_status()

        return response.json()["message"]["content"]