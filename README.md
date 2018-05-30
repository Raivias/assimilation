# Assimilation!
Assimilation is an altered version of tag where the teams grow

## Rules
1) On creation each agent is assigned a team(color)
2) Agents are able to fire their color in the form of bullets at other agents
3) If an Agent is hit by a bullet it becomes an agent of that team

## System Flow
1) Initialize Server
2) If no agents wait for agents to join
2) Send all agents AgentMove msg
  - Kill Agents if they don't move in time/timeout?
  - Wait for all msgs to return
3) Update map
  - Kill any agents that intersect?
  - Update each item location. Check for interactions if items intersect
  - Generate joined agents at random non-intersecting location
  - Remove any bots that have quit
4) Go back to

## How can I set this up so agents are async and can be on other machines?
Set a up api
Msgs that I need to have interaction:
Agent -> Server
- Join
- Quit
Server
- AgentMove
  - agent moving
    - team
    - current location
    - size
    - current score
  - current map
    - all agents
      - team
      - current location
      - size
      - current score
    - all bullets
      - team
      - current location
      - size
- Dead


> Note: I can compare intersections to check for conflicts/impacts (if agents hit eachother they should die, or maybe only if it's on a different team?)
