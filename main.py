from agents.planner_agent import PlannerAgent
from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.summary_agent import SummaryAgent

from dotenv import load_dotenv
load_dotenv()



def run_goal_pipeline(goal):
    print("[User Goal]", goal)

    planner = PlannerAgent()
    tasks = planner.plan(goal)
    print("\n[Planner Output] Tasks:", tasks)

    data = None
    result = ""
    for task in tasks:
        if "spacex" in task.lower():
            spacex = SpaceXAgent()
            data = spacex.get_next_launch()
            print("\n[SpaceX Output]", data)

        elif "weather" in task.lower():
            weather = WeatherAgent()
            data = weather.get_weather(data)
            print("\n[Weather Output]", data)

        elif "summarize" in task.lower():
            summarizer = SummaryAgent()
            result = summarizer.analyze(data)
            print("\n[Final Summary]", result)
    
    return result


if __name__ == '__main__':
    user_goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."
    run_goal_pipeline(user_goal)