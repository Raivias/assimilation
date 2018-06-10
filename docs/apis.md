## API
Set a up api
Msgs that I need to have interaction:
Agent -> Server
- POST Join
#TODO
- Quit
#TODO

Server -> Agent
- GET Move
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

Server -> Observer
- PUT UpdateState
# TODO
