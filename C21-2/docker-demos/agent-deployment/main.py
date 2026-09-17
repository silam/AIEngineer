from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from langchain.tools import tool
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import requests
import os

load_dotenv()

llm = ChatOpenRouter(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


@tool
def getWeatherInfo(city: str):
    """
    Get the current weather for a city using openweathermap api
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("WEATHER_API_KEY"),
        "units": "metric"
    }

    response = requests.get(url, params)

    if response.status_code != 200:
        return f"Unable to fetch data from weather api"
    return response.json()


agent = create_agent(
    model=llm,
    system_prompt="""
    You are a a helpful AI agent who answers queries with a bit of humour. Use emojis to decorate your responses. Be polite and professional.
    """,
    tools=[getWeatherInfo]
)

app = FastAPI(title="Weather AI Agent")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": request.message}
            ]
        }
    )
    return ChatResponse(reply=response["messages"][-1].content)


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)