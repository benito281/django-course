console.log("running js")

function alertMessage(icon, title, text){
    return Swal.fire({
                title: title,
                text: text,
                icon: icon
      });
}

document.querySelector("#form_project").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name_project = document.querySelector("#id_name_project").value;
    const description = document.querySelector("#id_description").value;

    const project = {
        name_project, description
    }

    try {
        const response = await fetch(`${window.location.origin}/projects/`, {
            method : 'POST',
            headers : {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // Token CSRF
            },
            body : JSON.stringify(project)
        })
        const data = await response.json()
        alertMessage(data.icon, data.title, data.text)
        console.log(data);
        await allProjects()
    } catch (error) {
        console.log(error.message)
    }

})

 const allProjects = async () => {
    try {
        const response = await fetch(`${window.location.origin}/all_projects/`);
        const data = await response.json()
        console.log(data);
        
    } catch (error) {
        console.log(error.message)
    }
}