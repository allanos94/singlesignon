function saveAnswer(pollId, answerId) {
    console.log('Saving answer')
    const url = "/polls/" + pollId + "/answers/" + answerId + "/edit"
    const value = document.getElementById('form-'+ answerId).value
    console.info(value)
    const fetchPromise = fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            'value': value
        }),
    })

    fetchPromise
        .then(response => {
            const data = response.json()
            showAnswerValue(answerId, data)
            showFlash()
        })
}

function showFlash() {
    const flashElement = document.getElementById('flash')
    flashElement.innerHTML = 'Answer updated successfully'
    flashElement.style.display = 'block'
    setTimeout(hideFlash, 1000)
}

function hideFlash() {
    const flashElement = document.getElementById('flash')
    flashElement.innerHTML = ''
    flashElement.style.display = 'none'
}

function showFormInput(answerId) {
    const spanElement = document.getElementById('read-'+ answerId)
    spanElement.style.display = 'none'
    const inputElement = document.getElementById('edit-'+ answerId)
    inputElement.style.display = 'block'
}

function showAnswerValue(answerId, data) {
    const inputElement = document.getElementById('edit-'+ answerId)
    inputElement.style.display = 'none'
    const valueElement = document.getElementById('value-'+ answerId)
    valueElement.innerHTML = data.value
    const spanElement = document.getElementById('read-'+ answerId)
    spanElement.style.display = 'block'
}