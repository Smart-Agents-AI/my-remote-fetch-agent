import os
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from protocols import Message

# Setting up the agent with environment variables
AGENT_SEED_PHRASE = os.environ.get('SEED_PHRASE', 'my_seed_phrase')
AGENT_ENDPOINT = os.environ.get(
    'AGENT_ENDPOINT', 'http://127.0.0.1:8001/submit')
AGENT_PORT = int(os.environ.get('PORT', 8001))

agent = Agent(
    name="my_remote_fetch_agent",
    port=AGENT_PORT,
    endpoint=[AGENT_ENDPOINT],
    seed=AGENT_SEED_PHRASE
)

# Retrieving the agent's address and ensuring wallet has sufficient funds
AGENT_ADDRESS = Agent(seed=AGENT_SEED_PHRASE).address
print(f"Your agent's address is: {AGENT_ADDRESS}")
fund_agent_if_low(agent.wallet.address())

# Defining the message handler for the agent


@agent.on_message(model=Message, replies=Message)
async def on_sender_message(ctx: Context, sender: str, msg: Message):
    # Sending a response message and logging the action
    await ctx.send(sender, Message(text="Hello world from agent!"))
    ctx.logger.info('Response has been sent to agent!')

# Running the agent if the script is executed as the main program
if __name__ == "__main__":
    agent.run()
