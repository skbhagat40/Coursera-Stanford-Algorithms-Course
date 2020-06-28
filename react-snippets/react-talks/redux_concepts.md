Usecase - using @connect with nested components.
Problem - change in store is available to child component almost immediately.

Will lead to error in following scenario - dispatching from componentWillMount, componentWillRecieveProps. Child component is updated almost immediately.
Props snapshot is capture here.

It will go through the render with previous props, for the childComponent (i.e. the props before the dispatch). This creates branching in store. (i.e. parent and child component have two different versions of the store) and this leads to problems.

Parent component looks to store, gets the current page,
check if it is not None - renders the children.

Children also gets it from the store, and renders the component appropriately.

The problem is prop/val gets snapshotted while child updates immediately and renders.

Possible fixes - 
1. Pass Down props.
2. Use React-context-api
3. use SetTimeOut
4. use Redux saga.
