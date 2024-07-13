# main.py
from concurrent.futures import ThreadPoolExecutor

from langchain.agents import AgentExecutor, Tool
from langgraph.graph import Graph

from agents.fitness_agent import FitnessAgent
from agents.nutrition_agent import NutritionAgent
from agents.mental_health_agent import MentalHealthAgent
from agents.progress_tracking_agent import ProgressTrackingAgent
from agents.reminder_agent import ReminderAgent
from user_interaction import collect_user_data

from pprint import pprint


def collect_feedback(agent_name):
    feedback = input(f"Provide feedback on your {agent_name} plan\n")
    return feedback


def main():
    # Collect user data
    user_data = collect_user_data()
    # user_data = {
    #     "name": "Prithviraj",
    #     "age": 25,
    #     "weight": 94,
    #     "height": 186,
    #     "fitness_goals": "lose fat and gain muscle",
    #     "dietary_preferences": "non veg",
    #     "mental_health_goals": "lose fat and maintain muscle",
    # }

    # Initialize agents
    fitness_agent = FitnessAgent(user_data)
    nutrition_agent = NutritionAgent(user_data)
    mental_health_agent = MentalHealthAgent(user_data)
    progress_agent = ProgressTrackingAgent(user_data)

    # Define a LangGraph workflow
    workflow = Graph()

    # Add nodes for each agent task
    workflow.add_node("fitness", lambda _: fitness_agent.start())
    workflow.add_node("collect_fitness_feedback", lambda _: collect_feedback("fitness"))
    workflow.add_node(
        "adjust_fitness",
        lambda x: fitness_agent.start(x) if x else fitness_agent.current_workout_plan,
    )
    workflow.add_node("nutrition", lambda _: nutrition_agent.start())
    workflow.add_node(
        "collect_nutrition_feedback", lambda _: collect_feedback("nutrition")
    )
    workflow.add_node(
        "adjust_nutrition",
        lambda x: nutrition_agent.start(x) if x else nutrition_agent.current_meal_plan,
    )
    workflow.add_node("mental_health", lambda _: mental_health_agent.start())
    workflow.add_node(
        "collect_mental_health_feedback", lambda _: collect_feedback("mental health")
    )
    workflow.add_node(
        "adjust_mental_health",
        lambda x: (
            mental_health_agent.start(x) if x else mental_health_agent.wellness_tips
        ),
    )
    workflow.add_node(
        "progress_report",
        lambda _: progress_agent.track_progress(
            fitness_agent.current_workout_plan,
            nutrition_agent.current_meal_plan,
            mental_health_agent.wellness_tips,
        ),
    )

    # Add edges for initial plan creation and feedback collection
    workflow.add_edge("fitness", "collect_fitness_feedback")
    workflow.add_edge("collect_fitness_feedback", "adjust_fitness")
    workflow.add_edge("adjust_fitness", "nutrition")
    workflow.add_edge("nutrition", "collect_nutrition_feedback")
    workflow.add_edge("collect_nutrition_feedback", "adjust_nutrition")
    workflow.add_edge("adjust_nutrition", "mental_health")
    workflow.add_edge("mental_health", "collect_mental_health_feedback")
    workflow.add_edge("collect_mental_health_feedback", "adjust_mental_health")
    workflow.add_edge("adjust_mental_health", "progress_report")

    # Conditional edge for fitness feedback
    workflow.add_conditional_edges(
        source="collect_fitness_feedback",
        path=lambda x: "adjust_fitness" if x else "nutrition",
        path_map={"adjust_fitness": "adjust_fitness", "nutrition": "nutrition"},
    )

    # Conditional edge for nutrition feedback
    workflow.add_conditional_edges(
        source="collect_nutrition_feedback",
        path=lambda x: "adjust_nutrition" if x else "mental_health",
        path_map={
            "adjust_nutrition": "adjust_nutrition",
            "mental_health": "mental_health",
        },
    )

    # Conditional edge for mental health feedback
    workflow.add_conditional_edges(
        source="collect_mental_health_feedback",
        path=lambda x: "adjust_mental_health" if x else "progress_report",
        path_map={
            "adjust_mental_health": "adjust_mental_health",
            "progress_report": "progress_report",
        },
    )

    # Set up start and end nodes
    workflow.set_entry_point("fitness")
    workflow.set_finish_point("progress_report")

    # Compile the graph
    chain = workflow.compile()

    # Execute the graph for each query in parallel
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda _: chain.invoke({}), [{}]))

    for result in results:
        print("Result: \n")
        pprint(result)


if __name__ == "__main__":
    main()
