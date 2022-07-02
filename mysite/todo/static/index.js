/* Calls get_tasks() function in api/v1 to generate a
   paragraph element containing "Complete Task", "Update", and "Task" buttons
   for each task in the database.*/
function loadList() {
    fetch('api/v1/tasks')
    .then(response => {
        if (!response.ok) {
        throw Error(`${response.status}`);
        }
    return response.json();
    })
    .then(data => {
        const html = data.items.map(task => {
            return `<p id=${task.id}>ID: ${task.id}  ${task.task}
                <button onclick= completeTask(${task.id})>
                    Complete Task </button>
                <button id=${task.id}update onclick=upDate(parentNode)>
                    Update </button></p>`;}).join('');
        document.querySelector('#tasks').insertAdjacentHTML('afterbegin', html);
    })
    .catch(error => {
        console.log(error);
    });
}

/* Try clean(id) to check for search result element.
   If successful, the paragraph element is removed from search results
   and the task list.
   Calls delete_task(id) in api/v1 and removes the
   associated paragraph element to the task being removed.*/

function completeTask(id) {
    fetch(`api/v1/task/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        const div = document.getElementById(id);
        div.remove();
    });
    clean(id);
}

/* Calls post_task() from api/v1 to post new task. (L74-L97),
   The new task text is retrieved from input element.id "new_task"
   and passed into the function as a parameter.
   the new task text is passed to api/v1.post_task() via the request body using fetch(). (L70-L76),
   New paragraph element and buttons created. (L85-L98)*/

function postTask(new_task) {
    const newTask = new FormData();
    newTask.append('task', new_task);
    const data = JSON.stringify({'task': new_task});

    fetch('api/v1/tasks', {
        method: 'POST',
        body: data
    })
    .then(response => {
        if (!response.ok) {
            throw Error(`${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        data = Object.keys(data)
            .map(function(key)
                {return data[key];}
            );
        const html = data.slice(0, 1).map(task => {
            const values = `ID: ${data[0]} ${data[1]}`
            return `<p id=${data[0]}>
                ${values}
                    <button onclick= completeTask(${data[0]})>
                        Complete Task </button>
                    <button id=${data[0]}button onclick=upDate(${data[0]})>
                        Update </button></p>`;
        }).join('');
    document.querySelector('#tasks').insertAdjacentHTML('beforeend', html);
    })
    .catch(error => {
        console.log(error);
    });
    document.getElementById('new_task').value = '';
}


function upDate(element) {
    const id = element.id
    const allButtons = document.querySelectorAll(`button`);
    for (const button of allButtons) {
        if (button.id == `${id}update`) {
            button.disabled = true;
        };
    };
    const text_box = `<input id="txtBox" type="text" name="task_update"/>`;
    const submitButton = `<button id=submit onclick=submit(${id})>
            Submit </button>`;
    const html = (text_box + submitButton);
    element.insertAdjacentHTML('beforeend', html);
}


function submit(id) {
    const element = document.getElementById(id)
    let text = ''
    try{text = element.children.item(2).value}
    catch{text = document.getElementById('txtBox').value}
    const allParagraphs = document.querySelectorAll(`p`)
    for (const task of allParagraphs) {
        if (task.id == element.id) {
            if (task.getAttribute('name') == task.id+'search') {
                console.log(task)
                const html = `<p id=${task.id}>ID: ${task.id}  ${text}
                <button onclick= completeTask(${task.id})>
                    Complete Task </button>
                <button id=${task.id}update onclick=upDate(parentNode)>
                    Update </button>
                <button onclick= clean(parentNode)> Clear </button></p>`;
                task.innerHTML = html
            } else {
                const html = `<p id=${task.id}>ID: ${task.id}  ${text}
                <button onclick= completeTask(${task.id})>
                    Complete Task </button>
                <button id=${task.id}update onclick=upDate(parentNode)>
                    Update </button></p>`;
                task.innerHTML = html
            }
        };
    };
    const text_box_val = JSON.stringify({'task': text});
    fetch(`api/v1/task/${id}`, {
        method: "PUT",
        body: text_box_val
    });
}


function clean(id) {
    const element = document.getElementById(id);
    const allParagraphs = document.querySelectorAll('p');
    for (const task of allParagraphs) {
        if (task.getAttribute('name')) {
            task.remove();
        };
    };
}


function getTask(search) {
    fetch(`api/v1/task/${search}`, {
        method: 'GET'
    })
    .then(response => {
        if (!response.ok) {
            throw Error(`${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        data = Object.keys(data)
                .map(function(key)
                    {return data[key];}
                );
        const html = data.slice(0, 1).map(task => {
            return `<p id=${data[0]} name=${data[0]}search>ID: ${data[0]}  ${data[1]}
                <button onclick= completeTask(${data[0]})>
                    Complete Task </button>
                <button id=${data[0]}update onclick=upDate(parentNode)>
                        Update </button>
                <button onclick= clean(${data[0]})>
                    Clear </button></p>`;}).join('');
        document.querySelector('#results').insertAdjacentHTML('beforeend', html);
    })
    .catch(error => {
        console.log(error);
    });
    document.getElementById('search_task').value = '';
}

function checkEmpty() {
    const addTask = document.getElementById('new_task').value;
    const searchTask = document.getElementById('search_task').value;
    let subText = ''
    try {
        const findParent = document.getElementById('txtBox').parentNode
        subText = findParent.id;
    }
    catch{{};};
    return {subText: subText, addTask: addTask, searchTask: searchTask};
}

// Checks text field boxes and submits existing text to relevant field actions.
function checkBox() {
    const addTask = checkEmpty().addTask
    if (addTask === '') {{};};
    if (!(checkEmpty().addTask === '')) {
        postTask(addTask);
    };

    const searchTask = checkEmpty().searchTask
    if (checkEmpty().searchTask === '') {{};};
    if (!(checkEmpty().searchTask === '')) {
        getTask(searchTask);
    };

    const subText = checkEmpty().subText
    if (checkEmpty().subText === '') {{};};
    if (!(checkEmpty().subText === '')) {
        submit(subText);
    };

    try {if (checkEmpty().subText === '') {{};};
    if (!(checkEmpty().subText === '')) {
        submit(subText.parentNode);
    };}
    catch{{};};
}

// Detects enter key events for both enter buttons.
function pressEnter() {
    document.addEventListener("keyup", function(event) {
        if (event.code === 'Enter') {
            checkBox();
        };
        if (event.code === 'NumpadEnter') {
            checkBox();
        };
    });
}

pressEnter();
loadList();