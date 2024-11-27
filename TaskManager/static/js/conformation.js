function register(taskId) {
    const userConfirmed = confirm("Are you sure you want to proceed?");
    if (userConfirmed) {
        // Redirect to the edit URL with the task ID
        const editUrl = `/edit/${taskId}`;
        window.location.href = editUrl;
    }
}

function deleteNow(taskId) {
    const userConfirmed = confirm("Are you sure you want to proceed?");
    if (userConfirmed) {
        // Redirect to the edit URL with the task ID
        const editUrl = `/delete/${taskId}`;
        window.location.href = editUrl;
    }
}