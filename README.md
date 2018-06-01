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

## API
Set a up api
Msgs that I need to have interaction:
Agent -> Server
- Join
#TODO
- Quit
#TODO

Server -> Agent
- AgentMove
send
``` javascript
{
  "agent":
  {
    "name" : "string"
    "team" : GUID,
    "location" :
    {
      "pos":
      [
        int,
        int,

      ],
      "angle" : int
    }
    "size" : int,
    "score" : int,
    "speed limit":
    {
      "pos":
      [
        int,
        int,

      ],
      "angle" : int
    }
  },
  map:
  {
    objects :
    [
      MapObjects
    ]
  }
}
```
return
``` javascript
{
   "agent" :
   {
     "location" :
     {
       "pos":
       [
         int,
         int,

       ],
       "angle" : int
     }
     "fire": bool
   }
}
```
> Should agents have names?

- Dead

Server -> Observer
- MapUpdate

> Note: I can compare intersections to check for conflicts/impacts (if agents hit eachother they should die, or maybe only if it's on a different team?)

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
