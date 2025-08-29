import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew


# Configure LLM
llm = ChatOpenAI(
	api_key=openai_api_key,
	model="gpt-4o-mini",
	temperature=0.2,
)

# Define agents
researcher = Agent(
	role="Исследователь",
	goal="Собирать точные факты по теме и готовить краткую выжимку",
	backstory=(
		"Вы опытный аналитик, который быстро находит факты, проверяет их и "
		"возвращает краткую выжимку без лишней воды."
	),
	llm=llm,
	verbose=True,
)

writer = Agent(
	role="Писатель",
	goal="Писать чёткие и структурированные ответы на основе материалов исследователя",
	backstory=(
		"Вы техничный писатель. Умеете превращать сухие факты в связный, "
		"краткий и полезный текст."
	),
	llm=llm,
	verbose=True,
)

# Define tasks
collect_facts = Task(
	description=(
		"Соберите 3-5 точных фактов о библиотеке CrewAI: назначение, ключевые возможности, "
		"минимальный пример использования. Верните краткую выжимку в виде списка."
	),
	expected_output="Краткий список фактов (3-5 пунктов)",
	agent=researcher,
)

compose_answer = Task(
	description=(
		"На основе выжимки исследователя напишите краткий пример использования CrewAI на Python: "
		"два агента и две задачи, запуск команды, вывод результата. Верните только финальный текст ответа."
	),
	expected_output="Короткий структурированный ответ с примером кода",
	agent=writer,
)

# Orchestrate crew
crew = Crew(
	agents=[researcher, writer],
	tasks=[collect_facts, compose_answer],
	verbose=True,
)

if __name__ == "__main__":
	result = crew.kickoff()
	print("\n===== РЕЗУЛЬТАТ =====\n")
	print(result)
