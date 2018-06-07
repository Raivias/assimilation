# Assimilation!
Assimilation is an altered version of tag where the teams grow

## Rules
1) On creation each agent is assigned a team(color)
2) Agents are able to fire their color in the form of bullets at other agents
3) If an Agent is hit by a bullet it becomes an agent of that team

## System Flow
1) Initialize Server   
2) If no agents wait for agents to join   
  2a) When someone joins (Observer or Agent)   
  - Add to subscriber list   
  - Send current state  

3) Send all agents AgentMove msg
  - Kill Agents if they don't move in time/timeout?
  - Wait for all msgs to return

4) Update map
  - Kill any agents that intersect?
  - Update each item location. Check for interactions if items intersect
  - Generate joined agents at random non-intersecting location
  - Remove any bots that have quit

5) Send MapUpdate to Observers and Agents
  - if no ACK remove from list

6) Go back to 2

## More Info
[APIs](/docs/apis.md)
[Sequence](/docs/sequence.png)

## Objects
Communications
- IJoinAPI
- JoinAPI : IJoinAPI
- IStateUpdateAPI
- StateUpdateAPI: IStateUpdateAPI

Map Objects
- IMap
- Map : IMap
- IItem
  - speed limit
  - location
  - size
- AgentFactory
- IAgent :IItem
- Agent : IAgent
- BulletFactory
- IBullet : IItem
- Bullet : IBullet
