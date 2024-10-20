document.querySelector("#form_project").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name_project = document.querySelector("#id_name_project").value;
    const description = document.querySelector("#id_description").value;

    const project = {
        name_project, description
    }

    try {
        const response = await fetch(`${window.location.origin}/projects`, {
            method : 'POST',
            headers : {
                'Content-type' : 'aplication/json'
            },
            body : JSON.stringify(project)
        })
        const data = await response.json()

        console.log(data);
        
    } catch (error) {
        console.log(error.message)
    }

})