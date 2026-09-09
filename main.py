from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage


def run_demo():
    demo_request = {
        "messages": [
            HumanMessage(content="I want to extract the data from the API endpoint 'https://pokeapi.co/api/v2/pokemon' and save it to data/extract folder in the csv folder")
        ],
        "route_response": ""
    }

    return data_agent.invoke(demo_request)


if __name__ == "__main__":
    response = run_demo()

    print(response)