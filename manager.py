from __future__ import annotations

import asyncio
import time
import json
from collections.abc import Sequence

from rich.console import Console

from agents import Runner, RunResult, custom_span, gen_trace_id, trace

from agent import History, historical_agent
from agent import Culinary, culinary_agent
from agent import Culture, culture_agent
from agent import Architecture, architecture_agent
from agent import Planner, planner_agent
from agent import FinalTour, orchestrator_agent
from printer import Printer


class TourManager:
    """
    Orchestrates the full flow
    """

    def __init__(self) -> None:
        self.console = Console()
        self.printer = Printer(self.console)

    async def run(self, query: str, interests: list, duration: str) -> str:
        trace_id = gen_trace_id()
        with trace("Tour Research trace", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                "View trace: https://platform.openai.com/traces/{}".format(trace_id),
                is_done=True,
                hide_checkmark=True,
            )
            self.printer.update_item("start", "Starting tour research...", is_done=True)

            # Get plan based on selected interests
            planner = await self._get_plan(query, interests, duration)

            # Initialize research results
            research_results = {}

            # Calculate word limits based on duration (150 words per minute)
            words_per_minute = 150
            total_words = int(duration) * words_per_minute

            # Calculate words for each selected interest
            num_interests = len(interests)
            if num_interests > 0:
                words_per_interest = total_words // num_interests
            else:
                words_per_interest = total_words

            # Only research selected interests
            if "Architecture" in interests:
                research_results["architecture"] = await self._get_architecture(query, interests, words_per_interest)

            if "History" in interests:
                research_results["history"] = await self._get_history(query, interests, words_per_interest)

            if "Culinary" in interests:
                research_results["culinary"] = await self._get_culinary(query, interests, words_per_interest)

            if "Culture" in interests:
                research_results["culture"] = await self._get_culture(query, interests, words_per_interest)

            # Get final tour with only selected interests
            final_tour = await self._get_final_tour(
                query,
                interests,
                duration,
                research_results
            )

            self.printer.update_item("final_report", "Tour generation completed", is_done=True)
            self.printer.end()

            return final_tour.output  # Return the string content for TTS

    async def _get_plan(self, query: str, interests: list, duration: str) -> Planner:
        self.printer.update_item("Planner", "Planning your personalized tour...")
        result = await Runner.run(
            planner_agent,
            "Location: {} | Interests: {} | Duration: {} minutes".format(query, ', '.join(interests), duration)
        )
        self.printer.update_item(
            "Planner",
            "Completed planning",
            is_done=True,
        )
        return result.final_output_as(Planner)

    async def _get_history(self, query: str, interests: list, word_limit: int) -> str:
        self.printer.update_item("History", "Researching historical highlights...")
        result = await Runner.run(
            historical_agent,
            "Location: {} | Interests: {} | Word Limit: {} words. Create engaging historical content for an audio tour. Focus on interesting stories and personal connections. Make it conversational and natural for speech.".format(
                query, ', '.join(interests), word_limit)
        )
        self.printer.update_item(
            "History",
            "Completed history research",
            is_done=True,
        )
        history_output = result.final_output_as(History)
        return history_output.output

    async def _get_architecture(self, query: str, interests: list, word_limit: int) -> str:
        self.printer.update_item("Architecture", "Exploring architectural wonders...")
        result = await Runner.run(
            architecture_agent,
            "Location: {} | Interests: {} | Word Limit: {} words. Create engaging architectural content for an audio tour. Focus on visual descriptions and interesting design details. Make it conversational and natural for speech.".format(
                query, ', '.join(interests), word_limit)
        )
        self.printer.update_item(
            "Architecture",
            "Completed architecture research",
            is_done=True,
        )
        arch_output = result.final_output_as(Architecture)
        return arch_output.output

    async def _get_culinary(self, query: str, interests: list, word_limit: int) -> str:
        self.printer.update_item("Culinary", "Discovering local flavors...")
        result = await Runner.run(
            culinary_agent,
            "Location: {} | Interests: {} | Word Limit: {} words. Create engaging culinary content for an audio tour. Focus on local specialties and food stories. Make it conversational and natural for speech.".format(
                query, ', '.join(interests), word_limit)
        )
        self.printer.update_item(
            "Culinary",
            "Completed culinary research",
            is_done=True,
        )
        culinary_output = result.final_output_as(Culinary)
        return culinary_output.output

    async def _get_culture(self, query: str, interests: list, word_limit: int) -> str:
        self.printer.update_item("Culture", "Exploring cultural highlights...")
        result = await Runner.run(
            culture_agent,
            "Location: {} | Interests: {} | Word Limit: {} words. Create engaging cultural content for an audio tour. Focus on local traditions and community life. Make it conversational and natural for speech.".format(
                query, ', '.join(interests), word_limit)
        )
        self.printer.update_item(
            "Culture",
            "Completed culture research",
            is_done=True,
        )
        culture_output = result.final_output_as(Culture)
        return culture_output.output

    async def _get_final_tour(self, query: str, interests: list, duration: float, research_results: dict) -> FinalTour:
        self.printer.update_item("Final Tour", "Creating your personalized tour...")

        # Build content sections string for the orchestrator
        content_sections = []
        for interest in interests:
            interest_lower = interest.lower()
            if interest_lower in research_results:
                content_sections.append(f"{interest} Content:\n{research_results[interest_lower]}")

        # Calculate total words based on duration
        words_per_minute = 150
        total_words = int(duration) * words_per_minute

        prompt = f"""
        Location: {query}
        Selected Interests: {', '.join(interests)}
        Tour Duration: {duration} minutes
        Target Word Count: {total_words} words

        Content from Specialists:
        {'\n\n'.join(content_sections)}

        Please create a natural, conversational audio tour that flows smoothly. 
        Include an engaging introduction and thoughtful conclusion.
        Make it sound like a friendly guide speaking to the visitor.
        Use natural transitions and maintain a conversational tone throughout.
        The total content should be approximately {total_words} words.
        """

        result = await Runner.run(orchestrator_agent, prompt)

        self.printer.update_item(
            "Final Tour",
            "Completed Final Tour Guide Creation",
            is_done=True,
        )
        return result.final_output_as(FinalTour)