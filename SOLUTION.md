# Solution

The algorithm I tried to make simulates the choice of a dot crossing the map from vertices to vertices.
It works on the **hard_to_choose** map, which is the simplest. However it loops on the **islands** map and takes too long in the **Paris_map**.

It uses 3 levels of decisions, depending on the situation.

### 1 : There are unused paths around the dot
Then it should choose one of the heaviests edges at disposal. It does so later in the run, when having to find complex ways to reach the last uncrossed edges,
these complex path can be made of lighter edges and not penalise the score too much.
It seems intuitive, however other setups could be tested.
*last minute update : a quick run choosing the lightest edges shows a slightly better result.*

### 2 : There are no unused paths around the dot (First approach)
The first approach for this is to look in the surroundings if there is an unused edge. In that situation, it is still enough of a short task to 
be done quickly, so why not.

#### 3 : First approach fails - Second approach
Then, we can probably use the distances as a decision basis. The algorithm evaluates the closest unused edge target, and tries finding the closest
vertice to go near it. If this works with non-problematic graphs, it is actually a huge problem when it comes to making sacrifices.
In the **islands** map, there must be one (or **more !**) vertexes that cannot be reached by approaching it, but only by getting far from it where
the only connected edges are. So that kind of approach won't work, as it will loop forever trying to reach the target.

• For that, I implemeted a list of forbidden vertices, which are the ones that have been already visited in the distance algorithm process.

• This is not sufficient, so we might have to do the same with edges (TODO).

• As it is still not guaranteed to work, the only solution might be to start another search where the unreachable target is, so it won't have any
choice but to go back where most of the edges are.


From a computer science point of view, some of the functions are not optimal. For instance, I'm always recalculating distances, always building
long lists of unused paths while I could store them and spare time.
So then :

# TODO
• Make every secondary algorithm optimal in time, to spare time the **Second approach** step mostly.

• Fix the second approach so it works in cases like the **islands map**
