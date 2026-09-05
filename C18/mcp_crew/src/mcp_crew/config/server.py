from mcp.server import MCPServer
import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


mcp = MCPServer("weather-demo")



@mcp.tool()
def getWeatherInfo(city: str):
    """
    Get the current weather for an indian city using Openweathermap api
    """
    if not OPENWEATHERMAP_API_KEY:
        return "Weather API key not found"
    
    url="https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }
    
    response = requests.get(url, params)
    
    if response.status_code !=200:
        return f"Unable to fetch data from weather api"
    
    return response.json()

if __name__=="__main__":
    mcp.run(transport="stdio", host="0.0.0.0", port=8000)