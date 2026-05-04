import pytest


@pytest.mark.usefixtures('setWebdriver')
class TestAIAuthoring:

    def test_with_ai_agent(self):
        # Search using AI Agent commands
        self.driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": ["Tap on Search Wikipedia"]}'
        )
        self.driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": ["Type India in the search field"]}'
        )

        # Verify results
        self.driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": ["Verify search results are displayed"]}'
        )
