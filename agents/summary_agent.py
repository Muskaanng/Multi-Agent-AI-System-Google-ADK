class SummaryAgent:
    def analyze(self, weather_data):
        if "error" in weather_data:
            return "Weather data incomplete; cannot determine delay risk."

        temp = weather_data.get("temperature")
        wind = weather_data.get("wind_speed")
        desc = weather_data.get("weather", "").lower()

        delay_risk = []
        if "rain" in desc or "storm" in desc or "thunder" in desc:
            delay_risk.append("stormy weather")
        if wind and wind > 12:
            delay_risk.append("high wind")
        if temp and (temp < -10 or temp > 40):
            delay_risk.append("extreme temperature")

        if delay_risk:
            return f"Potential delay due to: {', '.join(delay_risk)}."
        else:
            return "Weather conditions seem optimal for launch."