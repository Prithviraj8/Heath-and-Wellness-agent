import json
import os

from langchain.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from pprint import pprint


class MentalHealthAgent:
    def __init__(self, user_data):
        self.user_data = user_data
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def provide_wellness_tips(self):
        context = self.tavily_client.get_search_context(
            query=f"wellness tips for {self.user_data['age']} year old with goal to {self.user_data['mental_health_goals']}"
        )
        mental_health_goals = self.user_data["mental_health_goals"]
        prompt = [
            {
                "role": "system",
                "content": "You are a mental health coach. Your task is to provide wellness tips based on user data.",
            },
            {
                "role": "user",
                "content": f"User data: {self.user_data}\n"
                f"Additional context: {context}\n"
                f"Provide mental wellness tips for someone looking to {mental_health_goals}.\n"
                f"Please return the tips in the following JSON format:\n"
                f'{{"wellness_tips": ["Tip 1", "Tip 2", "Tip 3", "Tip 4"]}}\n',
            },
        ]

        lc_messages = convert_openai_messages(prompt)
        optional_params = {"response_format": {"type": "json_object"}}
        response = (
            ChatOpenAI(
                model="gpt-4-0125-preview", max_retries=1, model_kwargs=optional_params
            )
            .invoke(lc_messages)
            .content
        )
        result = json.loads(response)
        print("Wellness Tip: \n")
        pprint(result)
        return result

    def start(self):
        return_data = dict
        return_data.update({"wellness_tip": self.provide_wellness_tips()})
        return return_data

if __name__ == "__main__":
    from pprint import pprint

    user_data = {
        "name": "Prithviraj Murthy",
        "age": 25,
        "mental_health_goals": "gain muscle and lose fat at the same time",
    }

    mental_health_agent = MentalHealthAgent(user_data)
    wellness_tips = mental_health_agent.provide_wellness_tips()
    print("Mental Wellness Tips:\n")
    pprint(wellness_tips, width=120)