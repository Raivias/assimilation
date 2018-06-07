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
