class PlannerAgent:
    def plan(self, goal):
        tasks = []
        if "spacex" in goal.lower():
            tasks.append("Query SpaceX API for next launch")
        if "weather" in goal.lower():
            tasks.append("Check weather at launch site")
        if "summarize" in goal.lower() or "delay" in goal.lower():
            tasks.append("Summarize delay possibility")
        return tasks