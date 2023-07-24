button = document.getElementById('botAction')

button.addEventListener("click", function (e) {
    document.getElementById("botResponse").value = ""
    document.getElementById('userQuestion').disabled = true;
    document.getElementById('botAction').disabled = true;


    const apiURL = "/botInfo";
    const userCode = document.getElementById("userQuestion").value;

    var formData = new FormData();
    formData.append('question', JSON.stringify({ 'content': userCode }));

    fetch(apiURL, {
        method: "post",
        body: formData
    })
        .then(response => response.json())
        .then((response) => {
            const botResp = response?.answer || "Error in fetching"

            document.getElementById("botResponse").value = botResp

            document.getElementById('userQuestion').disabled = false;
            document.getElementById('botAction').disabled = false;

        });
});