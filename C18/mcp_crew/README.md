# McpCrew Crew

Welcome to the McpCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/mcp_crew/config/agents.yaml` to define your agents
- Modify `src/mcp_crew/config/tasks.yaml` to define your tasks
- Modify `src/mcp_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/mcp_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the mcp_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The mcp_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the McpCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


==================


ent variable.
An error occurred while running the crew: Command '['uv', 'run', 'run_crew']' returned non-zero exit status 1.
(.venv) sichilam@Sis-MacBook-Pro-2 mcp_crew % crewai run
Running the Crew
warning: `VIRTUAL_ENV=/Users/sichilam/Documents/dev/edureka/advancedAI/langchain_app/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
╭───────────────────────────────────────────────────── Crew Execution Started ─────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Crew Execution Started                                                                                                          │
│  Name: crew                                                                                                                      │
│  ID: ab2caf5a-ea34-4c7e-9689-5863acdb87b7                                                                                        │
│  Tool Args:                                                                                                                      │
│                                                                                                                                  │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: research_task (ID: 5b2985ac-4f04-42bf-898f-5e04becb7efe)
    Status: Executing Task...
╭──────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Agent: Weather Researcher                                                                                                       │
│                                                                                                                                  │
│  Task: Conduct a thorough research about weather for city: Ahmedabad Make sure you find any interesting and relevant             │
│  information given the city name.                                                                                                │
│                                                                                                                                  │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: research_task (ID: 5b2985ac-4f04-42bf-898f-5e04becb7efe)
    Status: Executing Task...
    └── 🔧 Used getWeatherInfo (1)
╭──────────────────────────────────────────────────── 🔧 Agent Tool Execution ─────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Agent: Weather Researcher                                                                                                       │
│                                                                                                                                  │
│  Thought: I need to gather the current weather data for Ahmedabad to compile the relevant information.                           │
│                                                                                                                                  │
│  Using Tool: getWeatherInfo                                                                                                      │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────── Tool Input ───────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  {                                                                                                                               │
│    "city": "Ahmedabad"                                                                                                           │
│  }                                                                                                                               │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭────────────────────────────────────────────────────────── Tool Output ───────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  {                                                                                                                               │
│    "coord": {                                                                                                                    │
│      "lon": 72.6167,                                                                                                             │
│      "lat": 23.0333                                                                                                              │
│    },                                                                                                                            │
│    "weather": [                                                                                                                  │
│      {                                                                                                                           │
│        "id": 804,                                                                                                                │
│        "main": "Clouds",                                                                                                         │
│        "description": "overcast clouds",                                                                                         │
│        "icon": "04d"                                                                                                             │
│      }                                                                                                                           │
│    ],                                                                                                                            │
│    "base": "stations",                                                                                                           │
│    "main": {                                                                                                                     │
│      "temp": 25.02,                                                                                                              │
│      "feels_like": 25.74,                                                                                                        │
│      "temp_min": 25.02,                                                                                                          │
│      "temp_max": 25.02,                                                                                                          │
│      "pressure": 1008,                                                                                                           │
│      "humidity": 83,                                                                                                             │
│      "sea_level": 1008,                                                                                                          │
│      "grnd_level": 1003                                                                                                          │
│    },                                                                                                                            │
│    "visibility": 10000,                                                                                                          │
│    "wind": {                                                                                                                     │
│      "speed": 3.09,                                                                                                              │
│      "deg": 240                                                                                                                  │
│    },                                                                                                                            │
│    "clouds": {                                                                                                                   │
│      "all": 100                                                                                                                  │
│    },                                                                                                                            │
│    "dt": 1788570381,                                                                                                             │
│    "sys": {                                                                                                                      │
│      "type": 1,                                                                                                                  │
│      "id": 9049,                                                                                                                 │
│      "country": "IN",                                                                                                            │
│      "sunrise": 1788569587,                                                                                                      │
│      "sunset": 1788614643                                                                                                        │
│    },                                                                                                                            │
│    "timezone": 19800,                                                                                                            │
│    "id": 1279233,                                                                                                                │
│    "name": "Ahmedabad",                                                                                                          │
│    "cod": 200                                                                                                                    │
│  }                                                                                                                               │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: research_task (ID: 5b2985ac-4f04-42bf-898f-5e04becb7efe)
    Status: Executing Task...
    └── 🔧 Used getWeatherInfo (1)
╭───────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Agent: Weather Researcher                                                                                                       │
│                                                                                                                                  │
│  Final Answer:                                                                                                                   │
│  - Current temperature: 25.02°C                                                                                                  │
│  - The temperature feels like: 25.74°C                                                                                           │
│  - Weather condition: Overcast clouds                                                                                            │
│  - Humidity level: 83%                                                                                                           │
│  - Atmospheric pressure: 1008 hPa                                                                                                │
│  - Wind speed: 3.09 m/s, coming from the southwest (240°)                                                                        │
│  - Cloud coverage: 100%                                                                                                          │
│  - Visibility: 10,000 meters                                                                                                     │
│  - Sunrise time: 6:53 AM IST                                                                                                     │
│  - Sunset time: 6:44 PM IST                                                                                                      │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: research_task (ID: 5b2985ac-4f04-42bf-898f-5e04becb7efe)
    Assigned to: Weather Researcher
    
    Status: ✅ Completed
    └── 🔧 Used getWeatherInfo (1)
╭──────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Task Completed                                                                                                                  │
│  Name: research_task                                                                                                             │
│  Agent: Weather Researcher                                                                                                       │
│                                                                                                                                  │
│  Tool Args:                                                                                                                      │
│                                                                                                                                  │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────╮
│                                                                                                                                  │
│  Crew Execution Completed                                                                                                        │
│  Name: crew                                                                                                                      │
│  ID: ab2caf5a-ea34-4c7e-9689-5863acdb87b7                                                                                        │
│  Tool Args:                                                                                                                      │
│  Final Output: - Current temperature: 25.02°C                                                                                    │
│  - The temperature feels like: 25.74°C                                                                                           │
│  - Weather condition: Overcast clouds                                                                                            │
│  - Humidity level: 83%                                                                                                           │
│  - Atmospheric pressure: 1008 hPa                                                                                                │
│  - Wind speed: 3.09 m/s, coming from the southwest (240°)                                                                        │
│  - Cloud coverage: 100%                                                                                                          │
│  - Visibility: 10,000 meters                                                                                                     │
│  - Sunrise time: 6:53 AM IST                                                                                                     │
│  - Sunset time: 6:44 PM IST                                                                                                      │
│                                                                                                                                  │
│                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────── Trace Batch Finalization ────────────────────────────────────────────────────╮
│ ✅ Trace batch finalized with session ID: e3fedea2-9b0e-46d3-b4dc-9e76a0a34a71                                                   │
│                                                                                                                                  │
│ 🔗 View here:                                                                                                                    │
│ https://app.crewai.com/crewai_plus/ephemeral_trace_batches/e3fedea2-9b0e-46d3-b4dc-9e76a0a34a71?access_code=TRACE-40b6e1603a     │
│ 🔑 Access Code: TRACE-40b6e1603a                                                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
(.venv) sichilam@Sis-MacBook-Pro-2 mcp_crew % 



