1. Important points using useState

useState updates might happend asynchronously, so if state updates rely on previous state, it is better to use callback functions.

Example - 
```
function ShowApplications(props) {
    const [applications, setApplications] = useState([]);
    props.applications_ids.map((id) => getApplication().then(app => setState([...applications, app])))
    // This approach won't work , as each time application is set to [].
    // To overcome this problem, we use callbacks.
   props.applications_ids.map((id) => getApplication().then(app => setState((applications)=> [...applications, app]))) 
}
```

2. Refs are used to store mutable data across re-renders, that does not trigger a re-render.

3. Using Child Component To render state related information.

By the way the functions which are not hooks and don't render anything must return null.

**Important Thing to study would be AutoSave implementation using useFormikContext**

```
function CountRender() {
    let count = useRef(1);
    useEffect(() => {
        this.count.current += 1.
    })
    return (<p>Rendered {count.current} times</p>)
}

function App() {
    const [count, setCount] = useState(0)
    const handleClick = () => setCount(count => (count + 1))
    return (<CountRender/>)
}

```