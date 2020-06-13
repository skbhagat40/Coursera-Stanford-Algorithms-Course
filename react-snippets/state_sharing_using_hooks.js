/* 
Using Hooks to share state between the sibling components.
Parent Child communication - props.
Child Parent Communication - callback function as props.

React Custom Hooks, Important points - 

    1. Two Different components calling the same custom hook do not share the state.
    
    2. When we use a custom Hook, the useState and useEffect behave as if it were called from the component directly, thus triggering re-render.

 */

// Link = https://1drv.ms/u/s!AkicLUy5pNvNmFZgIS5_wDWBGsVp

let state = { value: 1 }

const listeners = []

function updateState(newState) {
    state = newState;
    listeners.forEach(listerner => listerner(state)) // This is just to trigger a re-render.
}

function useCustomHook() {
    let newListener = useState();
    useEffect(() => { listeners.push(newListener) }, []) // To make sure listener is added only once.
    return [state, updateState]
}